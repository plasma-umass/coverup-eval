# file lib/ansible/plugins/action/pause.py:88-93
# lines [88, 89, 91, 92]
# branches []

import pytest
from unittest.mock import MagicMock
from ansible.plugins.action import pause

# Test function to cover the ActionModule class
def test_action_module_initialization(mocker):
    # Mock the ActionBase class to avoid side effects and initialization errors
    mocker.patch('ansible.plugins.action.ActionBase.__init__', return_value=None)

    # Create an instance of the ActionModule with mocked arguments
    action_module = pause.ActionModule(task=MagicMock(), connection=MagicMock(), play_context=MagicMock(), loader=MagicMock(), templar=MagicMock(), shared_loader_obj=MagicMock())

    # Assertions to ensure the class attributes are set correctly
    assert action_module.BYPASS_HOST_LOOP is True
    assert action_module._VALID_ARGS == frozenset(('echo', 'minutes', 'prompt', 'seconds'))

    # No need to clean up explicitly as mocker.patch will do it automatically
