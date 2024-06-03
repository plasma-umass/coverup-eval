# file lib/ansible/plugins/callback/default.py:153-159
# lines [154, 155, 157, 158, 159]
# branches ['154->155', '154->157']

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.callback.default import CallbackModule
import ansible.constants as C

@pytest.fixture
def callback_module():
    module = CallbackModule()
    module._last_task_banner = None
    module._print_task_banner = MagicMock()
    module.host_label = MagicMock(return_value='test_host')
    module._dump_results = MagicMock(return_value='test_result')
    module._display = MagicMock()
    module._display.display = MagicMock()
    module.display_failed_stderr = True
    return module

def test_v2_runner_on_unreachable(callback_module):
    result = MagicMock()
    result._task._uuid = 'unique_task_id'
    result._result = 'some_result'

    callback_module.v2_runner_on_unreachable(result)

    callback_module._print_task_banner.assert_called_once_with(result._task)
    callback_module.host_label.assert_called_once_with(result)
    callback_module._dump_results.assert_called_once_with(result._result)
    callback_module._display.display.assert_called_once_with(
        "fatal: [test_host]: UNREACHABLE! => test_result",
        color=C.COLOR_UNREACHABLE,
        stderr=True
    )
