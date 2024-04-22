#!/usr/bin/python3
""" Queries REST API for employee info, exports to CSV
    "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
    argv 1 = int employee ID
"""
import csv
import requests
from sys import argv

def export_to_csv(user_id):
    url = "https://jsonplaceholder.typicode.com/"
    
    # Retrieve user information
    user_response = requests.get(url + "users/{}".format(user_id))
    user_data = user_response.json()
    username = user_data.get("username")
    
    # Retrieve user's tasks
    tasks_response = requests.get(url + "todos", params={"userId": user_id})
    tasks_data = tasks_response.json()
    
    # Write data to CSV file
    with open('{}.csv'.format(user_id), 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in tasks_data:
            csv_writer.writerow([user_id, username, task["completed"], task["title"]])

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: {} <employee_id>".format(argv[0]))
        exit(1)
    user_id = argv[1]
    export_to_csv(user_id)
