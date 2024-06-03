# file lib/ansible/plugins/action/pause.py:88-93
# lines [88, 89, 91, 92]
# branches []

import pytest
from ansible.plugins.action.pause import ActionModule

@pytest.fixture
def action_module():
    return ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

def test_action_module_initialization(action_module):
    assert action_module.BYPASS_HOST_LOOP is True
    assert action_module._VALID_ARGS == frozenset(('echo', 'minutes', 'prompt', 'seconds'))

def test_action_module_attributes(action_module):
    assert hasattr(action_module, 'BYPASS_HOST_LOOP')
    assert hasattr(action_module, '_VALID_ARGS')
    assert isinstance(action_module._VALID_ARGS, frozenset)
