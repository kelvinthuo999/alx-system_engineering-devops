#!/usr/bin/python3
"""
Reddit API Subreddit Subscriber Count
--------------------------------------
This module provides a function to query the Reddit API and return the number
of subscribers for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.

    Args:
    - subreddit: A string representing the subreddit name.

    Returns:
    - integer rep the num of subs, or 0 if the subreddit is invalid.
    """

    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    headers = {"User-Agent": "my_bot/0.1"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        return data["data"]["subscribers"]
    else:
        return 0
