# file: lib/ansible/plugins/callback/default.py:290-304
# asked: {"lines": [], "branches": [[291, 294]]}
# gained: {"lines": [], "branches": [[291, 294]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.callback.default import CallbackModule

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_v2_runner_item_on_failed_new_task(callback_module, mocker):
    result = MagicMock()
    result._task._uuid = "new_uuid"
    result._task.action = "action"
    result._result = {"failed": True}

    callback_module._last_task_banner = "old_uuid"
    callback_module._print_task_banner = MagicMock()
    callback_module.host_label = MagicMock(return_value="host_label")
    callback_module._clean_results = MagicMock()
    callback_module._handle_exception = MagicMock()
    callback_module._handle_warnings = MagicMock()
    callback_module._display = MagicMock()
    callback_module._get_item_label = MagicMock(return_value="item_label")
    callback_module._dump_results = MagicMock(return_value="dumped_results")
    callback_module.display_failed_stderr = True

    callback_module.v2_runner_item_on_failed(result)

    callback_module._print_task_banner.assert_called_once_with(result._task)
    callback_module._clean_results.assert_called_once_with(result._result, result._task.action)
    callback_module._handle_exception.assert_called_once_with(result._result, use_stderr=True)
    callback_module._handle_warnings.assert_called_once_with(result._result)
    callback_module._display.display.assert_called_once_with(
        "failed: [host_label] (item=item_label) => dumped_results",
        color=mocker.ANY,
        stderr=True
    )

def test_v2_runner_item_on_failed_same_task(callback_module, mocker):
    result = MagicMock()
    result._task._uuid = "same_uuid"
    result._task.action = "action"
    result._result = {"failed": True}

    callback_module._last_task_banner = "same_uuid"
    callback_module._print_task_banner = MagicMock()
    callback_module.host_label = MagicMock(return_value="host_label")
    callback_module._clean_results = MagicMock()
    callback_module._handle_exception = MagicMock()
    callback_module._handle_warnings = MagicMock()
    callback_module._display = MagicMock()
    callback_module._get_item_label = MagicMock(return_value="item_label")
    callback_module._dump_results = MagicMock(return_value="dumped_results")
    callback_module.display_failed_stderr = True

    callback_module.v2_runner_item_on_failed(result)

    callback_module._print_task_banner.assert_not_called()
    callback_module._clean_results.assert_called_once_with(result._result, result._task.action)
    callback_module._handle_exception.assert_called_once_with(result._result, use_stderr=True)
    callback_module._handle_warnings.assert_called_once_with(result._result)
    callback_module._display.display.assert_called_once_with(
        "failed: [host_label] (item=item_label) => dumped_results",
        color=mocker.ANY,
        stderr=True
    )
