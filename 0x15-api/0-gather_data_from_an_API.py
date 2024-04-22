#!/usr/bin/env python3
"""
Gathers data from a REST API about a given employee's TODO list progress
"""

import requests
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    api_url = 'https://jsonplaceholder.typicode.com/'

    # Fetch user data
    response_user = requests.get(api_url + 'users/' + user_id)
    user_data = response_user.json()
    employee_name = user_data.get('name')

    # Fetch tasks data
    response_tasks = requests.get(api_url + 'todos', params={'userId': user_id})
    tasks_data = response_tasks.json()

    # Calculate progress
    total_tasks = len(tasks_data)
    completed_tasks = sum(task['completed'] for task in tasks_data)

    # Display progress
    print(f"Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):")
    for task in tasks_data:
        if task['completed']:
            print(f"\t {task['title']}")

