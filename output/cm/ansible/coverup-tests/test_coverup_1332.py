# file lib/ansible/plugins/action/reboot.py:97-102
# lines [99, 100, 101, 102]
# branches ['100->101', '100->102']

import pytest
from unittest.mock import MagicMock, create_autospec
from ansible.plugins.action import ActionBase
from ansible.plugins.action.reboot import ActionModule

@pytest.fixture
def action_module(mocker):
    mocker.patch('ansible.plugins.action.ActionBase.__init__', return_value=None)
    action_module = ActionModule()
    action_module._task = MagicMock()
    return action_module

def test_check_delay_negative_value(action_module):
    action_module._task.args = {"delay": "-10", "delay_sec": "5"}
    assert action_module._check_delay("delay", 1) == 0
