import random

import requests
import json
import CONST as C
import os.path

FILES_DIR = os.path.dirname(__file__)
ARCHIVE_NAME = '10bunkers.zip'


def get_path(filename: str):
    return os.path.join(FILES_DIR, filename)


ARCHIVE_FILE_PATH = get_path(filename=ARCHIVE_NAME)


# def to_json(labels: list, response_url):
#     return {'labels': ''.join(str(label) for label in labels),
#             'responseUrl': response_url}


def create_task_archive(labels, response_url):
    url = f'{C.IP}/api/v1/process/archive'
    payload = {'labels': labels,
               'responseUrl': response_url,
               'resultsTransport': 'HTTP'
               }
    files = [
        ('zip', (ARCHIVE_NAME, open(ARCHIVE_FILE_PATH, 'rb'), 'application/zip'))
    ]
    # print(ARCHIVE_FILE_PATH, labels)
    response = requests.post(url, data=payload, files=files)
    return response


def get_task_result(task_id):
    url = f"{C.IP}/api/v1/tasks/{task_id}/results"
    headers = C.APPLICATION_HEADERS
    return requests.get(url, headers=headers)


def get_task_info(task_id):
    url = f"{C.IP}/api/v1/tasks/{task_id}"
    headers = C.APPLICATION_HEADERS
    return requests.get(url, headers=headers)


def get_tasks():
    # не придумал как добавить фильтры в функцию status from to
    url = f'{C.IP}/api/v1/tasks'
    headers = C.APPLICATION_HEADERS
    return requests.get(url, headers=headers)


def change_task_status(task_id, action):
    url = f"{C.IP}/tasks/{task_id}/{action}"
    headers = C.APPLICATION_HEADERS
    return requests.post(url, headers=headers)


def get_labels():
    url = f"{C.IP}/api/v1/labels"
    headers = C.APPLICATION_HEADERS
    return requests.get(url, headers=headers)






