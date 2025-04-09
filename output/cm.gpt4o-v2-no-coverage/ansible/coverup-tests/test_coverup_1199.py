# file: lib/ansible/plugins/callback/default.py:263-288
# asked: {"lines": [287], "branches": [[269, 272], [278, 281], [286, 287]]}
# gained: {"lines": [287], "branches": [[286, 287]]}

import pytest
from unittest.mock import Mock, patch
from ansible.plugins.callback.default import CallbackModule
from ansible.playbook.task_include import TaskInclude
from ansible import constants as C

@pytest.fixture
def callback_module():
    module = CallbackModule()
    module._last_task_banner = None
    module.display_ok_hosts = True
    module._display = Mock()
    module._task_type_cache = {}
    module._last_task_name = None
    module.check_mode_markers = True
    return module

def test_v2_runner_item_on_ok_task_include(callback_module):
    result = Mock()
    result._task = Mock(spec=TaskInclude)
    callback_module.v2_runner_item_on_ok(result)
    callback_module._display.display.assert_not_called()

def test_v2_runner_item_on_ok_changed(callback_module):
    result = Mock()
    result._task._uuid = 'uuid1'
    result._task.action = 'action'
    result._task.delegate_to = None
    result._host.get_name.return_value = 'host'
    result._result = {'changed': True}
    callback_module._last_task_banner = 'uuid2'
    
    with patch.object(callback_module, '_print_task_banner') as mock_print_task_banner, \
         patch.object(callback_module, '_get_item_label', return_value='item_label') as mock_get_item_label, \
         patch.object(callback_module, '_clean_results') as mock_clean_results, \
         patch.object(callback_module, '_run_is_verbose', return_value=False) as mock_run_is_verbose:
        
        callback_module.v2_runner_item_on_ok(result)
        
        mock_print_task_banner.assert_called_once_with(result._task)
        mock_get_item_label.assert_called_once_with(result._result)
        mock_clean_results.assert_called_once_with(result._result, result._task.action)
        callback_module._display.display.assert_called_once_with('changed: [host] => (item=item_label)', color=C.COLOR_CHANGED)

def test_v2_runner_item_on_ok_ok(callback_module):
    result = Mock()
    result._task._uuid = 'uuid1'
    result._task.action = 'action'
    result._task.delegate_to = None
    result._host.get_name.return_value = 'host'
    result._result = {'changed': False}
    callback_module._last_task_banner = 'uuid2'
    
    with patch.object(callback_module, '_print_task_banner') as mock_print_task_banner, \
         patch.object(callback_module, '_get_item_label', return_value='item_label') as mock_get_item_label, \
         patch.object(callback_module, '_clean_results') as mock_clean_results, \
         patch.object(callback_module, '_run_is_verbose', return_value=False) as mock_run_is_verbose:
        
        callback_module.v2_runner_item_on_ok(result)
        
        mock_print_task_banner.assert_called_once_with(result._task)
        mock_get_item_label.assert_called_once_with(result._result)
        mock_clean_results.assert_called_once_with(result._result, result._task.action)
        callback_module._display.display.assert_called_once_with('ok: [host] => (item=item_label)', color=C.COLOR_OK)

def test_v2_runner_item_on_ok_verbose(callback_module):
    result = Mock()
    result._task._uuid = 'uuid1'
    result._task.action = 'action'
    result._task.delegate_to = None
    result._host.get_name.return_value = 'host'
    result._result = {'changed': False}
    callback_module._last_task_banner = 'uuid2'
    
    with patch.object(callback_module, '_print_task_banner') as mock_print_task_banner, \
         patch.object(callback_module, '_get_item_label', return_value='item_label') as mock_get_item_label, \
         patch.object(callback_module, '_clean_results') as mock_clean_results, \
         patch.object(callback_module, '_run_is_verbose', return_value=True) as mock_run_is_verbose, \
         patch.object(callback_module, '_dump_results', return_value='dumped_results') as mock_dump_results:
        
        callback_module.v2_runner_item_on_ok(result)
        
        mock_print_task_banner.assert_called_once_with(result._task)
        mock_get_item_label.assert_called_once_with(result._result)
        mock_clean_results.assert_called_once_with(result._result, result._task.action)
        callback_module._display.display.assert_called_once_with('ok: [host] => (item=item_label) => dumped_results', color=C.COLOR_OK)
