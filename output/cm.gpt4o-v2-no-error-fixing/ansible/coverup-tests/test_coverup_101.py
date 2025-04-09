# file: lib/ansible/plugins/callback/junit.py:133-154
# asked: {"lines": [133, 134, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 149, 151, 153, 154], "branches": [[153, 0], [153, 154]]}
# gained: {"lines": [133, 134, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 149, 151, 153, 154], "branches": [[153, 154]]}

import os
import pytest
from unittest.mock import patch, MagicMock
from ansible.plugins.callback.junit import CallbackModule

@pytest.fixture
def mock_os_environ(monkeypatch):
    env_vars = {
        'JUNIT_OUTPUT_DIR': '/tmp/test_ansible_log',
        'JUNIT_TASK_CLASS': 'True',
        'JUNIT_TASK_RELATIVE_PATH': 'relative/path',
        'JUNIT_FAIL_ON_CHANGE': 'True',
        'JUNIT_FAIL_ON_IGNORE': 'True',
        'JUNIT_INCLUDE_SETUP_TASKS_IN_REPORT': 'False',
        'JUNIT_HIDE_TASK_ARGUMENTS': 'True',
        'JUNIT_TEST_CASE_PREFIX': 'test_prefix'
    }
    for key, value in env_vars.items():
        monkeypatch.setenv(key, value)
    yield
    for key in env_vars.keys():
        monkeypatch.delenv(key, raising=False)

@pytest.fixture
def mock_os_path_exists(monkeypatch):
    def mock_exists(path):
        return False
    monkeypatch.setattr(os.path, 'exists', mock_exists)

@pytest.fixture
def mock_os_makedirs(monkeypatch):
    mock_makedirs = MagicMock()
    monkeypatch.setattr(os, 'makedirs', mock_makedirs)
    return mock_makedirs

def test_callback_module_init(mock_os_environ, mock_os_path_exists, mock_os_makedirs):
    callback = CallbackModule()

    assert callback._output_dir == '/tmp/test_ansible_log'
    assert callback._task_class == 'true'
    assert callback._task_relative_path == 'relative/path'
    assert callback._fail_on_change == 'true'
    assert callback._fail_on_ignore == 'true'
    assert callback._include_setup_tasks_in_report == 'false'
    assert callback._hide_task_arguments == 'true'
    assert callback._test_case_prefix == 'test_prefix'
    assert callback._playbook_path is None
    assert callback._playbook_name is None
    assert callback._play_name is None
    assert callback._task_data == {}
    assert callback.disabled is False
    mock_os_makedirs.assert_called_once_with('/tmp/test_ansible_log')
