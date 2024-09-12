# file: lib/ansible/executor/playbook_executor.py:50-76
# asked: {"lines": [50, 51, 52, 53, 54, 55, 56, 58, 59, 60, 62, 63, 64, 65, 66, 67, 76], "branches": [[58, 60], [58, 62]]}
# gained: {"lines": [50, 51, 52, 53, 54, 55, 56, 58, 59, 60, 62, 63, 64, 65, 66, 67, 76], "branches": [[58, 60], [58, 62]]}

import pytest
from unittest.mock import MagicMock, patch

# Mocking the necessary imports from ansible
context = MagicMock()
context.CLIARGS = {
    'listhosts': False,
    'listtasks': False,
    'listtags': False,
    'syntax': False,
    'forks': 5
}

TaskQueueManager = MagicMock()
set_default_transport = MagicMock()

# Import the PlaybookExecutor class
from ansible.executor.playbook_executor import PlaybookExecutor

@pytest.fixture
def mock_context(mocker):
    mocker.patch('ansible.executor.playbook_executor.context', context)
    mocker.patch('ansible.executor.playbook_executor.TaskQueueManager', TaskQueueManager)
    mocker.patch('ansible.executor.playbook_executor.set_default_transport', set_default_transport)

def test_playbook_executor_initialization_with_tqm(mock_context):
    playbooks = ['test_playbook.yml']
    inventory = MagicMock()
    variable_manager = MagicMock()
    loader = MagicMock()
    passwords = {'conn_pass': 'password'}

    executor = PlaybookExecutor(playbooks, inventory, variable_manager, loader, passwords)

    assert executor._playbooks == playbooks
    assert executor._inventory == inventory
    assert executor._variable_manager == variable_manager
    assert executor._loader == loader
    assert executor.passwords == passwords
    assert executor._unreachable_hosts == {}
    assert executor._tqm is not None
    TaskQueueManager.assert_called_once_with(
        inventory=inventory,
        variable_manager=variable_manager,
        loader=loader,
        passwords=passwords,
        forks=5
    )
    set_default_transport.assert_called_once()

def test_playbook_executor_initialization_without_tqm(mock_context):
    context.CLIARGS['listhosts'] = True

    playbooks = ['test_playbook.yml']
    inventory = MagicMock()
    variable_manager = MagicMock()
    loader = MagicMock()
    passwords = {'conn_pass': 'password'}

    executor = PlaybookExecutor(playbooks, inventory, variable_manager, loader, passwords)

    assert executor._playbooks == playbooks
    assert executor._inventory == inventory
    assert executor._variable_manager == variable_manager
    assert executor._loader == loader
    assert executor.passwords == passwords
    assert executor._unreachable_hosts == {}
    assert executor._tqm is None
    set_default_transport.assert_called_once()

    context.CLIARGS['listhosts'] = False  # Reset state

def test_playbook_executor_initialization_with_other_cliargs(mock_context):
    context.CLIARGS['listtasks'] = True

    playbooks = ['test_playbook.yml']
    inventory = MagicMock()
    variable_manager = MagicMock()
    loader = MagicMock()
    passwords = {'conn_pass': 'password'}

    executor = PlaybookExecutor(playbooks, inventory, variable_manager, loader, passwords)

    assert executor._playbooks == playbooks
    assert executor._inventory == inventory
    assert executor._variable_manager == variable_manager
    assert executor._loader == loader
    assert executor.passwords == passwords
    assert executor._unreachable_hosts == {}
    assert executor._tqm is None
    set_default_transport.assert_called_once()

    context.CLIARGS['listtasks'] = False  # Reset state
