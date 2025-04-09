# file: lib/ansible/plugins/callback/junit.py:156-174
# asked: {"lines": [156, 159, 161, 162, 164, 165, 166, 167, 169, 170, 171, 172, 174], "branches": [[161, 162], [161, 164], [169, 170], [169, 174], [171, 172], [171, 174]]}
# gained: {"lines": [156, 159, 161, 162, 164, 165, 166, 167, 169, 170, 171, 172, 174], "branches": [[161, 162], [161, 164], [169, 170], [169, 174], [171, 172]]}

import pytest
from unittest.mock import Mock
from ansible.plugins.callback.junit import CallbackModule, TaskData

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_start_task_new_task(callback_module):
    task = Mock()
    task._uuid = "1234"
    task.get_name.return_value = "test_task"
    task.get_path.return_value = "/path/to/task"
    task.action = "test_action"
    task.no_log = False
    task.args = {"arg1": "value1", "arg2": "value2"}

    callback_module._play_name = "test_play"
    callback_module._hide_task_arguments = 'false'

    callback_module._start_task(task)

    assert "1234" in callback_module._task_data
    task_data = callback_module._task_data["1234"]
    assert task_data.name == "test_task arg1=value1, arg2=value2"
    assert task_data.path == "/path/to/task"
    assert task_data.play == "test_play"
    assert task_data.action == "test_action"

def test_start_task_existing_task(callback_module):
    task = Mock()
    task._uuid = "1234"
    callback_module._task_data["1234"] = TaskData("1234", "existing_task", "/path/to/task", "test_play", "test_action")

    callback_module._start_task(task)

    assert callback_module._task_data["1234"].name == "existing_task"

def test_start_task_no_log(callback_module):
    task = Mock()
    task._uuid = "1234"
    task.get_name.return_value = "test_task"
    task.get_path.return_value = "/path/to/task"
    task.action = "test_action"
    task.no_log = True
    task.args = {"arg1": "value1", "arg2": "value2"}

    callback_module._play_name = "test_play"
    callback_module._hide_task_arguments = 'false'

    callback_module._start_task(task)

    assert "1234" in callback_module._task_data
    task_data = callback_module._task_data["1234"]
    assert task_data.name == "test_task"
    assert task_data.path == "/path/to/task"
    assert task_data.play == "test_play"
    assert task_data.action == "test_action"

def test_start_task_hide_arguments(callback_module):
    task = Mock()
    task._uuid = "1234"
    task.get_name.return_value = "test_task"
    task.get_path.return_value = "/path/to/task"
    task.action = "test_action"
    task.no_log = False
    task.args = {"arg1": "value1", "arg2": "value2"}

    callback_module._play_name = "test_play"
    callback_module._hide_task_arguments = 'true'

    callback_module._start_task(task)

    assert "1234" in callback_module._task_data
    task_data = callback_module._task_data["1234"]
    assert task_data.name == "test_task"
    assert task_data.path == "/path/to/task"
    assert task_data.play == "test_play"
    assert task_data.action == "test_action"
