# file: lib/ansible/plugins/callback/default.py:290-304
# asked: {"lines": [290, 291, 292, 294, 295, 296, 298, 299, 300, 301, 302, 303], "branches": [[291, 292], [291, 294]]}
# gained: {"lines": [290, 291, 292, 294, 295, 296, 298, 299, 300, 301, 302, 303], "branches": [[291, 292], [291, 294]]}

import pytest
from unittest.mock import Mock, patch
from ansible.plugins.callback.default import CallbackModule

@pytest.fixture
def callback_module():
    module = CallbackModule()
    module.display_failed_stderr = True  # Ensure the attribute is set
    module.C = Mock()  # Mock the C attribute
    module.C.COLOR_ERROR = 'red'  # Set a value for COLOR_ERROR
    return module

@pytest.fixture
def result():
    mock_result = Mock()
    mock_result._task = Mock()
    mock_result._task._uuid = '1234'
    mock_result._task.action = 'test_action'
    mock_result._result = {'failed': True}
    return mock_result

def test_v2_runner_item_on_failed_new_task(callback_module, result, mocker):
    mocker.patch.object(callback_module, '_print_task_banner')
    mocker.patch.object(callback_module, 'host_label', return_value='localhost')
    mocker.patch.object(callback_module, '_clean_results')
    mocker.patch.object(callback_module, '_handle_exception')
    mocker.patch.object(callback_module, '_handle_warnings')
    mocker.patch.object(callback_module._display, 'display')
    mocker.patch.object(callback_module, '_get_item_label', return_value='item_label')
    mocker.patch.object(callback_module, '_dump_results', return_value='dumped_results')

    callback_module._last_task_banner = '5678'
    callback_module.v2_runner_item_on_failed(result)

    callback_module._print_task_banner.assert_called_once_with(result._task)
    callback_module._clean_results.assert_called_once_with(result._result, result._task.action)
    callback_module._handle_exception.assert_called_once_with(result._result, use_stderr=callback_module.display_failed_stderr)
    callback_module._handle_warnings.assert_called_once_with(result._result)
    callback_module._display.display.assert_called_once_with(
        "failed: [localhost] (item=item_label) => dumped_results",
        color=callback_module.C.COLOR_ERROR,
        stderr=callback_module.display_failed_stderr
    )

def test_v2_runner_item_on_failed_same_task(callback_module, result, mocker):
    mocker.patch.object(callback_module, '_print_task_banner')
    mocker.patch.object(callback_module, 'host_label', return_value='localhost')
    mocker.patch.object(callback_module, '_clean_results')
    mocker.patch.object(callback_module, '_handle_exception')
    mocker.patch.object(callback_module, '_handle_warnings')
    mocker.patch.object(callback_module._display, 'display')
    mocker.patch.object(callback_module, '_get_item_label', return_value='item_label')
    mocker.patch.object(callback_module, '_dump_results', return_value='dumped_results')

    callback_module._last_task_banner = '1234'
    callback_module.v2_runner_item_on_failed(result)

    callback_module._print_task_banner.assert_not_called()
    callback_module._clean_results.assert_called_once_with(result._result, result._task.action)
    callback_module._handle_exception.assert_called_once_with(result._result, use_stderr=callback_module.display_failed_stderr)
    callback_module._handle_warnings.assert_called_once_with(result._result)
    callback_module._display.display.assert_called_once_with(
        "failed: [localhost] (item=item_label) => dumped_results",
        color=callback_module.C.COLOR_ERROR,
        stderr=callback_module.display_failed_stderr
    )
