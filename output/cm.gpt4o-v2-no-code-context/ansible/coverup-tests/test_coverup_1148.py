# file: lib/ansible/executor/playbook_executor.py:50-76
# asked: {"lines": [51, 52, 53, 54, 55, 56, 58, 59, 60, 62, 63, 64, 65, 66, 67, 76], "branches": [[58, 60], [58, 62]]}
# gained: {"lines": [51, 52, 53, 54, 55, 56, 58, 59, 60, 62, 63, 64, 65, 66, 67, 76], "branches": [[58, 60], [58, 62]]}

import pytest
from unittest.mock import MagicMock, patch

# Mocking the context and TaskQueueManager
class MockContext:
    CLIARGS = {
        'listhosts': False,
        'listtasks': False,
        'listtags': False,
        'syntax': False,
        'forks': 5
    }

class MockTaskQueueManager:
    def __init__(self, inventory, variable_manager, loader, passwords, forks):
        self.inventory = inventory
        self.variable_manager = variable_manager
        self.loader = loader
        self.passwords = passwords
        self.forks = forks

# Mocking the set_default_transport function
def mock_set_default_transport():
    pass

# Patching the context, TaskQueueManager, and set_default_transport
@pytest.fixture(autouse=True)
def patch_dependencies(monkeypatch):
    monkeypatch.setattr('ansible.executor.playbook_executor.context', MockContext)
    monkeypatch.setattr('ansible.executor.playbook_executor.TaskQueueManager', MockTaskQueueManager)
    monkeypatch.setattr('ansible.executor.playbook_executor.set_default_transport', mock_set_default_transport)

# Importing the PlaybookExecutor after patching dependencies
from ansible.executor.playbook_executor import PlaybookExecutor

# Test function to cover the PlaybookExecutor initialization
def test_playbook_executor_initialization():
    playbooks = ['playbook1.yml']
    inventory = MagicMock()
    variable_manager = MagicMock()
    loader = MagicMock()
    passwords = {'vault_pass': 'secret'}

    executor = PlaybookExecutor(playbooks, inventory, variable_manager, loader, passwords)

    assert executor._playbooks == playbooks
    assert executor._inventory == inventory
    assert executor._variable_manager == variable_manager
    assert executor._loader == loader
    assert executor.passwords == passwords
    assert executor._unreachable_hosts == {}
    assert isinstance(executor._tqm, MockTaskQueueManager)
    assert executor._tqm.inventory == inventory
    assert executor._tqm.variable_manager == variable_manager
    assert executor._tqm.loader == loader
    assert executor._tqm.passwords == passwords
    assert executor._tqm.forks == 5

# Test function to cover the branch where CLIARGS has list options set to True
def test_playbook_executor_with_list_options():
    MockContext.CLIARGS['listhosts'] = True

    playbooks = ['playbook1.yml']
    inventory = MagicMock()
    variable_manager = MagicMock()
    loader = MagicMock()
    passwords = {'vault_pass': 'secret'}

    executor = PlaybookExecutor(playbooks, inventory, variable_manager, loader, passwords)

    assert executor._tqm is None

    # Reset the CLIARGS for other tests
    MockContext.CLIARGS['listhosts'] = False
