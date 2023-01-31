#!/usr/bin/python3

"""
returns a list containing titles of all hot articles.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    ''' function recurse :Get ALL hot posts'''
    headers = {"User-Agent":
               """Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"""}
    params = {'limit': 100}
    if isinstance(after, str):
        if after != "STOP":
            params['after'] = after
        else:
            return hot_list
    response = requests.get('http://reddit.com/r/{}/hot.json'.format(
                            subreddit),
                            headers=headers, params=params)
    if response.status_code != 200:
        return None
    data = response.json().get('data', {})
    after = data.get('after', 'STOP')
    if not after:
        after = "STOP"
    hot_list = hot_list + [post.get('data', {}).get('title')
                           for post in data.get('children', [])]
    return recurse(subreddit, hot_list, after)
