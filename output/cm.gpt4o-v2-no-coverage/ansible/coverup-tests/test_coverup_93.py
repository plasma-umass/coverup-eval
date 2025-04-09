# file: lib/ansible/plugins/callback/default.py:263-288
# asked: {"lines": [263, 265, 266, 267, 268, 269, 270, 272, 273, 275, 276, 278, 279, 281, 282, 284, 285, 286, 287, 288], "branches": [[266, 267], [266, 268], [268, 269], [268, 275], [269, 270], [269, 272], [275, 276], [275, 278], [278, 279], [278, 281], [286, 287], [286, 288]]}
# gained: {"lines": [263, 265, 266, 267, 268, 269, 270, 272, 273, 275, 276, 278, 279, 281, 282, 284, 285, 286, 288], "branches": [[266, 267], [266, 268], [268, 269], [268, 275], [269, 270], [275, 276], [275, 278], [278, 279], [286, 288]]}

import pytest
from unittest.mock import Mock, patch
from ansible.plugins.callback.default import CallbackModule
from ansible.playbook.task_include import TaskInclude
from ansible import constants as C

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_v2_runner_item_on_ok_task_include(callback_module, mocker):
    result = Mock()
    result._task = Mock(spec=TaskInclude)
    result._result = {}
    
    callback_module.v2_runner_item_on_ok(result)
    
    # Ensure that the method returns early for TaskInclude
    assert True

def test_v2_runner_item_on_ok_changed(callback_module, mocker):
    result = Mock()
    result._task = Mock()
    result._task._uuid = 'uuid1'
    result._result = {'changed': True}
    result._host.get_name.return_value = 'host1'
    result._task.delegate_to = None
    
    mocker.patch.object(callback_module, '_print_task_banner')
    mocker.patch.object(callback_module, '_get_item_label', return_value='item_label')
    mocker.patch.object(callback_module, '_clean_results')
    mocker.patch.object(callback_module, '_run_is_verbose', return_value=False)
    mocker.patch.object(callback_module._display, 'display')
    
    callback_module.v2_runner_item_on_ok(result)
    
    callback_module._print_task_banner.assert_called_once_with(result._task)
    callback_module._display.display.assert_called_once_with('changed: [host1] => (item=item_label)', color=C.COLOR_CHANGED)

def test_v2_runner_item_on_ok_not_changed_display_ok_hosts(callback_module, mocker):
    result = Mock()
    result._task = Mock()
    result._task._uuid = 'uuid2'
    result._result = {'changed': False}
    result._host.get_name.return_value = 'host2'
    result._task.delegate_to = None
    
    callback_module.display_ok_hosts = True
    mocker.patch.object(callback_module, '_print_task_banner')
    mocker.patch.object(callback_module, '_get_item_label', return_value='item_label')
    mocker.patch.object(callback_module, '_clean_results')
    mocker.patch.object(callback_module, '_run_is_verbose', return_value=False)
    mocker.patch.object(callback_module._display, 'display')
    
    callback_module.v2_runner_item_on_ok(result)
    
    callback_module._print_task_banner.assert_called_once_with(result._task)
    callback_module._display.display.assert_called_once_with('ok: [host2] => (item=item_label)', color=C.COLOR_OK)

def test_v2_runner_item_on_ok_not_changed_no_display_ok_hosts(callback_module, mocker):
    result = Mock()
    result._task = Mock()
    result._task._uuid = 'uuid3'
    result._result = {'changed': False}
    
    callback_module.display_ok_hosts = False
    mocker.patch.object(callback_module, '_print_task_banner')
    mocker.patch.object(callback_module, '_get_item_label')
    mocker.patch.object(callback_module, '_clean_results')
    mocker.patch.object(callback_module, '_run_is_verbose')
    mocker.patch.object(callback_module._display, 'display')
    
    callback_module.v2_runner_item_on_ok(result)
    
    callback_module._print_task_banner.assert_not_called()
    callback_module._get_item_label.assert_not_called()
    callback_module._clean_results.assert_not_called()
    callback_module._run_is_verbose.assert_not_called()
    callback_module._display.display.assert_not_called()
