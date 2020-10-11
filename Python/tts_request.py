"""
You need install Requests library.

Author: Gabriel Rodrigues Segalla
"""

import requests
import json
import webbrowser


r = requests.post('https://ttsmp3.com/makemp3_new.php', data={
    'msg': 'Hello World. #HacktoberFest',
    'lang': 'Joey',
    'source': 'ttsmp3'
})
resp = r.json()
webbrowser.open(resp['URL'])


