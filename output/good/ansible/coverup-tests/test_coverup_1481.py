# file lib/ansible/plugins/action/reboot.py:89-91
# lines [91]
# branches []

import pytest
from unittest.mock import MagicMock
from ansible.plugins.action.reboot import ActionModule

# Mocking the ActionBase class to avoid side effects
class MockActionBase:
    def __init__(self, *args, **kwargs):
        self.DEFAULT_PRE_REBOOT_DELAY = 0

    def _check_delay(self, key, default):
        return default

# Inheriting from the mocked class instead of the real ActionBase
class MockActionModule(ActionModule, MockActionBase):
    def __init__(self, *args, **kwargs):
        MockActionBase.__init__(self, *args, **kwargs)

@pytest.fixture
def action_module(mocker):
    mocker.patch('ansible.plugins.action.ActionBase.__init__', return_value=None)
    return MockActionModule()

def test_pre_reboot_delay(action_module, mocker):
    # Mock the _check_delay method to ensure it is called with the correct parameters
    mocker.patch.object(action_module, '_check_delay', return_value=10)
    delay = action_module.pre_reboot_delay
    # Assert that the _check_delay method was called with the correct parameters
    action_module._check_delay.assert_called_once_with('pre_reboot_delay', action_module.DEFAULT_PRE_REBOOT_DELAY)
    # Assert that the returned delay is what we mocked
    assert delay == 10
