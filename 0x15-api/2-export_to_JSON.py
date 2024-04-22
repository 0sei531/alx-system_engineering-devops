#!/usr/bin/python3
"""Exports all to-do list information for all employees to JSON format."""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    users = requests.get(url + "/users").json()

    all_tasks = {}

    for user in users:
        user_id = user["id"]
        username = user["username"]

        todos_url = url + "/todos"
        todos_params = {"userId": user_id}
        todos = requests.get(todos_url, params=todos_params).json()

        user_tasks = []
        for todo in todos:
            task = {
                "username": username,
                "task": todo["title"],
                "completed": todo["completed"]
            }
            user_tasks.append(task)

        all_tasks[str(user_id)] = user_tasks

    output_file = "todo_all_employees.json"
    with open(output_file, "w") as jsonfile:
        json.dump(all_tasks, jsonfile)
