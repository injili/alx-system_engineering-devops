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
