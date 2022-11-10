import time

import requests
import json
import CONST as C
import main as m


def test_create_task(random_labels):
    response = m.create_task_archive(random_labels, C.RESPONSE_URL)
    assert (response.status_code == 200) & (type(response.json()["data"]["taskUuid"]) == str)


def test_create_task_get_info(random_labels):
    response = m.create_task_archive(random_labels, C.RESPONSE_URL)
    task_id = response.json()["data"]["taskUuid"]
    info = m.get_task_info(task_id)
    assert (info.status_code == 200) & \
           (info.json()["data"]["uuid"] == task_id) & \
           (info.json()["data"]["status"] == "in progress") & \
           (info.json()["data"]["responseUrl"] == C.RESPONSE_URL)


def test_create_task_get_result(random_labels):
    response = m.create_task_archive(random_labels, C.RESPONSE_URL)
    task_id = response.json()["data"]["taskUuid"]
    time.sleep(5)
    result = m.get_task_result(task_id)
    assert result.status_code == 200


def test_get_created_task(random_labels):
    task = m.create_task_archive(random_labels, C.RESPONSE_URL)
    task_id = task.json()["data"]["taskUuid"]
    response = m.get_tasks()
    # print(random_labels.split(","))
    # print((response.json()["data"][-1]["labels"]))
    assert (response.json()["data"][-1]["uuid"] == task_id) & \
           (response.json()["data"][-1]["labels"] == random_labels.split(","))
