#!/usr/bin/python3

"""Gather data from an API and export the result in JSON format."""

import json
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) != 2:
        exit("Usage: {} <USER_ID>".format(argv[0]))

    user_id = argv[1]
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    todo_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'\
               .format(user_id)

    user = requests.get(user_url).json()
    todos = requests.get(todo_url).json()

    todo_list = []
    for todo in todos:
        task = {
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": user.get("username")
        }
        todo_list.append(task)

    output = {user_id: todo_list}
    with open(user_id + ".json", "w") as json_file:
        json.dump(output, json_file)
