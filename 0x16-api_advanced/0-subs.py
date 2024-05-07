#!/usr/bin/python3
"""
Retrieve the number of subscribers for a given subreddit using Reddit API.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Retrieve the number of subscribers for a given subreddit.

    Args:
    subreddit (str): The name of the subreddit.

    Returns:
    int: The number of subscribers,
    or 0 if the subreddit is invalid or inaccessible.
    """

    if not subreddit or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    url = ('https://www.reddit.com/r/{}/about'
           '.json').format(subreddit)

    try:
        response = requests.get(url, headers=user_agent)
        response.raise_for_status()  # Raise exception for non-2xx status codes
        data = response.json()
        return data.get('data', {}).get('subscribers', 0)
    except (requests.RequestException, ValueError, KeyError):
        return 0
