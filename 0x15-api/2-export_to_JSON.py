#!/usr/bin/python3
"""
Python script that, using a given REST API, retrieves information about an
employee's TODO list progress and exports data in JSON format.
"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: {} <employee_id>".format(argv[0]))
    else:
        employee_id = int(argv[1])
        base_url = "https://jsonplaceholder.typicode.com"
        user_url = "{}/users/{}".format(base_url, employee_id)
        todo_url = "{}/todos?userId={}".format(base_url, employee_id)

        try:
            user_response = requests.get(user_url)
            user_data = user_response.json()
            todo_response = requests.get(todo_url)
            todo_data = todo_response.json()

            user_id = str(user_data.get("id"))
            username = user_data.get("username")

            json_data = {user_id: []}

            for task in todo_data:
                task_title = task.get("title")
                task_completed = task.get("completed")

                json_data[user_id].append({
                    "task": task_title,
                    "completed": task_completed,
                    "username": username
                })

            with open(f"{user_id}.json", "w") as json_file:
                json.dump(json_data, json_file)

        except requests.exceptions.RequestException as e:
            print("Error: {}".format(e))
