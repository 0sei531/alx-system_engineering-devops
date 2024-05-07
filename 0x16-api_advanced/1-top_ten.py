#!/usr/bin/python3
"""Module for task 1"""

import requests


def top_ten(subreddit):
    """Queries the Reddit API and returns
       the top 10 hot posts of the subreddit
    """
    user_agent = {"User-Agent": "My-User-Agent"}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    try:
        response = requests.get(url, headers=user_agent, allow_redirects=False)
        response.raise_for_status()  # Raise exception for non-2xx status codes

        data = response.json().get("data")
        if data:
            for child in data.get("children"):
                print(child.get("data").get("title"))
        else:
            print("None")
    except requests.RequestException:
        print("None")
