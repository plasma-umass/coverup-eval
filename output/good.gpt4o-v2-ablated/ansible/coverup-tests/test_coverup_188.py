# file: lib/ansible/plugins/callback/default.py:399-405
# asked: {"lines": [399, 400, 401, 402, 403, 404, 405], "branches": [[403, 404], [403, 405]]}
# gained: {"lines": [399, 400, 401, 402, 403, 404, 405], "branches": [[403, 404], [403, 405]]}

import pytest
from unittest.mock import Mock, patch
from ansible.plugins.callback.default import CallbackModule
from ansible.plugins.callback import CallbackBase
from ansible.utils.display import Display
import ansible.constants as C

@pytest.fixture
def mock_result():
    result = Mock()
    result.task_name = "test_task"
    result._task = "test_task_fallback"
    result._result = {'retries': 3, 'attempts': 1}
    return result

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_v2_runner_retry_basic(mock_result, callback_module, mocker):
    mocker.patch.object(callback_module, 'host_label', return_value='test_host')
    mocker.patch.object(callback_module, '_run_is_verbose', return_value=False)
    mock_display = mocker.patch.object(callback_module, '_display', new_callable=Mock)
    
    callback_module.v2_runner_retry(mock_result)
    
    expected_msg = "FAILED - RETRYING: [test_host]: test_task (2 retries left)."
    mock_display.display.assert_called_once_with(expected_msg, color=C.COLOR_DEBUG)

def test_v2_runner_retry_verbose(mock_result, callback_module, mocker):
    mocker.patch.object(callback_module, 'host_label', return_value='test_host')
    mocker.patch.object(callback_module, '_run_is_verbose', return_value=True)
    mocker.patch.object(callback_module, '_dump_results', return_value='dumped_result')
    mock_display = mocker.patch.object(callback_module, '_display', new_callable=Mock)
    
    callback_module.v2_runner_retry(mock_result)
    
    expected_msg = "FAILED - RETRYING: [test_host]: test_task (2 retries left).Result was: dumped_result"
    mock_display.display.assert_called_once_with(expected_msg, color=C.COLOR_DEBUG)

def test_v2_runner_retry_no_task_name(mock_result, callback_module, mocker):
    mock_result.task_name = None
    mocker.patch.object(callback_module, 'host_label', return_value='test_host')
    mocker.patch.object(callback_module, '_run_is_verbose', return_value=False)
    mock_display = mocker.patch.object(callback_module, '_display', new_callable=Mock)
    
    callback_module.v2_runner_retry(mock_result)
    
    expected_msg = "FAILED - RETRYING: [test_host]: test_task_fallback (2 retries left)."
    mock_display.display.assert_called_once_with(expected_msg, color=C.COLOR_DEBUG)
