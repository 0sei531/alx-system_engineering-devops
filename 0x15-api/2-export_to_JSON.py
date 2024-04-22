#!/usr/bin/env python3
"""
Exports data in JSON format from a given API endpoint based on user ID
"""

import json
import requests
from sys import argv


if __name__ == "__main__":
    user_id = argv[1]
    api_url = 'https://jsonplaceholder.typicode.com/'

    # Fetch tasks data from API
    response = requests.get(api_url + 'todos')
    tasks = response.json()

    # Filter tasks owned by the specified user ID
    user_tasks = [task for task in tasks if str(task['userId']) == user_id]

    # Format tasks into JSON format
    data = {user_id: [{"task": task["title"], "completed": task["completed"], "username": "USERNAME"} for task in user_tasks]}

    # Write data into JSON file
    with open(f'{user_id}.json', 'w') as json_file:
        json.dump(data, json_file)
