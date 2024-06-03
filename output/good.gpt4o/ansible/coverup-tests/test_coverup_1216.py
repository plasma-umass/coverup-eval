# file lib/ansible/plugins/callback/junit.py:295-299
# lines [296, 297, 299]
# branches ['296->297', '296->299']

import pytest
from unittest.mock import Mock, patch
from ansible.plugins.callback.junit import CallbackModule

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_v2_runner_on_failed_ignore_errors(callback_module, mocker):
    result = Mock()
    callback_module._fail_on_ignore = 'false'
    mock_finish_task = mocker.patch.object(callback_module, '_finish_task')

    callback_module.v2_runner_on_failed(result, ignore_errors=True)

    mock_finish_task.assert_called_once_with('ok', result)

def test_v2_runner_on_failed_no_ignore_errors(callback_module, mocker):
    result = Mock()
    callback_module._fail_on_ignore = 'true'
    mock_finish_task = mocker.patch.object(callback_module, '_finish_task')

    callback_module.v2_runner_on_failed(result, ignore_errors=True)

    mock_finish_task.assert_called_once_with('failed', result)
