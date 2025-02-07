# file: lib/ansible/plugins/callback/default.py:263-288
# asked: {"lines": [], "branches": [[269, 272], [278, 281]]}
# gained: {"lines": [], "branches": [[269, 272], [278, 281]]}

import pytest
from unittest.mock import Mock, patch
from ansible.plugins.callback.default import CallbackModule
from ansible.playbook.task_include import TaskInclude
from ansible import constants as C

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_v2_runner_item_on_ok_changed(callback_module, mocker):
    result = Mock()
    result._task._uuid = '1234'
    result._task.action = 'test_action'
    result._result = {'changed': True}
    result._task.no_log = False
    result._task.args = {}
    result._task.check_mode = False

    mocker.patch.object(callback_module, '_last_task_banner', '5678')
    mocker.patch.object(callback_module, '_print_task_banner')
    mocker.patch.object(callback_module, 'host_label', return_value='host1')
    mocker.patch.object(callback_module, '_get_item_label', return_value='item1')
    mocker.patch.object(callback_module, '_clean_results')
    mocker.patch.object(callback_module, '_run_is_verbose', return_value=False)
    mocker.patch.object(callback_module, '_display')
    
    callback_module.v2_runner_item_on_ok(result)
    
    callback_module._print_task_banner.assert_called_once_with(result._task)
    callback_module._display.display.assert_called_once_with('changed: [host1] => (item=item1)', color=C.COLOR_CHANGED)

def test_v2_runner_item_on_ok_ok(callback_module, mocker):
    result = Mock()
    result._task._uuid = '1234'
    result._task.action = 'test_action'
    result._result = {'changed': False}
    result._task.no_log = False
    result._task.args = {}
    result._task.check_mode = False

    # Mocking display_ok_hosts as an instance attribute
    callback_module.display_ok_hosts = True
    mocker.patch.object(callback_module, '_last_task_banner', '5678')
    mocker.patch.object(callback_module, '_print_task_banner')
    mocker.patch.object(callback_module, 'host_label', return_value='host1')
    mocker.patch.object(callback_module, '_get_item_label', return_value='item1')
    mocker.patch.object(callback_module, '_clean_results')
    mocker.patch.object(callback_module, '_run_is_verbose', return_value=False)
    mocker.patch.object(callback_module, '_display')
    
    callback_module.v2_runner_item_on_ok(result)
    
    callback_module._print_task_banner.assert_called_once_with(result._task)
    callback_module._display.display.assert_called_once_with('ok: [host1] => (item=item1)', color=C.COLOR_OK)

def test_v2_runner_item_on_ok_changed_no_last_task_banner(callback_module, mocker):
    result = Mock()
    result._task._uuid = '1234'
    result._task.action = 'test_action'
    result._result = {'changed': True}
    result._task.no_log = False
    result._task.args = {}
    result._task.check_mode = False

    mocker.patch.object(callback_module, '_last_task_banner', '1234')
    mocker.patch.object(callback_module, '_print_task_banner')
    mocker.patch.object(callback_module, 'host_label', return_value='host1')
    mocker.patch.object(callback_module, '_get_item_label', return_value='item1')
    mocker.patch.object(callback_module, '_clean_results')
    mocker.patch.object(callback_module, '_run_is_verbose', return_value=False)
    mocker.patch.object(callback_module, '_display')
    
    callback_module.v2_runner_item_on_ok(result)
    
    callback_module._print_task_banner.assert_not_called()
    callback_module._display.display.assert_called_once_with('changed: [host1] => (item=item1)', color=C.COLOR_CHANGED)

def test_v2_runner_item_on_ok_ok_no_last_task_banner(callback_module, mocker):
    result = Mock()
    result._task._uuid = '1234'
    result._task.action = 'test_action'
    result._result = {'changed': False}
    result._task.no_log = False
    result._task.args = {}
    result._task.check_mode = False

    # Mocking display_ok_hosts as an instance attribute
    callback_module.display_ok_hosts = True
    mocker.patch.object(callback_module, '_last_task_banner', '1234')
    mocker.patch.object(callback_module, '_print_task_banner')
    mocker.patch.object(callback_module, 'host_label', return_value='host1')
    mocker.patch.object(callback_module, '_get_item_label', return_value='item1')
    mocker.patch.object(callback_module, '_clean_results')
    mocker.patch.object(callback_module, '_run_is_verbose', return_value=False)
    mocker.patch.object(callback_module, '_display')
    
    callback_module.v2_runner_item_on_ok(result)
    
    callback_module._print_task_banner.assert_not_called()
    callback_module._display.display.assert_called_once_with('ok: [host1] => (item=item1)', color=C.COLOR_OK)
