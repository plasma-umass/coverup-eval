# file lib/ansible/plugins/action/service.py:26-37
# lines [26, 28, 30, 31, 36]
# branches []

import pytest
from ansible.plugins.action.service import ActionModule
from ansible.plugins.loader import action_loader
from unittest.mock import MagicMock

# Define a test case for the ActionModule class to ensure coverage of UNUSED_PARAMS and BUILTIN_SVC_MGR_MODULES
def test_action_module_unused_params_and_builtin_svc_mgr(mocker):
    # Mock the necessary components for the test
    mocker.patch.object(action_loader, 'get', return_value=MagicMock())

    # Instantiate the ActionModule with a mock task and connection
    task = MagicMock()
    connection = MagicMock()
    play_context = MagicMock()
    loader = MagicMock()
    templar = MagicMock()
    shared_loader_obj = MagicMock()
    action_module = ActionModule(task, connection, play_context, loader, templar, shared_loader_obj)

    # Set the action to one of the built-in service manager names
    action_module._task.action = 'systemd'

    # Assert that the UNUSED_PARAMS and BUILTIN_SVC_MGR_MODULES are being used
    assert action_module.UNUSED_PARAMS['systemd'] == ['pattern', 'runlevel', 'sleep', 'arguments', 'args']
    assert 'systemd' in action_module.BUILTIN_SVC_MGR_MODULES

# Note: The test function should be automatically discovered and run by pytest, so no need to call it explicitly.
