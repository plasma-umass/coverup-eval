# file: lib/ansible/plugins/callback/default.py:247-261
# asked: {"lines": [], "branches": [[250, 249], [252, 249], [253, 255], [258, 0], [259, 261]]}
# gained: {"lines": [], "branches": [[250, 249]]}

import pytest
from unittest.mock import Mock, patch
from ansible.plugins.callback.default import CallbackModule

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_v2_on_file_diff_with_loop(callback_module, mocker):
    result = Mock()
    result._task.loop = True
    result._task._uuid = "1234"
    result._result = {
        'results': [
            {'diff': 'some_diff', 'changed': True},
            {'diff': '', 'changed': False},
            {'diff': 'another_diff', 'changed': True}
        ]
    }
    
    mocker.patch.object(callback_module, '_get_diff', side_effect=lambda x: x)
    mocker.patch.object(callback_module, '_print_task_banner')
    mocker.patch.object(callback_module._display, 'display')
    
    callback_module.v2_on_file_diff(result)
    
    assert callback_module._print_task_banner.call_count == 2
    callback_module._display.display.assert_any_call('some_diff')
    callback_module._display.display.assert_any_call('another_diff')

def test_v2_on_file_diff_without_loop(callback_module, mocker):
    result = Mock()
    result._task.loop = False
    result._task._uuid = "1234"
    result._result = {
        'diff': 'some_diff',
        'changed': True
    }
    
    mocker.patch.object(callback_module, '_get_diff', side_effect=lambda x: x)
    mocker.patch.object(callback_module, '_print_task_banner')
    mocker.patch.object(callback_module._display, 'display')
    
    callback_module.v2_on_file_diff(result)
    
    callback_module._print_task_banner.assert_called_once_with(result._task)
    callback_module._display.display.assert_called_once_with('some_diff')

def test_v2_on_file_diff_no_diff(callback_module, mocker):
    result = Mock()
    result._task.loop = False
    result._task._uuid = "1234"
    result._result = {
        'diff': '',
        'changed': True
    }
    
    mocker.patch.object(callback_module, '_get_diff', return_value=None)
    mocker.patch.object(callback_module, '_print_task_banner')
    mocker.patch.object(callback_module._display, 'display')
    
    callback_module.v2_on_file_diff(result)
    
    callback_module._print_task_banner.assert_not_called()
    callback_module._display.display.assert_not_called()
