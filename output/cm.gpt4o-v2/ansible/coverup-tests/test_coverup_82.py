# file: lib/ansible/plugins/callback/default.py:263-288
# asked: {"lines": [263, 265, 266, 267, 268, 269, 270, 272, 273, 275, 276, 278, 279, 281, 282, 284, 285, 286, 287, 288], "branches": [[266, 267], [266, 268], [268, 269], [268, 275], [269, 270], [269, 272], [275, 276], [275, 278], [278, 279], [278, 281], [286, 287], [286, 288]]}
# gained: {"lines": [263, 265, 266, 267, 268, 269, 270, 272, 273, 275, 276, 278, 279, 281, 282, 284, 285, 286, 287, 288], "branches": [[266, 267], [266, 268], [268, 269], [268, 275], [269, 270], [275, 276], [275, 278], [278, 279], [286, 287], [286, 288]]}

import pytest
from unittest.mock import Mock, patch
from ansible.plugins.callback.default import CallbackModule
from ansible.playbook.task_include import TaskInclude
from ansible import constants as C

@pytest.fixture
def callback_module():
    cb = CallbackModule()
    cb._last_task_banner = None
    cb.display_ok_hosts = True
    cb._display = Mock()
    return cb

def test_v2_runner_item_on_ok_task_include(callback_module):
    result = Mock()
    result._task = TaskInclude()
    callback_module.v2_runner_item_on_ok(result)
    callback_module._display.display.assert_not_called()

def test_v2_runner_item_on_ok_changed(callback_module):
    result = Mock()
    result._task._uuid = '1234'
    result._task.action = 'test_action'
    result._result = {'changed': True}
    callback_module._last_task_banner = '5678'
    
    with patch.object(callback_module, 'host_label', return_value='host_label'), \
         patch.object(callback_module, '_print_task_banner') as mock_print_task_banner, \
         patch.object(callback_module, '_get_item_label', return_value='item_label'), \
         patch.object(callback_module, '_clean_results'), \
         patch.object(callback_module, '_run_is_verbose', return_value=False):
        
        callback_module.v2_runner_item_on_ok(result)
        
        mock_print_task_banner.assert_called_once_with(result._task)
        callback_module._display.display.assert_called_once_with(
            'changed: [host_label] => (item=item_label)', color=C.COLOR_CHANGED
        )

def test_v2_runner_item_on_ok_not_changed_display_ok_hosts(callback_module):
    result = Mock()
    result._task._uuid = '1234'
    result._task.action = 'test_action'
    result._result = {'changed': False}
    callback_module._last_task_banner = '5678'
    
    with patch.object(callback_module, 'host_label', return_value='host_label'), \
         patch.object(callback_module, '_print_task_banner') as mock_print_task_banner, \
         patch.object(callback_module, '_get_item_label', return_value='item_label'), \
         patch.object(callback_module, '_clean_results'), \
         patch.object(callback_module, '_run_is_verbose', return_value=False):
        
        callback_module.v2_runner_item_on_ok(result)
        
        mock_print_task_banner.assert_called_once_with(result._task)
        callback_module._display.display.assert_called_once_with(
            'ok: [host_label] => (item=item_label)', color=C.COLOR_OK
        )

def test_v2_runner_item_on_ok_not_changed_not_display_ok_hosts(callback_module):
    result = Mock()
    result._task._uuid = '1234'
    result._task.action = 'test_action'
    result._result = {'changed': False}
    callback_module.display_ok_hosts = False
    
    callback_module.v2_runner_item_on_ok(result)
    callback_module._display.display.assert_not_called()

def test_v2_runner_item_on_ok_verbose(callback_module):
    result = Mock()
    result._task._uuid = '1234'
    result._task.action = 'test_action'
    result._result = {'changed': True}
    callback_module._last_task_banner = '5678'
    
    with patch.object(callback_module, 'host_label', return_value='host_label'), \
         patch.object(callback_module, '_print_task_banner'), \
         patch.object(callback_module, '_get_item_label', return_value='item_label'), \
         patch.object(callback_module, '_clean_results'), \
         patch.object(callback_module, '_run_is_verbose', return_value=True), \
         patch.object(callback_module, '_dump_results', return_value='dumped_results'):
        
        callback_module.v2_runner_item_on_ok(result)
        
        callback_module._display.display.assert_called_once_with(
            'changed: [host_label] => (item=item_label) => dumped_results', color=C.COLOR_CHANGED
        )
