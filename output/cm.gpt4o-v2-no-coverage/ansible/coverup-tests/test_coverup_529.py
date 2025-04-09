# file: lib/ansible/plugins/callback/default.py:399-405
# asked: {"lines": [399, 400, 401, 402, 403, 404, 405], "branches": [[403, 404], [403, 405]]}
# gained: {"lines": [399, 400, 401, 402, 403, 404, 405], "branches": [[403, 404], [403, 405]]}

import pytest
from unittest.mock import Mock, patch
from ansible.plugins.callback.default import CallbackModule
from ansible import constants as C

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_v2_runner_retry(callback_module, mocker):
    result = Mock()
    result.task_name = "test_task"
    result._task = "default_task"
    result._result = {'retries': 3, 'attempts': 1}
    
    mocker.patch.object(callback_module, 'host_label', return_value="localhost")
    mocker.patch.object(callback_module, '_run_is_verbose', return_value=True)
    mocker.patch.object(callback_module, '_dump_results', return_value="dumped_results")
    mock_display = mocker.patch.object(callback_module._display, 'display')

    callback_module.v2_runner_retry(result)

    expected_msg = "FAILED - RETRYING: [localhost]: test_task (2 retries left).Result was: dumped_results"
    mock_display.assert_called_once_with(expected_msg, color=C.COLOR_DEBUG)

def test_v2_runner_retry_non_verbose(callback_module, mocker):
    result = Mock()
    result.task_name = None
    result._task = "default_task"
    result._result = {'retries': 3, 'attempts': 1}
    
    mocker.patch.object(callback_module, 'host_label', return_value="localhost")
    mocker.patch.object(callback_module, '_run_is_verbose', return_value=False)
    mock_display = mocker.patch.object(callback_module._display, 'display')

    callback_module.v2_runner_retry(result)

    expected_msg = "FAILED - RETRYING: [localhost]: default_task (2 retries left)."
    mock_display.assert_called_once_with(expected_msg, color=C.COLOR_DEBUG)
