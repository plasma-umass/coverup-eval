# file: lib/ansible/plugins/callback/default.py:263-288
# asked: {"lines": [265, 266, 267, 268, 269, 270, 272, 273, 275, 276, 278, 279, 281, 282, 284, 285, 286, 287, 288], "branches": [[266, 267], [266, 268], [268, 269], [268, 275], [269, 270], [269, 272], [275, 276], [275, 278], [278, 279], [278, 281], [286, 287], [286, 288]]}
# gained: {"lines": [265, 266, 267, 268, 269, 270, 272, 273, 275, 276, 278, 279, 281, 282, 284, 285, 286, 288], "branches": [[266, 267], [266, 268], [268, 269], [268, 275], [269, 270], [275, 276], [275, 278], [278, 279], [286, 288]]}

import pytest
from unittest.mock import Mock, patch
from ansible.plugins.callback.default import CallbackModule
from ansible.playbook.task_include import TaskInclude
from ansible import constants as C

@pytest.fixture
def callback_module():
    return CallbackModule()

@pytest.fixture
def result():
    mock_result = Mock()
    mock_result._task = Mock()
    mock_result._task._uuid = '1234'
    mock_result._result = {'changed': True}
    return mock_result

def test_v2_runner_item_on_ok_changed(callback_module, result, mocker):
    mocker.patch.object(callback_module, 'host_label', return_value='host1')
    mocker.patch.object(callback_module, '_print_task_banner')
    mocker.patch.object(callback_module, '_clean_results')
    mocker.patch.object(callback_module, '_run_is_verbose', return_value=False)
    mocker.patch.object(callback_module._display, 'display')

    callback_module._last_task_banner = '5678'
    callback_module.v2_runner_item_on_ok(result)

    callback_module._print_task_banner.assert_called_once_with(result._task)
    callback_module._clean_results.assert_called_once_with(result._result, result._task.action)
    callback_module._display.display.assert_called_once_with('changed: [host1] => (item=None)', color=C.COLOR_CHANGED)

def test_v2_runner_item_on_ok_not_changed_display_ok_hosts(callback_module, result, mocker):
    mocker.patch.object(callback_module, 'host_label', return_value='host1')
    mocker.patch.object(callback_module, '_print_task_banner')
    mocker.patch.object(callback_module, '_clean_results')
    mocker.patch.object(callback_module, '_run_is_verbose', return_value=False)
    mocker.patch.object(callback_module._display, 'display')

    result._result['changed'] = False
    callback_module.display_ok_hosts = True
    callback_module._last_task_banner = '5678'
    callback_module.v2_runner_item_on_ok(result)

    callback_module._print_task_banner.assert_called_once_with(result._task)
    callback_module._clean_results.assert_called_once_with(result._result, result._task.action)
    callback_module._display.display.assert_called_once_with('ok: [host1] => (item=None)', color=C.COLOR_OK)

def test_v2_runner_item_on_ok_not_changed_no_display_ok_hosts(callback_module, result, mocker):
    mocker.patch.object(callback_module, 'host_label', return_value='host1')
    mocker.patch.object(callback_module, '_print_task_banner')
    mocker.patch.object(callback_module, '_clean_results')
    mocker.patch.object(callback_module, '_run_is_verbose', return_value=False)
    mocker.patch.object(callback_module._display, 'display')

    result._result['changed'] = False
    callback_module.display_ok_hosts = False
    callback_module._last_task_banner = '5678'
    callback_module.v2_runner_item_on_ok(result)

    callback_module._print_task_banner.assert_not_called()
    callback_module._clean_results.assert_not_called()
    callback_module._display.display.assert_not_called()

def test_v2_runner_item_on_ok_task_include(callback_module, result, mocker):
    mocker.patch.object(callback_module, 'host_label', return_value='host1')
    mocker.patch.object(callback_module, '_print_task_banner')
    mocker.patch.object(callback_module, '_clean_results')
    mocker.patch.object(callback_module, '_run_is_verbose', return_value=False)
    mocker.patch.object(callback_module._display, 'display')

    result._task = TaskInclude()
    callback_module.v2_runner_item_on_ok(result)

    callback_module._print_task_banner.assert_not_called()
    callback_module._clean_results.assert_not_called()
    callback_module._display.display.assert_not_called()
