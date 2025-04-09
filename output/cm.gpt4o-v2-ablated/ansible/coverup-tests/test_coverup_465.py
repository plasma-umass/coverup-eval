# file: lib/ansible/plugins/callback/junit.py:133-154
# asked: {"lines": [154], "branches": [[153, 154]]}
# gained: {"lines": [154], "branches": [[153, 154]]}

import os
import pytest
from unittest.mock import patch, MagicMock

from ansible.plugins.callback.junit import CallbackModule

@pytest.fixture
def mock_env(monkeypatch):
    monkeypatch.setenv('JUNIT_OUTPUT_DIR', '/tmp/.ansible.log')
    monkeypatch.setenv('JUNIT_TASK_CLASS', 'True')
    monkeypatch.setenv('JUNIT_TASK_RELATIVE_PATH', 'relative/path')
    monkeypatch.setenv('JUNIT_FAIL_ON_CHANGE', 'True')
    monkeypatch.setenv('JUNIT_FAIL_ON_IGNORE', 'True')
    monkeypatch.setenv('JUNIT_INCLUDE_SETUP_TASKS_IN_REPORT', 'False')
    monkeypatch.setenv('JUNIT_HIDE_TASK_ARGUMENTS', 'True')
    monkeypatch.setenv('JUNIT_TEST_CASE_PREFIX', 'prefix_')

@pytest.fixture
def mock_os_path_exists(monkeypatch):
    mock_exists = MagicMock(return_value=False)
    monkeypatch.setattr(os.path, 'exists', mock_exists)
    return mock_exists

@pytest.fixture
def mock_os_makedirs(monkeypatch):
    mock_makedirs = MagicMock()
    monkeypatch.setattr(os, 'makedirs', mock_makedirs)
    return mock_makedirs

def test_callback_module_initialization(mock_env, mock_os_path_exists, mock_os_makedirs):
    callback = CallbackModule()

    assert callback._output_dir == '/tmp/.ansible.log'
    assert callback._task_class == 'true'
    assert callback._task_relative_path == 'relative/path'
    assert callback._fail_on_change == 'true'
    assert callback._fail_on_ignore == 'true'
    assert callback._include_setup_tasks_in_report == 'false'
    assert callback._hide_task_arguments == 'true'
    assert callback._test_case_prefix == 'prefix_'
    assert callback._playbook_path is None
    assert callback._playbook_name is None
    assert callback._play_name is None
    assert callback._task_data == {}
    assert callback.disabled is False

    mock_os_path_exists.assert_called_once_with('/tmp/.ansible.log')
    mock_os_makedirs.assert_called_once_with('/tmp/.ansible.log')
