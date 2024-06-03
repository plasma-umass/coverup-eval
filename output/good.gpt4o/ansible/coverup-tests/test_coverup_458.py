# file lib/ansible/plugins/callback/default.py:399-405
# lines [399, 400, 401, 402, 403, 404, 405]
# branches ['403->404', '403->405']

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.callback.default import CallbackModule
from ansible.plugins.callback import CallbackBase
from ansible.utils.display import Display
import ansible.constants as C

@pytest.fixture
def mock_result():
    result = MagicMock()
    result.task_name = "test_task"
    result._task = "test_task"
    result._result = {'retries': 3, 'attempts': 1}
    return result

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_v2_runner_retry(mock_result, callback_module, mocker):
    mocker.patch.object(callback_module, 'host_label', return_value='test_host')
    mocker.patch.object(callback_module, '_run_is_verbose', return_value=True)
    mocker.patch.object(callback_module, '_dump_results', return_value='mocked_result')
    mocker.patch.object(callback_module, '_display', Display())
    mocker.patch.object(callback_module._display, 'display')

    callback_module.v2_runner_retry(mock_result)

    expected_msg = "FAILED - RETRYING: [test_host]: test_task (2 retries left).Result was: mocked_result"
    callback_module._display.display.assert_called_once_with(expected_msg, color=C.COLOR_DEBUG)
