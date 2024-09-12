# file: lib/ansible/plugins/callback/default.py:136-151
# asked: {"lines": [136, 138, 140, 142, 143, 145, 146, 148, 149, 150, 151], "branches": [[138, 0], [138, 140], [142, 143], [142, 145], [145, 146], [145, 148], [149, 150], [149, 151]]}
# gained: {"lines": [136, 138, 140, 142, 143, 145, 146, 148, 149, 150, 151], "branches": [[138, 140], [142, 143], [145, 146], [145, 148], [149, 150], [149, 151]]}

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
    result._result = {'_ansible_verbose_always': False, '_ansible_verbose_override': False}
    result._task.action = 'some_action'
    result._task._uuid = '1234'
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
    result._task._uuid = '1234'
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
    result._result = {'_ansible_verbose_always': False, '_ansible_verbose_override': False}
    result._task.action = 'some_action'
    result._task._uuid = '1234'
    result._task.loop = None
    result._host.get_name.return_value = 'localhost'

    with patch.object(callback_module, '_clean_results') as mock_clean_results, \
         patch.object(callback_module, '_print_task_banner') as mock_print_task_banner, \
         patch.object(callback_module, '_run_is_verbose', return_value=True) as mock_run_is_verbose, \
         patch.object(callback_module, '_dump_results', return_value='dumped_results') as mock_dump_results:
        
        callback_module.v2_runner_on_skipped(result)
        
        mock_clean_results.assert_called_once_with(result._result, result._task.action)
        mock_print_task_banner.assert_called_once_with(result._task)
        mock_run_is_verbose.assert_called_once_with(result)
        mock_dump_results.assert_called_once_with(result._result)
        callback_module._display.display.assert_called_once_with('skipping: [localhost] => dumped_results', color=C.COLOR_SKIP)
