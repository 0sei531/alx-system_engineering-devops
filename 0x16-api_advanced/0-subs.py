#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """
    Retrieve the total number of subscribers for a given subreddit.

    Args:
    subreddit (str): The name of the subreddit to query.

    Returns:
    int: The total number of subscribers if the subreddit exists, otherwise 0.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get("data")
        if data:
            return data.get("subscribers", 0)
    return 0
