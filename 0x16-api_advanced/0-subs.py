#!/usr/bin/python3

"""
The function th number_of_subscribers queries the
Reddit API returning the number of subscribers
"""


def number_of_subscribers(subreddit):
    """
    Args:
        subreddit : the subreddit to find subscribers from
    Returns the number of subscribers
    """
    import requests

    r = requests.get('https://www.reddit.com/r/{}/about.json'
                     .format(subreddit),
                     headers={'User-Agent': 'My-User-Agent'},
                     allow_redirects=False)

    if r.status_code == 200:
        return r.json().get('data').get('subscribers')

    return 0
