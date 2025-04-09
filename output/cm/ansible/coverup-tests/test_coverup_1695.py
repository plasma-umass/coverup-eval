# file lib/ansible/plugins/callback/default.py:306-315
# lines [314]
# branches ['307->exit', '308->311', '313->314']

import pytest
from ansible.plugins.callback.default import CallbackModule
from ansible.executor.task_result import TaskResult
from unittest.mock import MagicMock, patch

@pytest.fixture
def callback_module():
    callback = CallbackModule()
    callback._display = MagicMock()
    callback._display.verbosity = 0  # Set verbosity to an integer to fix TypeError
    callback._last_task_banner = None
    callback.display_skipped_hosts = True
    callback.check_mode_markers = False
    callback._task_type_cache = {}  # Added to avoid KeyError
    callback._last_task_name = None  # Added to avoid AttributeError
    return callback

@pytest.fixture
def task_result():
    mock_task = MagicMock()
    mock_task._uuid = 'test_uuid'
    mock_host = MagicMock()
    mock_host.get_name.return_value = 'test_host'
    mock_result = {'skipped': True, 'item': 'test_item'}
    result = TaskResult(host=mock_host, task=mock_task, return_data=mock_result)
    return result

def test_v2_runner_item_on_skipped_verbose(callback_module, task_result):
    with patch.object(callback_module, '_run_is_verbose', return_value=True), \
         patch.object(callback_module, '_clean_results'), \
         patch.object(callback_module, '_get_item_label', return_value='test_item'), \
         patch.object(callback_module, '_dump_results', return_value='dumped_results'):
        callback_module.v2_runner_item_on_skipped(task_result)
        callback_module._display.display.assert_called_once()
        assert callback_module._display.display.call_args[0][0].endswith(' => dumped_results')

def test_v2_runner_item_on_skipped_not_verbose(callback_module, task_result):
    with patch.object(callback_module, '_run_is_verbose', return_value=False), \
         patch.object(callback_module, '_clean_results'), \
         patch.object(callback_module, '_get_item_label', return_value='test_item'):
        callback_module.v2_runner_item_on_skipped(task_result)
        callback_module._display.display.assert_called_once()
        assert not callback_module._display.display.call_args[0][0].endswith(' => dumped_results')
