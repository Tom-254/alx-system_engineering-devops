#!/usr/bin/python3

"""
function that queries Reddit API and returns
number of subscribers (not active users, total subscribers)
"""
import json
import requests


def number_of_subscribers(subreddit):
    """ return number of subscribers """
    res = requests.get(
        "https://www.reddit.com/r/{}/about.json"
        .format(subreddit),
        headers={"User-Agent":
                 """Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"""})
    if res.status_code == 200:
        return res.json().get("data").get("subscribers")
    else:
        return 0
