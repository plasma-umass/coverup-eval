# file: lib/ansible/plugins/action/reboot.py:86-87
# asked: {"lines": [86, 87], "branches": []}
# gained: {"lines": [86, 87], "branches": []}

import pytest
from ansible.plugins.action.reboot import ActionModule
from ansible.plugins.action import ActionBase

class MockTask:
    pass

class MockConnection:
    pass

class MockPlayContext:
    pass

class MockLoader:
    pass

class MockTemplar:
    pass

class MockSharedLoaderObj:
    pass

@pytest.fixture
def action_module():
    task = MockTask()
    connection = MockConnection()
    play_context = MockPlayContext()
    loader = MockLoader()
    templar = MockTemplar()
    shared_loader_obj = MockSharedLoaderObj()
    return ActionModule(task, connection, play_context, loader, templar, shared_loader_obj)

def test_action_module_init(action_module):
    assert isinstance(action_module, ActionModule)
    assert isinstance(action_module, ActionBase)
    assert action_module._task is not None
    assert action_module._connection is not None
    assert action_module._play_context is not None
    assert action_module._loader is not None
    assert action_module._templar is not None
    assert action_module._shared_loader_obj is not None
