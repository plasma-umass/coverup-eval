# file lib/ansible/plugins/callback/default.py:247-261
# lines [248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261]
# branches ['248->249', '248->256', '249->exit', '249->250', '250->249', '250->251', '252->249', '252->253', '253->254', '253->255', '256->exit', '256->257', '258->exit', '258->259', '259->260', '259->261']

import pytest
from unittest.mock import Mock, MagicMock
from ansible.plugins.callback.default import CallbackModule

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_v2_on_file_diff_with_loop(callback_module, mocker):
    # Mocking the result object
    result = Mock()
    result._task.loop = True
    result._task._uuid = 'unique-task-id'
    result._result = {
        'results': [
            {'diff': 'some-diff', 'changed': True}
        ]
    }

    # Mocking methods in CallbackModule
    mocker.patch.object(callback_module, '_get_diff', return_value='formatted-diff')
    mocker.patch.object(callback_module, '_print_task_banner')
    mocker.patch.object(callback_module._display, 'display')

    callback_module.v2_on_file_diff(result)

    callback_module._print_task_banner.assert_called_once_with(result._task)
    callback_module._display.display.assert_called_once_with('formatted-diff')

def test_v2_on_file_diff_without_loop(callback_module, mocker):
    # Mocking the result object
    result = Mock()
    result._task.loop = False
    result._task._uuid = 'unique-task-id'
    result._result = {
        'diff': 'some-diff',
        'changed': True
    }

    # Mocking methods in CallbackModule
    mocker.patch.object(callback_module, '_get_diff', return_value='formatted-diff')
    mocker.patch.object(callback_module, '_print_task_banner')
    mocker.patch.object(callback_module._display, 'display')

    callback_module.v2_on_file_diff(result)

    callback_module._print_task_banner.assert_called_once_with(result._task)
    callback_module._display.display.assert_called_once_with('formatted-diff')
