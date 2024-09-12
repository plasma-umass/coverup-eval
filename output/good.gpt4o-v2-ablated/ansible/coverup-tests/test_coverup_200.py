# file: lib/ansible/plugins/callback/default.py:153-159
# asked: {"lines": [153, 154, 155, 157, 158, 159], "branches": [[154, 155], [154, 157]]}
# gained: {"lines": [153, 154, 155, 157, 158, 159], "branches": [[154, 155], [154, 157]]}

import pytest
from unittest.mock import Mock, patch
from ansible.plugins.callback.default import CallbackModule
from ansible.plugins.callback import CallbackBase
from ansible.utils.display import Display
import ansible.constants as C

@pytest.fixture
def callback_module():
    module = CallbackModule()
    module._last_task_banner = None
    module._display = Mock(spec=Display)
    module.display_failed_stderr = True
    return module

@pytest.fixture
def result():
    result = Mock()
    result._task = Mock()
    result._task._uuid = "task-uuid"
    result._result = {"msg": "some error"}
    return result

def test_v2_runner_on_unreachable_new_task(callback_module, result):
    callback_module._last_task_banner = "different-uuid"
    with patch.object(callback_module, '_print_task_banner') as mock_print_task_banner, \
         patch.object(callback_module, 'host_label', return_value='host1'), \
         patch.object(callback_module, '_dump_results', return_value='{"msg": "some error"}'):
        
        callback_module.v2_runner_on_unreachable(result)
        
        mock_print_task_banner.assert_called_once_with(result._task)
        callback_module._display.display.assert_called_once_with(
            "fatal: [host1]: UNREACHABLE! => {\"msg\": \"some error\"}",
            color=C.COLOR_UNREACHABLE,
            stderr=callback_module.display_failed_stderr
        )

def test_v2_runner_on_unreachable_same_task(callback_module, result):
    callback_module._last_task_banner = "task-uuid"
    with patch.object(callback_module, '_print_task_banner') as mock_print_task_banner, \
         patch.object(callback_module, 'host_label', return_value='host1'), \
         patch.object(callback_module, '_dump_results', return_value='{"msg": "some error"}'):
        
        callback_module.v2_runner_on_unreachable(result)
        
        mock_print_task_banner.assert_not_called()
        callback_module._display.display.assert_called_once_with(
            "fatal: [host1]: UNREACHABLE! => {\"msg\": \"some error\"}",
            color=C.COLOR_UNREACHABLE,
            stderr=callback_module.display_failed_stderr
        )
