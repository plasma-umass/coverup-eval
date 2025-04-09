# file lib/ansible/plugins/callback/default.py:290-304
# lines []
# branches ['291->294']

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.callback.default import CallbackModule

@pytest.fixture
def callback_module():
    module = CallbackModule()
    module.display_failed_stderr = True  # Mock the missing attribute
    return module

@pytest.fixture
def mock_result():
    mock_task = MagicMock()
    mock_task._uuid = "unique-task-uuid"
    mock_task.action = "some_action"
    mock_result = MagicMock()
    mock_result._task = mock_task
    mock_result._result = {}
    return mock_result

def test_v2_runner_item_on_failed_new_task(callback_module, mock_result, mocker):
    # Mock methods to avoid side effects
    mocker.patch.object(callback_module, '_print_task_banner')
    mocker.patch.object(callback_module, 'host_label', return_value='localhost')
    mocker.patch.object(callback_module, '_clean_results')
    mocker.patch.object(callback_module, '_handle_exception')
    mocker.patch.object(callback_module, '_handle_warnings')
    mocker.patch.object(callback_module._display, 'display')

    # Ensure _last_task_banner is different to trigger the branch
    callback_module._last_task_banner = "different-uuid"

    # Call the method
    callback_module.v2_runner_item_on_failed(mock_result)

    # Assertions to verify the correct branches were executed
    callback_module._print_task_banner.assert_called_once_with(mock_result._task)
    callback_module.host_label.assert_called_once_with(mock_result)
    callback_module._clean_results.assert_called_once_with(mock_result._result, mock_result._task.action)
    callback_module._handle_exception.assert_called_once_with(mock_result._result, use_stderr=callback_module.display_failed_stderr)
    callback_module._handle_warnings.assert_called_once_with(mock_result._result)
    callback_module._display.display.assert_called_once()
    assert "failed: [localhost]" in callback_module._display.display.call_args[0][0]

def test_v2_runner_item_on_failed_same_task(callback_module, mock_result, mocker):
    # Mock methods to avoid side effects
    mocker.patch.object(callback_module, '_print_task_banner')
    mocker.patch.object(callback_module, 'host_label', return_value='localhost')
    mocker.patch.object(callback_module, '_clean_results')
    mocker.patch.object(callback_module, '_handle_exception')
    mocker.patch.object(callback_module, '_handle_warnings')
    mocker.patch.object(callback_module._display, 'display')

    # Ensure _last_task_banner is the same to avoid triggering the branch
    callback_module._last_task_banner = "unique-task-uuid"

    # Call the method
    callback_module.v2_runner_item_on_failed(mock_result)

    # Assertions to verify the correct branches were executed
    callback_module._print_task_banner.assert_not_called()
    callback_module.host_label.assert_called_once_with(mock_result)
    callback_module._clean_results.assert_called_once_with(mock_result._result, mock_result._task.action)
    callback_module._handle_exception.assert_called_once_with(mock_result._result, use_stderr=callback_module.display_failed_stderr)
    callback_module._handle_warnings.assert_called_once_with(mock_result._result)
    callback_module._display.display.assert_called_once()
    assert "failed: [localhost]" in callback_module._display.display.call_args[0][0]
