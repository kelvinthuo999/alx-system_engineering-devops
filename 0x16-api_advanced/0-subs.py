#!/usr/bin/python3
"""Function to get the number of subscribers for a given subreddit."""

import requests

def number_of_subscribers(subreddit):
    """Returns the number of subscribers for the given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()['data']['subscribers']
    return 0
