# -*- coding: utf-8 -*-

import datetime
import requests
import time


def reddit(sub: str = None):
    """Grabs upto top 100 posts from any subreddit"""
    sub = str(input("What's the name of the sub?\n"))
    start = datetime.datetime.now()
    print("\nConnecting...\n")
    url = f'https://www.reddit.com/r/{sub}/top.json?sort=top&limit=100'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/41.0.2228.0 Safari/537.36'}

    r = requests.get(url, headers=headers)
    if r.status_code != 200:
        print("Failed D:")
        time.sleep(3)
        exit()

    resp = r.json()
    total = resp["data"]["dist"]
    if total == 0:
        print("Sorry! Nothing found :(")
        time.sleep(3)
        exit()

    print(f"Connected! - Total Posts Found : {total}\n")
    posts = resp["data"]["children"]
    for post in posts:
        title = post['data']['title']
        source = post['data']['url']
        print(title, source, sep=" - ")
    end = datetime.datetime.now()
    total_time = (end - start).total_seconds()
    print(f"\nDone!")

    input(f"Total time taken : {total_time} seconds")


if __name__ == '__main__':
    reddit()
