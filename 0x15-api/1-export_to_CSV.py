#!/usr/bin/python3
"""
Python script that fetch data from an API and exports it in CSV format
"""
import csv
import requests
import sys

if __name__ == "__main__":
    emp_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/"
    emp_data = requests.get(f"{base_url}users/{emp_id}").json()
    emp_username = emp_data.get("username")
    todos = requests.get(f"{base_url}todos", params={"userId": emp_id}).json()

    with open(f"{emp_id}.csv", "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [csv_writer.writerow(
            [emp_id, emp_username, todo.get("completed"), todo.get("title")]
            ) for todo in todos]
