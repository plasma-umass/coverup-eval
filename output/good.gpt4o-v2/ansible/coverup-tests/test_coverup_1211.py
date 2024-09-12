# file: lib/ansible/plugins/callback/default.py:399-405
# asked: {"lines": [400, 401, 402, 403, 404, 405], "branches": [[403, 404], [403, 405]]}
# gained: {"lines": [400, 401, 402, 403, 404, 405], "branches": [[403, 404], [403, 405]]}

import pytest
from unittest.mock import Mock, patch
from ansible.plugins.callback.default import CallbackModule
from ansible import constants as C

@pytest.fixture
def mock_result():
    result = Mock()
    result.task_name = "test_task"
    result._task = Mock()
    result._task.delegate_to = None
    result._result = {
        'retries': 3,
        'attempts': 1,
        '_ansible_verbose_always': False,
        '_ansible_verbose_override': False
    }
    result._host.get_name.return_value = "localhost"
    return result

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_v2_runner_retry_non_verbose(callback_module, mock_result):
    with patch.object(callback_module._display, 'display') as mock_display:
        callback_module.v2_runner_retry(mock_result)
        mock_display.assert_called_once_with(
            "FAILED - RETRYING: [localhost]: test_task (2 retries left).", 
            color=C.COLOR_DEBUG
        )

def test_v2_runner_retry_verbose(callback_module, mock_result):
    mock_result._result['_ansible_verbose_always'] = True
    with patch.object(callback_module._display, 'display') as mock_display, \
         patch.object(callback_module, '_dump_results', return_value="dumped_result"):
        callback_module.v2_runner_retry(mock_result)
        mock_display.assert_called_once_with(
            "FAILED - RETRYING: [localhost]: test_task (2 retries left).Result was: dumped_result", 
            color=C.COLOR_DEBUG
        )
