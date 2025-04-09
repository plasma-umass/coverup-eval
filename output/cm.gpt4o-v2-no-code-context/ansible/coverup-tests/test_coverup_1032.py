# file: lib/ansible/plugins/callback/junit.py:205-249
# asked: {"lines": [212, 217], "branches": [[211, 212], [216, 217], [242, 249]]}
# gained: {"lines": [212, 217], "branches": [[211, 212], [216, 217]]}

import os
import re
import pytest
from unittest.mock import Mock, patch
from ansible.plugins.callback.junit import CallbackModule
from junit_xml import TestCase, TestSuite

@pytest.fixture
def callback_module():
    return CallbackModule()

@pytest.fixture
def task_data():
    mock_task_data = Mock()
    mock_task_data.play = "play"
    mock_task_data.name = "task"
    mock_task_data.path = "/path/to/task.yml:123"
    mock_task_data.start = 0
    return mock_task_data

@pytest.fixture
def host_data():
    mock_host_data = Mock()
    mock_host_data.name = "host"
    mock_host_data.finish = 10
    mock_host_data.result = Mock()
    mock_host_data.result._result = {}
    return mock_host_data

def test_task_relative_path(callback_module, task_data, host_data, monkeypatch):
    monkeypatch.setattr(callback_module, '_task_relative_path', '/path')
    monkeypatch.setattr(callback_module, '_task_class', 'false')
    host_data.status = 'ok'
    test_case = callback_module._build_test_case(task_data, host_data)
    assert test_case.classname == 'to/task.yml:123'

def test_task_class_true(callback_module, task_data, host_data, monkeypatch):
    monkeypatch.setattr(callback_module, '_task_relative_path', '/path')
    monkeypatch.setattr(callback_module, '_task_class', 'true')
    host_data.status = 'ok'
    test_case = callback_module._build_test_case(task_data, host_data)
    assert test_case.classname == 'to/task'

def test_host_data_skipped_with_reason(callback_module, task_data, host_data):
    host_data.status = 'skipped'
    host_data.result._result = {'skip_reason': 'some reason'}
    test_case = callback_module._build_test_case(task_data, host_data)
    assert test_case.skipped == 'some reason'

def test_host_data_skipped_without_reason(callback_module, task_data, host_data):
    host_data.status = 'skipped'
    host_data.result._result = {}
    test_case = callback_module._build_test_case(task_data, host_data)
    assert test_case.skipped == 'skipped'
