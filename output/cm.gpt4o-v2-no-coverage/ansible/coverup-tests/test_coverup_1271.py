# file: lib/ansible/plugins/callback/default.py:153-159
# asked: {"lines": [154, 155, 157, 158, 159], "branches": [[154, 155], [154, 157]]}
# gained: {"lines": [154, 155, 157, 158, 159], "branches": [[154, 155]]}

import pytest
from unittest.mock import Mock, patch
from ansible.plugins.callback.default import CallbackModule
from ansible import constants as C

@pytest.fixture
def callback_module():
    module = CallbackModule()
    module._last_task_banner = None
    module._display = Mock()
    module.display_failed_stderr = True
    return module

def test_v2_runner_on_unreachable(callback_module):
    result = Mock()
    result._task._uuid = '1234'
    result._task.no_log = False
    result._task.args = {'arg1': 'value1'}
    result._task.check_mode = False
    result._task.get_name.return_value = 'test_task'
    result._task.delegate_to = None
    result._host.get_name.return_value = 'localhost'
    result._result = {'key': 'value'}

    with patch.object(callback_module, '_print_task_banner') as mock_print_task_banner, \
         patch.object(callback_module, 'host_label', return_value='localhost') as mock_host_label, \
         patch.object(callback_module, '_dump_results', return_value='{"key": "value"}') as mock_dump_results:
        
        callback_module.v2_runner_on_unreachable(result)
        
        mock_print_task_banner.assert_called_once_with(result._task)
        mock_host_label.assert_called_once_with(result)
        mock_dump_results.assert_called_once_with(result._result)
        callback_module._display.display.assert_called_once_with(
            'fatal: [localhost]: UNREACHABLE! => {"key": "value"}',
            color=C.COLOR_UNREACHABLE,
            stderr=callback_module.display_failed_stderr
        )
