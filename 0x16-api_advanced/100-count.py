#!/usr/bin/python3
"""
Reddit API Word Count
---------------------
This module provides a recursive function to query the Reddit API,
parse the titles of all hot articles,
and print a sorted count of given keywords (case-insensitive).
"""

import requests


def count_words(subreddit, word_list, after=None, counts={}):
    """
    Recursively queries the Reddit API,
    parses the title of all hot articles, and prints
    a sorted count of given keywords (case-insensitive).

    Args:
    - subreddit: A string representing the subreddit name.
    - word_list: A list of keywords to count.
    - after: A string rep the "after" parameter
    for pagination (default is None).
    - counts: A dictionary to store the counts
    of each keyword (default is {}).

    Returns:
    - None
    """
    if not word_list:
        return

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    if after:
        url += f"&after={after}"

    headers = {"User-Agent": "my_bot/0.1"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]
        if len(posts) == 0:
            sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print(f"{word.lower()}: {count}")
            return
        else:
            for post in posts:
                title = post["data"]["title"].lower()
                for word in word_list:
                    if word.lower() in title.split():
                        counts[word.lower()] = counts.get(word.lower(), 0) + 1
            after = data["data"]["after"]
            return count_words(subreddit, word_list, after, counts)
    else:
        return
