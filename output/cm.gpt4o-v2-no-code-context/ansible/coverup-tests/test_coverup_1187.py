# file: lib/ansible/plugins/callback/default.py:263-288
# asked: {"lines": [287], "branches": [[269, 272], [278, 281], [286, 287]]}
# gained: {"lines": [287], "branches": [[286, 287]]}

import pytest
from unittest.mock import Mock, patch
from ansible.plugins.callback.default import CallbackModule
from ansible.playbook.task_include import TaskInclude
from ansible.playbook.task import Task
import ansible.constants as C

@pytest.fixture
def callback_module():
    return CallbackModule()

@pytest.fixture
def mock_result():
    result = Mock()
    result._task = Mock(spec=Task)
    result._task._uuid = 'test-uuid'
    result._result = {'changed': True}
    result._host.get_name.return_value = 'test-host'
    result._task.delegate_to = None
    return result

def test_v2_runner_item_on_ok_changed(callback_module, mock_result, mocker):
    mocker.patch.object(callback_module, '_print_task_banner')
    mocker.patch.object(callback_module, '_clean_results')
    mocker.patch.object(callback_module, '_run_is_verbose', return_value=True)
    mocker.patch.object(callback_module, '_dump_results', return_value='dumped_result')
    mocker.patch.object(callback_module, '_get_item_label', return_value='item_label')
    mocker.patch.object(callback_module._display, 'display')

    callback_module._last_task_banner = 'different-uuid'
    callback_module.v2_runner_item_on_ok(mock_result)

    callback_module._print_task_banner.assert_called_once_with(mock_result._task)
    callback_module._clean_results.assert_called_once_with(mock_result._result, mock_result._task.action)
    callback_module._display.display.assert_called_once_with('changed: [test-host] => (item=item_label) => dumped_result', color=C.COLOR_CHANGED)

def test_v2_runner_item_on_ok_ok(callback_module, mock_result, mocker):
    mocker.patch.object(callback_module, '_print_task_banner')
    mocker.patch.object(callback_module, '_clean_results')
    mocker.patch.object(callback_module, '_run_is_verbose', return_value=True)
    mocker.patch.object(callback_module, '_dump_results', return_value='dumped_result')
    mocker.patch.object(callback_module, '_get_item_label', return_value='item_label')
    mocker.patch.object(callback_module._display, 'display')

    mock_result._result['changed'] = False
    callback_module.display_ok_hosts = True
    callback_module._last_task_banner = 'different-uuid'
    callback_module.v2_runner_item_on_ok(mock_result)

    callback_module._print_task_banner.assert_called_once_with(mock_result._task)
    callback_module._clean_results.assert_called_once_with(mock_result._result, mock_result._task.action)
    callback_module._display.display.assert_called_once_with('ok: [test-host] => (item=item_label) => dumped_result', color=C.COLOR_OK)

def test_v2_runner_item_on_ok_no_display_ok_hosts(callback_module, mock_result, mocker):
    mocker.patch.object(callback_module, '_print_task_banner')
    mocker.patch.object(callback_module, '_clean_results')
    mocker.patch.object(callback_module, '_run_is_verbose', return_value=True)
    mocker.patch.object(callback_module, '_dump_results', return_value='dumped_result')
    mocker.patch.object(callback_module, '_get_item_label', return_value='item_label')
    mocker.patch.object(callback_module._display, 'display')

    mock_result._result['changed'] = False
    callback_module.display_ok_hosts = False
    callback_module._last_task_banner = 'different-uuid'
    callback_module.v2_runner_item_on_ok(mock_result)

    callback_module._print_task_banner.assert_not_called()
    callback_module._clean_results.assert_not_called()
    callback_module._display.display.assert_not_called()
