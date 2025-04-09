# file: lib/ansible/executor/playbook_executor.py:50-76
# asked: {"lines": [50, 51, 52, 53, 54, 55, 56, 58, 59, 60, 62, 63, 64, 65, 66, 67, 76], "branches": [[58, 60], [58, 62]]}
# gained: {"lines": [50, 51, 52, 53, 54, 55, 56, 58, 59, 60, 62, 63, 64, 65, 66, 67, 76], "branches": [[58, 60], [58, 62]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.executor.playbook_executor import PlaybookExecutor
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible import context

@pytest.fixture
def mock_context_cliargs():
    original_cliargs = context.CLIARGS
    context.CLIARGS = context.CLIArgs({
        'listhosts': False,
        'listtasks': False,
        'listtags': False,
        'syntax': False,
        'forks': 5
    })
    yield
    context.CLIARGS = original_cliargs

@pytest.fixture
def mock_task_queue_manager():
    with patch('ansible.executor.playbook_executor.TaskQueueManager', autospec=True) as mock_tqm:
        yield mock_tqm

@pytest.fixture
def mock_set_default_transport():
    with patch('ansible.executor.playbook_executor.set_default_transport', autospec=True) as mock_sdt:
        yield mock_sdt

def test_playbook_executor_initialization_with_tqm(mock_context_cliargs, mock_task_queue_manager, mock_set_default_transport):
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
    mock_task_queue_manager.assert_called_once_with(
        inventory=inventory,
        variable_manager=variable_manager,
        loader=loader,
        passwords=passwords,
        forks=5
    )
    mock_set_default_transport.assert_called_once()

def test_playbook_executor_initialization_without_tqm(mock_set_default_transport):
    original_cliargs = context.CLIARGS
    context.CLIARGS = context.CLIArgs({
        'listhosts': True,
        'listtasks': False,
        'listtags': False,
        'syntax': False
    })
    playbooks = ['test_playbook.yml']
    inventory = MagicMock()
    variable_manager = MagicMock()
    loader = MagicMock()
    passwords = {'conn_pass': 'password'}

    executor = PlaybookExecutor(playbooks, inventory, variable_manager, loader, passwords)

    assert executor._tqm is None
    mock_set_default_transport.assert_called_once()
    context.CLIARGS = original_cliargs
