# file: lib/ansible/plugins/callback/default.py:290-304
# asked: {"lines": [290, 291, 292, 294, 295, 296, 298, 299, 300, 301, 302, 303], "branches": [[291, 292], [291, 294]]}
# gained: {"lines": [290, 291, 292, 294, 295, 296, 298, 299, 300, 301, 302, 303], "branches": [[291, 292]]}

import pytest
from unittest.mock import Mock, patch
from ansible.plugins.callback.default import CallbackModule
from ansible import constants as C

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_v2_runner_item_on_failed(callback_module, mocker):
    # Mocking the result object
    result = Mock()
    result._task._uuid = '1234'
    result._task.action = 'test_action'
    result._result = {'item': 'test_item'}
    
    # Mocking methods and attributes
    callback_module._last_task_banner = '5678'
    callback_module._print_task_banner = Mock()
    callback_module.host_label = Mock(return_value='localhost')
    callback_module._clean_results = Mock()
    callback_module._handle_exception = Mock()
    callback_module._handle_warnings = Mock()
    callback_module._display = Mock()
    callback_module._get_item_label = Mock(return_value='item_label')
    callback_module._dump_results = Mock(return_value='dumped_results')
    callback_module.display_failed_stderr = True

    # Call the method
    callback_module.v2_runner_item_on_failed(result)

    # Assertions
    callback_module._print_task_banner.assert_called_once_with(result._task)
    callback_module._clean_results.assert_called_once_with(result._result, result._task.action)
    callback_module._handle_exception.assert_called_once_with(result._result, use_stderr=True)
    callback_module._handle_warnings.assert_called_once_with(result._result)
    callback_module._display.display.assert_called_once_with(
        "failed: [localhost] (item=item_label) => dumped_results",
        color=C.COLOR_ERROR,
        stderr=True
    )

    # Clean up
    mocker.stopall()
