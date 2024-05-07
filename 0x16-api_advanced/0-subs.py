#!/usr/bin/python3
"""Module for task 0"""

import requests


def number_of_subscribers(subreddit):
    """
       Queries the Reddit API and returns the
       number of subscribers to the subreddit
    """
    user_agent = {"User-Agent": "My-User-Agent"}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    try:
        response = requests.get(url, headers=user_agent, allow_redirects=False)
        response.raise_for_status()  # Raise exception for non-2xx status codes

        data = response.json().get("data")
        if data:
            return data.get("subscribers", 0)
        else:
            return 0
    except requests.RequestException:
        return 0
