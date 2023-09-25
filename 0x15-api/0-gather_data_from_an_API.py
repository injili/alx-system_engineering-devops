#!/usr/bin/python3
"""
This script fetches an employee's ID using RETSTFUL api
"""
import json
import requests
import sys


base_url = 'https://jsonplaceholder.typicode.com'

if __name__ == "__main__":

    user_id = sys.argv[1]
    user_url = '{}/users?id={}'.format(base_url, user_id)
    response = requests.get(user_url)
    data = response.text
    data = json.loads(data)
    name = data[0].get('name')
    tasks_url = '{}/todos?userId={}'.format(base_url, user_id)
    response = requests.get(tasks_url)
    tasks = response.text
    tasks = json.loads(tasks)

    # initialize completed count as 0 and find total number of tasks
    completed = 0
    total_tasks = len(tasks)

    completed_tasks = []
    # loop through tasks counting number of completed tasks
    for task in tasks:

        if task.get('completed'):
            # print("The tasks are: {}\n".format(task))
            completed_tasks.append(task)
            completed += 1

    # print the output in the required format
    print("Employee {} is done with tasks({}/{}):"
          .format(name, completed, total_tasks))
    for task in completed_tasks:
        print("\t {}".format(task.get('title')))
