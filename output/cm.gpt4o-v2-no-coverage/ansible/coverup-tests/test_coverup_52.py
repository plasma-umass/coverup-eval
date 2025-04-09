# file: lib/ansible/plugins/callback/default.py:101-134
# asked: {"lines": [101, 103, 105, 106, 107, 108, 109, 110, 111, 113, 114, 116, 117, 119, 120, 122, 123, 125, 127, 128, 130, 132, 133, 134], "branches": [[105, 106], [105, 109], [106, 107], [106, 108], [109, 110], [109, 116], [110, 111], [110, 113], [116, 117], [116, 119], [119, 120], [119, 122], [127, 128], [127, 130], [132, 133], [132, 134]]}
# gained: {"lines": [101, 103, 105, 106, 107, 108, 109, 110, 111, 113, 114, 116, 119, 120, 122, 123, 125, 127, 128, 130, 132, 133, 134], "branches": [[105, 106], [105, 109], [106, 107], [109, 110], [109, 116], [110, 111], [116, 119], [119, 120], [127, 128], [127, 130], [132, 133], [132, 134]]}

import pytest
from unittest.mock import Mock, patch
from ansible.plugins.callback.default import CallbackModule
from ansible.playbook.task_include import TaskInclude
from ansible import constants as C

@pytest.fixture
def callback_module():
    module = CallbackModule()
    module.display_ok_hosts = True  # Ensure this attribute is set
    return module

def test_v2_runner_on_ok_task_include(callback_module, mocker):
    result = Mock()
    result._task = Mock(spec=TaskInclude)
    result._task._uuid = "uuid1"
    result._result = {}
    callback_module._last_task_banner = "uuid2"
    
    mocker.patch.object(callback_module, '_print_task_banner')
    
    callback_module.v2_runner_on_ok(result)
    
    callback_module._print_task_banner.assert_called_once_with(result._task)

def test_v2_runner_on_ok_changed(callback_module, mocker):
    result = Mock()
    result._task = Mock()
    result._task._uuid = "uuid1"
    result._result = {'changed': True}
    callback_module._last_task_banner = "uuid2"
    
    mocker.patch.object(callback_module, '_print_task_banner')
    mocker.patch.object(callback_module, '_handle_warnings')
    mocker.patch.object(callback_module, '_clean_results')
    mocker.patch.object(callback_module, '_run_is_verbose', return_value=False)
    mocker.patch.object(callback_module, 'host_label', return_value="host1")
    mocker.patch.object(callback_module._display, 'display')
    
    callback_module.v2_runner_on_ok(result)
    
    callback_module._print_task_banner.assert_called_once_with(result._task)
    callback_module._handle_warnings.assert_called_once_with(result._result)
    callback_module._clean_results.assert_called_once_with(result._result, result._task.action)
    callback_module._display.display.assert_called_once_with("changed: [host1]", color=C.COLOR_CHANGED)

def test_v2_runner_on_ok_ok(callback_module, mocker):
    result = Mock()
    result._task = Mock()
    result._task._uuid = "uuid1"
    result._result = {'changed': False}
    callback_module._last_task_banner = "uuid2"
    callback_module.display_ok_hosts = True
    
    mocker.patch.object(callback_module, '_print_task_banner')
    mocker.patch.object(callback_module, '_handle_warnings')
    mocker.patch.object(callback_module, '_clean_results')
    mocker.patch.object(callback_module, '_run_is_verbose', return_value=False)
    mocker.patch.object(callback_module, 'host_label', return_value="host1")
    mocker.patch.object(callback_module._display, 'display')
    
    callback_module.v2_runner_on_ok(result)
    
    callback_module._print_task_banner.assert_called_once_with(result._task)
    callback_module._handle_warnings.assert_called_once_with(result._result)
    callback_module._clean_results.assert_called_once_with(result._result, result._task.action)
    callback_module._display.display.assert_called_once_with("ok: [host1]", color=C.COLOR_OK)

def test_v2_runner_on_ok_loop(callback_module, mocker):
    result = Mock()
    result._task = Mock()
    result._task._uuid = "uuid1"
    result._task.loop = True
    result._result = {'results': []}
    callback_module._last_task_banner = "uuid2"
    
    mocker.patch.object(callback_module, '_print_task_banner')
    mocker.patch.object(callback_module, '_handle_warnings')
    mocker.patch.object(callback_module, '_process_items')
    mocker.patch.object(callback_module, 'host_label', return_value="host1")
    
    callback_module.v2_runner_on_ok(result)
    
    callback_module._print_task_banner.assert_called_once_with(result._task)
    callback_module._handle_warnings.assert_called_once_with(result._result)
    callback_module._process_items.assert_called_once_with(result)

def test_v2_runner_on_ok_verbose(callback_module, mocker):
    result = Mock()
    result._task = Mock()
    result._task._uuid = "uuid1"
    result._result = {'changed': True}
    callback_module._last_task_banner = "uuid2"
    
    mocker.patch.object(callback_module, '_print_task_banner')
    mocker.patch.object(callback_module, '_handle_warnings')
    mocker.patch.object(callback_module, '_clean_results')
    mocker.patch.object(callback_module, '_run_is_verbose', return_value=True)
    mocker.patch.object(callback_module, '_dump_results', return_value="dumped_results")
    mocker.patch.object(callback_module, 'host_label', return_value="host1")
    mocker.patch.object(callback_module._display, 'display')
    
    callback_module.v2_runner_on_ok(result)
    
    callback_module._print_task_banner.assert_called_once_with(result._task)
    callback_module._handle_warnings.assert_called_once_with(result._result)
    callback_module._clean_results.assert_called_once_with(result._result, result._task.action)
    callback_module._display.display.assert_called_once_with("changed: [host1] => dumped_results", color=C.COLOR_CHANGED)
