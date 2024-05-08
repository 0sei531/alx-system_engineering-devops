#!/usr/bin/python3

"""Queries the Reddit API for subreddit subscriber count."""


import requests
import sys

def number_of_subscribers(subreddit):
    """Return total number of subscribers on a subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "My-User-Agent"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json().get("data")
            return data.get("subscribers")
        else:
            return 0
    except requests.RequestException as e:
        print(f"Error occurred: {e}")
        return 0

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        subscribers = number_of_subscribers(subreddit)
        if subscribers != 0:
            print("Existing Subreddit")
        else:
            print("Non-existing subreddit")
