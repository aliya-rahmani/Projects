xpath = '//*[@id="quote-header-info"]/div[3]/div[1]/div/span[1]'
website = "https://finance.yahoo.com/quote/TSLA/"
limit = 480.00

from selenium import webdriver
import time, yagmail

driver = webdriver.Chrome(executable_path=r'C:\Users\HP Gold\Desktop\Programs\Python\Web Automation\chromedriver.exe')

driver.set_page_load_timeout(30)
driver.get(website)

def send(price):
    receiver = dest_email
    yag = yagmail.SMTP(email_address,password)
    yag.send(
        to=receiver,
        subject="TESLA stock",
        contents=f"The current price for Tesla on Yahoo Finance is at {str(price)}!"
    )
    print("Sent done")

while True:
    #try:
        elem_xp = driver.find_elements_by_xpath(xpath)

        for i in range(len(elem_xp)):
            
            stuff = elem_xp[i]
            
            source_code = stuff.get_attribute("outerHTML")
            
            source_code = source_code[74::]
            source_code = source_code[0:6:]
            source_code = float(source_code)
            print(float(source_code))

        if source_code > limit:
            send(source_code)
            time.sleep(30)
        
    #except:
    #    print("an error has occured")


    
