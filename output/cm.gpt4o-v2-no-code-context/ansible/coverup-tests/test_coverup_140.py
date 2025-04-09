# file: lib/ansible/plugins/callback/junit.py:133-154
# asked: {"lines": [133, 134, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 149, 151, 153, 154], "branches": [[153, 0], [153, 154]]}
# gained: {"lines": [133, 134, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 149, 151, 153, 154], "branches": [[153, 154]]}

import os
import pytest
from unittest.mock import patch, MagicMock
from ansible.plugins.callback.junit import CallbackModule

@pytest.fixture
def mock_env_vars(monkeypatch):
    monkeypatch.setenv('JUNIT_OUTPUT_DIR', '/tmp/test_ansible_log')
    monkeypatch.setenv('JUNIT_TASK_CLASS', 'True')
    monkeypatch.setenv('JUNIT_TASK_RELATIVE_PATH', 'relative/path')
    monkeypatch.setenv('JUNIT_FAIL_ON_CHANGE', 'True')
    monkeypatch.setenv('JUNIT_FAIL_ON_IGNORE', 'True')
    monkeypatch.setenv('JUNIT_INCLUDE_SETUP_TASKS_IN_REPORT', 'False')
    monkeypatch.setenv('JUNIT_HIDE_TASK_ARGUMENTS', 'True')
    monkeypatch.setenv('JUNIT_TEST_CASE_PREFIX', 'prefix_')

@pytest.fixture
def cleanup():
    yield
    if os.path.exists('/tmp/test_ansible_log'):
        os.rmdir('/tmp/test_ansible_log')

def test_callback_module_initialization(mock_env_vars, cleanup):
    with patch('os.makedirs') as mock_makedirs:
        callback = CallbackModule()
        assert callback._output_dir == '/tmp/test_ansible_log'
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
        mock_makedirs.assert_called_once_with('/tmp/test_ansible_log')
