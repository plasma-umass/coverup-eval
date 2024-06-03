# file lib/ansible/plugins/action/wait_for_connection.py:36-44
# lines [36, 37, 38, 40, 41, 42, 43]
# branches []

import pytest
from ansible.plugins.action.wait_for_connection import ActionModule

@pytest.fixture
def action_module():
    return ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

def test_action_module_defaults(action_module):
    assert action_module.TRANSFERS_FILES is False
    assert action_module._VALID_ARGS == frozenset(('connect_timeout', 'delay', 'sleep', 'timeout'))
    assert action_module.DEFAULT_CONNECT_TIMEOUT == 5
    assert action_module.DEFAULT_DELAY == 0
    assert action_module.DEFAULT_SLEEP == 1
    assert action_module.DEFAULT_TIMEOUT == 600
