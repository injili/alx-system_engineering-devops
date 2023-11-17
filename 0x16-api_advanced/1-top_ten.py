#!/usr/bin/python3

"""
The function top_ten prints the titles
of the top 10 hot posts for a given subreddit
"""


def top_ten(subreddit):
    """
    Args:
        subreddit: the subreddit to fetch the posts from
    """

    import requests

    r = requests.get('https://www.reddit.com/r/{}/hot.json?limit=10'
                     .format(subreddit),
                     headers={'User-Agent': 'My-User-Agent'},
                     allow_redirects=False)

    if r.status_code == 200:
        [print(child.get('data').get('title'))
         for child in r.json().get('data').get('children')]
    else:
        print('None')
