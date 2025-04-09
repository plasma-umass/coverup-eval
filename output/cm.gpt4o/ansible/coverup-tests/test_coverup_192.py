# file lib/ansible/executor/playbook_executor.py:50-76
# lines [50, 51, 52, 53, 54, 55, 56, 58, 59, 60, 62, 63, 64, 65, 66, 67, 76]
# branches ['58->60', '58->62']

import pytest
from unittest.mock import MagicMock, patch
from ansible.executor.playbook_executor import PlaybookExecutor
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible import context

@pytest.fixture
def mock_context(mocker):
    mocker.patch.object(context, 'CLIARGS', {
        'listhosts': False,
        'listtasks': False,
        'listtags': False,
        'syntax': False,
        'forks': 5
    })

@pytest.fixture
def mock_set_default_transport(mocker):
    return mocker.patch('ansible.executor.playbook_executor.set_default_transport')

@pytest.fixture
def mock_task_queue_manager(mocker):
    return mocker.patch('ansible.executor.playbook_executor.TaskQueueManager', autospec=True)

def test_playbook_executor_initialization(mock_context, mock_set_default_transport, mock_task_queue_manager):
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

def test_playbook_executor_initialization_with_cliargs(mock_context, mock_set_default_transport, mock_task_queue_manager):
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
    mock_task_queue_manager.assert_not_called()
    mock_set_default_transport.assert_called_once()
