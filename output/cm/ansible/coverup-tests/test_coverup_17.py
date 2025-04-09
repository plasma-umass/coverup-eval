# file lib/ansible/plugins/action/reboot.py:405-465
# lines [405, 406, 407, 410, 411, 412, 414, 415, 417, 418, 420, 422, 424, 425, 427, 430, 431, 432, 433, 434, 435, 436, 439, 440, 441, 442, 443, 444, 446, 448, 449, 450, 451, 452, 454, 455, 456, 457, 460, 462, 463, 465]
# branches ['410->411', '410->414', '414->415', '414->417', '417->418', '417->420', '424->425', '424->427', '448->449', '448->454', '454->455', '454->460']

import pytest
from datetime import datetime, timedelta
from ansible.plugins.action.reboot import ActionModule
from ansible.utils.display import Display
from ansible.module_utils._text import to_text
from unittest.mock import MagicMock

# Mock the Display class to prevent actual output during tests
@pytest.fixture
def mock_display(mocker):
    return mocker.patch.object(Display, 'debug'), mocker.patch.object(Display, 'vvv')

# Mock the time.sleep to prevent actual delay during tests
@pytest.fixture
def mock_sleep(mocker):
    return mocker.patch('time.sleep', return_value=None)

# Mock the ActionModule methods that are not under test
@pytest.fixture
def mock_action_module(mocker):
    mocker.patch.object(ActionModule, 'deprecated_args')
    mocker.patch.object(ActionModule, 'get_distribution', return_value='test_distribution')
    mocker.patch.object(ActionModule, 'get_system_boot_time', return_value=datetime.utcnow() - timedelta(seconds=600))
    mocker.patch.object(ActionModule, 'perform_reboot', return_value={'failed': False, 'start': datetime.utcnow()})
    mocker.patch.object(ActionModule, 'validate_reboot', return_value={'changed': True, 'rebooted': True})

# Test function to cover the missing lines/branches
def test_action_module_run_local_connection(mock_action_module, mock_display, mock_sleep, mocker):
    action_module = ActionModule(None, None, None, None, None, None)
    action_module._connection = MagicMock()
    action_module._connection.transport = 'local'
    action_module._task = MagicMock()
    action_module._task.action = 'reboot'
    action_module._play_context = MagicMock()
    action_module._play_context.check_mode = False

    result = action_module.run()

    assert result['changed'] == False
    assert result['elapsed'] == 0
    assert result['rebooted'] == False
    assert result['failed'] == True
    assert 'Running reboot with local connection would reboot the control node.' in result['msg']
