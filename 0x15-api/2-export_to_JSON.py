#!/usr/bin/python3
"""
Script that exports an employee TODO tasks to a json file
Is an interger representing an employee id.
"""
import json
import requests
import sys


if __name__ == '__main__':
    id_c = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                         .format(id_c)).json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                         .format(sys.argv[1])).json()

    with open("{}.json".format(id_c), "w") as user_id:
        json.dump({id_c: [{
            'task': task.get('title'),
            'completed': task.get('completed'),
            'username': users.get('username')
        } for task in todos]}, user_id)
