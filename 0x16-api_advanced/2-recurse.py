#!/usr/bin/python3
"""
Reddit API Recursive Query
--------------------------
This module provides a recursive function
to query the Reddit API and return
a list containing the titles of all hot articles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    Recursively queries the Reddit API
    and returns a list containing the titles
    of all hot articles for a given subreddit.

    Args:
    - subreddit: A string representing the subreddit name.
    - hot_list: A list to store the titles
    of hot articles (default is None).
    - after: A string representing
    the "after" parameter for pagination (default is None).

    Returns:
    - A list containing the titles of all hot articles,
    or None if no results are found.
    """
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    if after:
        url += f"&after={after}"

    headers = {"User-Agent": "my_bot/0.1"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]
        if len(posts) == 0:
            return hot_list
        else:
            for post in posts:
                hot_list.append(post["data"]["title"])
            after = data["data"]["after"]
            return recurse(subreddit, hot_list, after)
    else:
        return None
