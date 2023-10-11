#!/usr/bin/python3
"""
A function to find the first 10 hot posts for a given subreddit
"""
import requests


def top_ten(subreddit):
    """
    if not a valid subreddit we print None
    """
    base_url = 'https://www.reddit.com/r/'
    sort = 'top'
    limit = 10
    url = '{}{}/about.json?sort={}&limit={}'.format(
        base_url, subreddit, sort, limit)
    headers = {
            'User-Agent':
            'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) \
            Gecko/20100401 Firefox/3.6.3 (FM Scene 4.6.1)'
            }

    result = requests.get(
            url,
            headers=headers,
            allow_redirects=False
            )

    if result.status_code == 200:
        for post in result.json()['data']['children'][0:10]:
            print(post['data']['title'])
    else:
        print(None)
