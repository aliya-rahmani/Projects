import pandas as pd
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import argparse
import sys

#TESTING URLS
# "https://www.imdb.com/title/tt5753856" DARK
# "https://www.imdb.com/title/tt0098904" SEINFLED
# "https://www.imdb.com/title/tt0306414" THEWIRE
# "https://www.imdb.com/title/tt0096697" Simpsons
# "https://www.imdb.com/title/tt0903747" BreakingBad

# Arguments
parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", help = "URL to show page",required=True)
parser.add_argument("-f", "--file", help = "Filename to save data to",default='data')
args = parser.parse_args()

url = args.url
csvName = args.file

# Get Show Home Page
try:
	res = requests.get(url)
except:
	print("Invalid URL\nMust follow IMDB Link format\nExample: https://www.imdb.com/title/tt1266020")
	sys.exit()

soup = BeautifulSoup(res.text,features='lxml')

# Extract Show Name
subs = soup.find("div",{"class":"title_wrapper"})
showName = subs.find('h1').text.encode('ascii','ignore').decode('utf-8')
print(f"Getting data for {showName}")

# Get number of seasons
subs = soup.findAll("div",{"class":"seasons-and-year-nav"})
numberOfSeason = subs[0].find('a')
numberOfSeason = int(numberOfSeason.text)
print(f"Fetching Data for {numberOfSeason} seasons")

# Update url to iterate over seasons
if url[-1] == '/':
	url = url[:-1]
url += "/episodes?season={}"

data = []

# Manipulates incoming data and adds to data list
def addData(data,row_data,isVote=False):
	if len(data)>0:
		if isVote:
			row_data.append(data[0].text.replace('(','').replace(')','').replace(',',''))
		else:
			row_data.append(data[0].text)
	else:
		row_data.append("")
	return row_data

# Iterate of seasons webpages and scrape episode wise data
for season in tqdm(range(1,numberOfSeason+1)):
	with requests.get(url.format(season)) as resp:
		html = resp.text
		soup = BeautifulSoup(html,features="lxml")
		episodes = soup.findAll("div", {"class": "list_item"})

		for episode in episodes:
			row_data = []
			title = episode.findAll("a", {"itemprop": "name"})
			airdate = episode.findAll("div", {"class": "airdate"})
			rating = episode.findAll("span", {"class": "ipl-rating-star__rating"})
			num_votes = episode.findAll("span", {"class": "ipl-rating-star__total-votes"})
			description = episode.findAll("div", {"class": "item_description"})
			
			row_data.append(season)
			row_data = addData(title,row_data)
			row_data = addData(airdate,row_data)
			row_data = addData(rating,row_data)
			row_data = addData(num_votes,row_data,isVote=True)
			row_data = addData(description,row_data)

			# row_data = [season,title[0].text,airdate[0].text,rating[0].text,num_votes[0].text.replace('(','').replace(')','').replace(',',''),description[0].text]
			row_data = [r.replace('\n','').strip() if isinstance(r,str) else r for r in row_data ]
			data.append(row_data)


# Save data to Dataframe making it easier to save to csv
df = pd.DataFrame(data, columns=["Season","Title","Airdate","Rating","Vote_count","Description"])
df.to_csv(csvName + '.csv',index=False)
print(f"Data saved to {csvName}.csv Successfully")