#!/usr/bin/python3
"""
The function recurse is a recursive function that
returns a list containing the titles of all
hot articles for a subreddit
"""
import requests


def recurse(subreddit, hot_list=[], count=0, after=None):
    """
    Args:
        subreddit: The subreddit to search for the posts from
        hot_list: the list of the posts
        count
        after
    """
    if hot_list is None:
        hot_list = []

    r = requests.get('https://www.reddit.com/r/{}/hot.json'
                     .format(subreddit),
                     params={'count': count, 'after': after},
                     headers={'User-Agent': 'My-User-Agent'},
                     allow_redirects=False)

    if r.status_code >= 400:
        return None

    hot = hot_list + [
                      child.get('data').get('title')
                      for child in r.json().get('data')
                      .get('children')]

    info = r.json()
    if not info.get('data').get('after'):
        return hot

    return recurse(subreddit, hot, info.get('data').get('count'),
                   info.get('data').get('after'))
