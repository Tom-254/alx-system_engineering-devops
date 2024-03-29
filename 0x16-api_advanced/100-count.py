#!/usr/bin/python3
"""
parses title of all hot articles, and prints a sorted count
of given keywords (case-insensitive, delimited by spaces.
Javascript should count as javascript, but java should not).
"""
import re
import requests


def count_words(subreddit, word_list, hot_list=[], after=None):
    '''function count_words : Get ALL hot posts'''
    headers = {'User-agent':
               """Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"""}
    params = {'limit': 100}
    if isinstance(after, str):
        if after != "STOP":
            params['after'] = after
        else:
            return print_results(word_list, hot_list)

    response = requests.get(
        'http://reddit.com/r/{}/hot.json'.format(subreddit),
        headers=headers, params=params)
    if response.status_code != 200:
        return None
    data = response.json().get('data', {})
    after = data.get('after', 'STOP')
    if not after:
        after = "STOP"
    hot_list = hot_list + [post.get('data', {}).get('title')
                           for post in data.get('children', [])]
    return count_words(subreddit, word_list, hot_list, after)


def print_results(word_list, hot_list):
    '''function print_results :Prints request results'''
    count = {}
    for word in word_list:
        count[word] = 0
    for title in hot_list:
        for word in word_list:
            count[word] = count[word] +\
                len(re.findall(r'(?:^| ){}(?:$| )'.format(word), title, re.I))

    count = {k: v for k, v in count.items() if v > 0}
    words = sorted(list(count.keys()))
    for word in sorted(words,
                       reverse=True, key=lambda k: count[k]):
        print("{}: {}".format(word, count[word]))
