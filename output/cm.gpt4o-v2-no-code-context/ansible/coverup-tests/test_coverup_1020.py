# file: lib/ansible/plugins/callback/default.py:153-159
# asked: {"lines": [154, 155, 157, 158, 159], "branches": [[154, 155], [154, 157]]}
# gained: {"lines": [154, 155, 157, 158, 159], "branches": [[154, 155], [154, 157]]}

import pytest
from unittest.mock import MagicMock, patch

# Assuming CallbackBase and other dependencies are imported correctly
from ansible.plugins.callback.default import CallbackModule
import ansible.constants as C

@pytest.fixture
def callback_module():
    module = CallbackModule()
    module._last_task_banner = None
    module._display = MagicMock()
    module._dump_results = MagicMock(return_value="mocked_result")
    module.host_label = MagicMock(return_value="mocked_host")
    module._print_task_banner = MagicMock()
    module.display_failed_stderr = True
    return module

def test_v2_runner_on_unreachable_new_task(callback_module):
    result = MagicMock()
    result._task._uuid = "new_task_uuid"
    result._result = "mocked_result"
    
    callback_module.v2_runner_on_unreachable(result)
    
    callback_module._print_task_banner.assert_called_once_with(result._task)
    callback_module._display.display.assert_called_once_with(
        "fatal: [mocked_host]: UNREACHABLE! => mocked_result",
        color=C.COLOR_UNREACHABLE,
        stderr=True
    )

def test_v2_runner_on_unreachable_same_task(callback_module):
    result = MagicMock()
    result._task._uuid = "same_task_uuid"
    result._result = "mocked_result"
    
    callback_module._last_task_banner = "same_task_uuid"
    
    callback_module.v2_runner_on_unreachable(result)
    
    callback_module._print_task_banner.assert_not_called()
    callback_module._display.display.assert_called_once_with(
        "fatal: [mocked_host]: UNREACHABLE! => mocked_result",
        color=C.COLOR_UNREACHABLE,
        stderr=True
    )
