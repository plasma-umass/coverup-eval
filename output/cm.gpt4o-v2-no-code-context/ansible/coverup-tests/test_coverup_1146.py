# file: lib/ansible/plugins/callback/default.py:136-151
# asked: {"lines": [138, 140, 142, 143, 145, 146, 148, 149, 150, 151], "branches": [[138, 0], [138, 140], [142, 143], [142, 145], [145, 146], [145, 148], [149, 150], [149, 151]]}
# gained: {"lines": [138, 140, 142, 143, 145, 146, 148, 149, 150, 151], "branches": [[138, 140], [142, 143], [145, 146], [145, 148], [149, 150], [149, 151]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.callback.default import CallbackModule

@pytest.fixture
def callback_module():
    return CallbackModule()

@pytest.fixture
def result():
    result = MagicMock()
    result._result = {}
    result._task = MagicMock()
    result._task.action = 'some_action'
    result._task._uuid = 'some_uuid'
    result._task.loop = False
    result._host.get_name.return_value = 'some_host'
    return result

def test_v2_runner_on_skipped_display_skipped_hosts(callback_module, result, mocker):
    callback_module.display_skipped_hosts = True
    callback_module._last_task_banner = 'different_uuid'
    
    mocker.patch.object(callback_module, '_clean_results')
    mocker.patch.object(callback_module, '_print_task_banner')
    mocker.patch.object(callback_module, '_run_is_verbose', return_value=False)
    mocker.patch.object(callback_module._display, 'display')
    
    callback_module.v2_runner_on_skipped(result)
    
    callback_module._clean_results.assert_called_once_with(result._result, result._task.action)
    callback_module._print_task_banner.assert_called_once_with(result._task)
    callback_module._display.display.assert_called_once_with("skipping: [some_host]", color=mocker.ANY)

def test_v2_runner_on_skipped_verbose(callback_module, result, mocker):
    callback_module.display_skipped_hosts = True
    callback_module._last_task_banner = 'different_uuid'
    
    mocker.patch.object(callback_module, '_clean_results')
    mocker.patch.object(callback_module, '_print_task_banner')
    mocker.patch.object(callback_module, '_run_is_verbose', return_value=True)
    mocker.patch.object(callback_module, '_dump_results', return_value='dumped_results')
    mocker.patch.object(callback_module._display, 'display')
    
    callback_module.v2_runner_on_skipped(result)
    
    callback_module._clean_results.assert_called_once_with(result._result, result._task.action)
    callback_module._print_task_banner.assert_called_once_with(result._task)
    callback_module._display.display.assert_called_once_with("skipping: [some_host] => dumped_results", color=mocker.ANY)

def test_v2_runner_on_skipped_with_loop(callback_module, result, mocker):
    callback_module.display_skipped_hosts = True
    callback_module._last_task_banner = 'different_uuid'
    result._task.loop = True
    result._result['results'] = []
    
    mocker.patch.object(callback_module, '_clean_results')
    mocker.patch.object(callback_module, '_print_task_banner')
    mocker.patch.object(callback_module, '_process_items')
    
    callback_module.v2_runner_on_skipped(result)
    
    callback_module._clean_results.assert_called_once_with(result._result, result._task.action)
    callback_module._print_task_banner.assert_called_once_with(result._task)
    callback_module._process_items.assert_called_once_with(result)
