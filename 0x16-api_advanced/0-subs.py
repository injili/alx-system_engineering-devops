#!/usr/bin/python3
"""
A function that querries the Reddit API and returns
the number of subscribers for a given subreddit
"""
import requests

def number_of_subscribers(subreddit):
    """
    If an invalid subreddit is givven the function should return 0
    """
    base_url = 'https://www.reddit.com/r/'
    url = '{}{}/about.json'.format(base_url, subreddit)
    header = {
            'UserAgent':
            'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) \
            Gecko/20100401 Firefox/3.6.3 (FM Scene 4.6.1)'
            }

    result = request.get{
            url,
            headers=headers
            allow_redirect=False
            }

    if results.status_code == 200:
        return result.json()['data']['subscribers']
    return 0
