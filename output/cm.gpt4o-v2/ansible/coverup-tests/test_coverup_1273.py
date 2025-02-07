# file: lib/ansible/plugins/callback/default.py:136-151
# asked: {"lines": [], "branches": [[138, 0], [142, 145]]}
# gained: {"lines": [], "branches": [[138, 0]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.callback.default import CallbackModule
from ansible import constants as C

@pytest.fixture
def callback_module():
    module = CallbackModule()
    module.display_skipped_hosts = True
    module._last_task_banner = None
    module._display = MagicMock()
    return module

def test_v2_runner_on_skipped_display_skipped_hosts(callback_module):
    result = MagicMock()
    result._result = {}
    result._task.action = 'some_action'
    result._task._uuid = 'unique_task_id'
    result._task.loop = None
    result._host.get_name.return_value = 'localhost'

    with patch.object(callback_module, '_clean_results') as mock_clean_results, \
         patch.object(callback_module, '_print_task_banner') as mock_print_task_banner, \
         patch.object(callback_module, '_run_is_verbose', return_value=False) as mock_run_is_verbose:
        
        callback_module.v2_runner_on_skipped(result)
        
        mock_clean_results.assert_called_once_with(result._result, result._task.action)
        mock_print_task_banner.assert_called_once_with(result._task)
        callback_module._display.display.assert_called_once_with('skipping: [localhost]', color=C.COLOR_SKIP)

def test_v2_runner_on_skipped_with_loop(callback_module):
    result = MagicMock()
    result._result = {'results': []}
    result._task.action = 'some_action'
    result._task._uuid = 'unique_task_id'
    result._task.loop = True
    result._host.get_name.return_value = 'localhost'

    with patch.object(callback_module, '_clean_results') as mock_clean_results, \
         patch.object(callback_module, '_print_task_banner') as mock_print_task_banner, \
         patch.object(callback_module, '_process_items') as mock_process_items:
        
        callback_module.v2_runner_on_skipped(result)
        
        mock_clean_results.assert_called_once_with(result._result, result._task.action)
        mock_print_task_banner.assert_called_once_with(result._task)
        mock_process_items.assert_called_once_with(result)

def test_v2_runner_on_skipped_verbose(callback_module):
    result = MagicMock()
    result._result = {}
    result._task.action = 'some_action'
    result._task._uuid = 'unique_task_id'
    result._task.loop = None
    result._host.get_name.return_value = 'localhost'

    with patch.object(callback_module, '_clean_results') as mock_clean_results, \
         patch.object(callback_module, '_print_task_banner') as mock_print_task_banner, \
         patch.object(callback_module, '_run_is_verbose', return_value=True) as mock_run_is_verbose, \
         patch.object(callback_module, '_dump_results', return_value='dumped_results') as mock_dump_results:
        
        callback_module.v2_runner_on_skipped(result)
        
        mock_clean_results.assert_called_once_with(result._result, result._task.action)
        mock_print_task_banner.assert_called_once_with(result._task)
        callback_module._display.display.assert_called_once_with('skipping: [localhost] => dumped_results', color=C.COLOR_SKIP)

def test_v2_runner_on_skipped_no_display_skipped_hosts(callback_module):
    callback_module.display_skipped_hosts = False
    result = MagicMock()
    result._result = {}
    result._task.action = 'some_action'
    result._task._uuid = 'unique_task_id'
    result._task.loop = None
    result._host.get_name.return_value = 'localhost'

    with patch.object(callback_module, '_clean_results') as mock_clean_results, \
         patch.object(callback_module, '_print_task_banner') as mock_print_task_banner, \
         patch.object(callback_module, '_run_is_verbose', return_value=False) as mock_run_is_verbose:
        
        callback_module.v2_runner_on_skipped(result)
        
        mock_clean_results.assert_not_called()
        mock_print_task_banner.assert_not_called()
        callback_module._display.display.assert_not_called()
