# file: lib/ansible/plugins/callback/default.py:306-315
# asked: {"lines": [306, 307, 308, 309, 311, 312, 313, 314, 315], "branches": [[307, 0], [307, 308], [308, 309], [308, 311], [313, 314], [313, 315]]}
# gained: {"lines": [306, 307, 308, 309, 311, 312, 313, 314, 315], "branches": [[307, 0], [307, 308], [308, 309], [313, 314], [313, 315]]}

import pytest
from unittest.mock import Mock, patch, PropertyMock
from ansible.plugins.callback.default import CallbackModule
from ansible.plugins.callback import CallbackBase
from ansible import constants as C

@pytest.fixture
def callback_module():
    module = CallbackModule()
    type(module).display_skipped_hosts = PropertyMock(return_value=True)
    return module

def test_v2_runner_item_on_skipped_display_skipped_hosts(callback_module, mocker):
    # Mocking dependencies
    mocker.patch.object(callback_module, '_last_task_banner', None)
    mocker.patch.object(callback_module, '_print_task_banner')
    mocker.patch.object(callback_module, '_clean_results')
    mocker.patch.object(callback_module, '_get_item_label', return_value='item_label')
    mocker.patch.object(callback_module, '_run_is_verbose', return_value=False)
    mocker.patch.object(callback_module, '_dump_results', return_value='dumped_results')
    mocker.patch.object(callback_module, '_display')
    
    # Creating a mock result object
    result = Mock()
    result._task._uuid = 'task_uuid'
    result._task.get_name.return_value = 'task_name'
    result._host.get_name.return_value = 'host_name'
    result._result = {'_ansible_verbose_always': False, '_ansible_verbose_override': False}

    # Call the method
    callback_module.v2_runner_item_on_skipped(result)

    # Assertions
    callback_module._print_task_banner.assert_called_once_with(result._task)
    callback_module._clean_results.assert_called_once_with(result._result, result._task.action)
    callback_module._get_item_label.assert_called_once_with(result._result)
    callback_module._display.display.assert_called_once_with("skipping: [host_name] => (item=item_label) ", color=C.COLOR_SKIP)

def test_v2_runner_item_on_skipped_not_display_skipped_hosts(callback_module, mocker):
    # Mocking dependencies
    type(callback_module).display_skipped_hosts = PropertyMock(return_value=False)
    mocker.patch.object(callback_module, '_last_task_banner', None)
    mocker.patch.object(callback_module, '_print_task_banner')
    mocker.patch.object(callback_module, '_clean_results')
    mocker.patch.object(callback_module, '_get_item_label', return_value='item_label')
    mocker.patch.object(callback_module, '_run_is_verbose', return_value=False)
    mocker.patch.object(callback_module, '_dump_results', return_value='dumped_results')
    mocker.patch.object(callback_module, '_display')
    
    # Creating a mock result object
    result = Mock()
    result._task._uuid = 'task_uuid'
    result._task.get_name.return_value = 'task_name'
    result._host.get_name.return_value = 'host_name'
    result._result = {'_ansible_verbose_always': False, '_ansible_verbose_override': False}

    # Call the method
    callback_module.v2_runner_item_on_skipped(result)

    # Assertions
    callback_module._print_task_banner.assert_not_called()
    callback_module._clean_results.assert_not_called()
    callback_module._get_item_label.assert_not_called()
    callback_module._display.display.assert_not_called()

def test_v2_runner_item_on_skipped_verbose(callback_module, mocker):
    # Mocking dependencies
    mocker.patch.object(callback_module, '_last_task_banner', None)
    mocker.patch.object(callback_module, '_print_task_banner')
    mocker.patch.object(callback_module, '_clean_results')
    mocker.patch.object(callback_module, '_get_item_label', return_value='item_label')
    mocker.patch.object(callback_module, '_run_is_verbose', return_value=True)
    mocker.patch.object(callback_module, '_dump_results', return_value='dumped_results')
    mocker.patch.object(callback_module, '_display')
    
    # Creating a mock result object
    result = Mock()
    result._task._uuid = 'task_uuid'
    result._task.get_name.return_value = 'task_name'
    result._host.get_name.return_value = 'host_name'
    result._result = {'_ansible_verbose_always': False, '_ansible_verbose_override': False}

    # Call the method
    callback_module.v2_runner_item_on_skipped(result)

    # Assertions
    callback_module._print_task_banner.assert_called_once_with(result._task)
    callback_module._clean_results.assert_called_once_with(result._result, result._task.action)
    callback_module._get_item_label.assert_called_once_with(result._result)
    callback_module._display.display.assert_called_once_with("skipping: [host_name] => (item=item_label)  => dumped_results", color=C.COLOR_SKIP)
