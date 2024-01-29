#!/usr/bin/python3
"""
Script that fetches info about employees' TODO list
and exports data in JSON format.
"""

import json
import requests


def export_todo_to_json():
    base_url = "https://jsonplaceholder.typicode.com"
    users_url = f"{base_url}/users"
    todos_url = f"{base_url}/todos"

    try:
        users_response = requests.get(users_url)
        users_data = users_response.json()

        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        todo_all_employees = {}

        for user in users_data:
            user_id = str(user.get("id"))
            username = user.get("username")

            todo_all_employees[user_id] = []

            user_tasks = [
                    task for task in todos_data
                    if task.get("userId") == user.get("id")
            ]

            for task in user_tasks:
                task_title = task.get("title")
                task_completed = task.get("completed")

                todo_all_employees[user_id].append({
                    "username": username,
                    "task": task_title,
                    "completed": task_completed
                })

        with open("todo_all_employees.json", "w") as json_file:
            json.dump(todo_all_employees, json_file)

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    export_todo_to_json()
