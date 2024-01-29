#!/usr/bin/python3
"""
Python script that, using a given REST API, retrieves information about an
employee's TODO list progress based on the employee ID.
"""

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

            employee_name = user_data.get("name")
            total_tasks = len(todo_data)
            comp_tsks = sum(1 for task in todo_data if task.get("completed"))

            print("Employee {} is done with tasks({}/{}):".format(
                employee_name, comp_tsks, total_tasks))

            for task in todo_data:
                if task.get("completed"):
                    print("\t {}".format(task.get("title")))

        except requests.exceptions.RequestException as e:
            print("Error: {}".format(e))
