# file lib/ansible/executor/playbook_executor.py:50-76
# lines [60]
# branches ['58->60']

import pytest
from unittest.mock import MagicMock
from ansible.executor.playbook_executor import PlaybookExecutor
from ansible.utils.context_objects import CLIArgs

@pytest.fixture
def mock_context_CLIARGS(mocker):
    mocker.patch.object(CLIArgs, 'get', side_effect=lambda k, default=None: {
        'listhosts': False,
        'listtasks': False,
        'listtags': False,
        'syntax': False,
        'forks': 5
    }.get(k, default))

@pytest.fixture
def playbook_executor(mock_context_CLIARGS, mocker):
    playbooks = ['test_playbook.yml']
    inventory = MagicMock()
    variable_manager = MagicMock()
    loader = MagicMock()
    passwords = {'conn_pass': 'password123'}
    mocker.patch('ansible.executor.playbook_executor.set_default_transport')
    return PlaybookExecutor(playbooks, inventory, variable_manager, loader, passwords)

def test_playbook_executor_tqm_initialization(playbook_executor):
    assert playbook_executor._tqm is not None
    assert playbook_executor._tqm._inventory == playbook_executor._inventory
    assert playbook_executor._tqm._variable_manager == playbook_executor._variable_manager
    assert playbook_executor._tqm._loader == playbook_executor._loader
    assert playbook_executor._tqm.passwords == playbook_executor.passwords

@pytest.fixture
def playbook_executor_with_listhosts(mock_context_CLIARGS, mocker):
    mocker.patch.object(CLIArgs, 'get', side_effect=lambda k, default=None: {
        'listhosts': True,
        'listtasks': False,
        'listtags': False,
        'syntax': False,
        'forks': 5
    }.get(k, default))
    playbooks = ['test_playbook.yml']
    inventory = MagicMock()
    variable_manager = MagicMock()
    loader = MagicMock()
    passwords = {'conn_pass': 'password123'}
    mocker.patch('ansible.executor.playbook_executor.set_default_transport')
    return PlaybookExecutor(playbooks, inventory, variable_manager, loader, passwords)

def test_playbook_executor_tqm_none_when_listhosts(playbook_executor_with_listhosts):
    assert playbook_executor_with_listhosts._tqm is None
