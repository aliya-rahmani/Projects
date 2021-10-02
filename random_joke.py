"""
Random Programming Related Jokes Genrator
Author: https://github.com/akashrchandran
"""

#imports
import requests
from colorama import Fore

url = 'https://v2.jokeapi.dev/joke/Programming?type=twopart'

#get random jokes from a free API and jsonify
response = requests.get(url).json()

setup = '[?] ' + response['setup']
delivery = '>> ' + response['delivery']

#printing the jokes in different colours to look good
print(Fore.RED + setup)
print(Fore.GREEN + delivery)
