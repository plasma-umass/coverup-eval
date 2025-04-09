# file lib/ansible/plugins/action/reboot.py:93-95
# lines [93, 94, 95]
# branches []

import pytest
from ansible.plugins.action.reboot import ActionModule

@pytest.fixture
def action_module(mocker):
    mocker.patch('ansible.plugins.action.ActionBase.__init__', return_value=None)
    return ActionModule()

def test_post_reboot_delay_default(action_module, mocker):
    # Mock the _check_delay method to simply return the value it's passed
    mocker.patch.object(action_module, '_check_delay', side_effect=lambda x, y: y)
    assert action_module.post_reboot_delay == action_module.DEFAULT_POST_REBOOT_DELAY

def test_post_reboot_delay_custom(action_module, mocker):
    custom_delay = 123
    # Mock the _check_delay method to return a custom delay
    mocker.patch.object(action_module, '_check_delay', return_value=custom_delay)
    assert action_module.post_reboot_delay == custom_delay
