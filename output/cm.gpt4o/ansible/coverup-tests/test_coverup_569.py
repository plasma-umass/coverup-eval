# file lib/ansible/plugins/callback/junit.py:95-132
# lines [95, 96, 128, 129, 130, 131]
# branches []

import os
import pytest
from unittest.mock import patch, MagicMock
from ansible.plugins.callback.junit import CallbackModule

@pytest.fixture
def mock_env_vars():
    env_vars = {
        'JUNIT_OUTPUT_DIR': '/tmp',
        'JUNIT_TASK_CLASS': 'True',
        'JUNIT_TASK_RELATIVE_PATH': '/relative/path',
        'JUNIT_FAIL_ON_CHANGE': 'True',
        'JUNIT_FAIL_ON_IGNORE': 'True',
        'JUNIT_INCLUDE_SETUP_TASKS_IN_REPORT': 'False',
        'JUNIT_HIDE_TASK_ARGUMENTS': 'True',
        'JUNIT_TEST_CASE_PREFIX': 'test_'
    }
    with patch.dict(os.environ, env_vars):
        yield env_vars

def test_callback_module_initialization(mock_env_vars):
    callback = CallbackModule()
    
    assert callback.CALLBACK_VERSION == 2.0
    assert callback.CALLBACK_TYPE == 'aggregate'
    assert callback.CALLBACK_NAME == 'junit'
    assert callback.CALLBACK_NEEDS_ENABLED is True

    assert os.environ['JUNIT_OUTPUT_DIR'] == '/tmp'
    assert os.environ['JUNIT_TASK_CLASS'] == 'True'
    assert os.environ['JUNIT_TASK_RELATIVE_PATH'] == '/relative/path'
    assert os.environ['JUNIT_FAIL_ON_CHANGE'] == 'True'
    assert os.environ['JUNIT_FAIL_ON_IGNORE'] == 'True'
    assert os.environ['JUNIT_INCLUDE_SETUP_TASKS_IN_REPORT'] == 'False'
    assert os.environ['JUNIT_HIDE_TASK_ARGUMENTS'] == 'True'
    assert os.environ['JUNIT_TEST_CASE_PREFIX'] == 'test_'
