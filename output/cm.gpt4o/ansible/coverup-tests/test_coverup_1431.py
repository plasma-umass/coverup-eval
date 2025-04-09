# file lib/ansible/plugins/callback/default.py:247-261
# lines []
# branches ['250->249', '252->249', '253->255', '256->exit', '258->exit', '259->261']

import pytest
from unittest.mock import Mock
from ansible.plugins.callback.default import CallbackModule

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_v2_on_file_diff_with_loop_and_results_no_diff(callback_module):
    result = Mock()
    result._task.loop = True
    result._task._uuid = '1234'
    result._result = {
        'results': [
            {'diff': None, 'changed': True}
        ]
    }
    callback_module._last_task_banner = '5678'
    callback_module._get_diff = Mock(return_value=None)
    callback_module._print_task_banner = Mock()
    callback_module._display = Mock()
    
    callback_module.v2_on_file_diff(result)
    
    callback_module._print_task_banner.assert_not_called()
    callback_module._display.display.assert_not_called()

def test_v2_on_file_diff_with_loop_and_results_no_changed(callback_module):
    result = Mock()
    result._task.loop = True
    result._task._uuid = '1234'
    result._result = {
        'results': [
            {'diff': 'some_diff', 'changed': False}
        ]
    }
    callback_module._last_task_banner = '5678'
    callback_module._get_diff = Mock(return_value='formatted_diff')
    callback_module._print_task_banner = Mock()
    callback_module._display = Mock()
    
    callback_module.v2_on_file_diff(result)
    
    callback_module._print_task_banner.assert_not_called()
    callback_module._display.display.assert_not_called()

def test_v2_on_file_diff_with_diff_no_diff(callback_module):
    result = Mock()
    result._task.loop = False
    result._task._uuid = '1234'
    result._result = {
        'diff': None,
        'changed': True
    }
    callback_module._last_task_banner = '5678'
    callback_module._get_diff = Mock(return_value=None)
    callback_module._print_task_banner = Mock()
    callback_module._display = Mock()
    
    callback_module.v2_on_file_diff(result)
    
    callback_module._print_task_banner.assert_not_called()
    callback_module._display.display.assert_not_called()

def test_v2_on_file_diff_with_diff_no_changed(callback_module):
    result = Mock()
    result._task.loop = False
    result._task._uuid = '1234'
    result._result = {
        'diff': 'some_diff',
        'changed': False
    }
    callback_module._last_task_banner = '5678'
    callback_module._get_diff = Mock(return_value='formatted_diff')
    callback_module._print_task_banner = Mock()
    callback_module._display = Mock()
    
    callback_module.v2_on_file_diff(result)
    
    callback_module._print_task_banner.assert_not_called()
    callback_module._display.display.assert_not_called()
