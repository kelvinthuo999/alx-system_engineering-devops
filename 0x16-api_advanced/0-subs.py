#!/usr/bin/python3
"""Module to query the Reddit API"""

import requests

def number_of_subscribers(subreddit):
    """Function to get the number of subscribers for a subreddit.

    Args:
        subreddit (str): The subreddit name.

    Returns:
        int: The number of subscribers, or 0 if the subreddit is invalid.
    """
    headers = {'User-Agent': 'MyUniqueUserAgent'}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        return response.json().get("data").get("subscribers")
    return 0
