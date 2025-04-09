# file: lib/ansible/executor/playbook_executor.py:50-76
# asked: {"lines": [51, 52, 53, 54, 55, 56, 58, 59, 60, 62, 63, 64, 65, 66, 67, 76], "branches": [[58, 60], [58, 62]]}
# gained: {"lines": [51, 52, 53, 54, 55, 56, 58, 59, 60, 62, 63, 64, 65, 66, 67, 76], "branches": [[58, 60], [58, 62]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.executor.playbook_executor import PlaybookExecutor
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible import context

@pytest.fixture
def mock_context():
    with patch('ansible.context.CLIARGS', new_callable=MagicMock) as mock_cliargs:
        yield mock_cliargs

@pytest.fixture
def mock_task_queue_manager():
    with patch('ansible.executor.playbook_executor.TaskQueueManager', autospec=True) as mock_tqm:
        yield mock_tqm

@pytest.fixture
def mock_set_default_transport():
    with patch('ansible.executor.playbook_executor.set_default_transport', autospec=True) as mock_sdt:
        yield mock_sdt

def test_playbook_executor_init_listhosts(mock_context, mock_task_queue_manager, mock_set_default_transport):
    mock_context.get.side_effect = lambda key: key == 'listhosts'
    executor = PlaybookExecutor(playbooks=[], inventory=None, variable_manager=None, loader=None, passwords=None)
    assert executor._tqm is None
    mock_set_default_transport.assert_called_once()

def test_playbook_executor_init_listtasks(mock_context, mock_task_queue_manager, mock_set_default_transport):
    mock_context.get.side_effect = lambda key: key == 'listtasks'
    executor = PlaybookExecutor(playbooks=[], inventory=None, variable_manager=None, loader=None, passwords=None)
    assert executor._tqm is None
    mock_set_default_transport.assert_called_once()

def test_playbook_executor_init_listtags(mock_context, mock_task_queue_manager, mock_set_default_transport):
    mock_context.get.side_effect = lambda key: key == 'listtags'
    executor = PlaybookExecutor(playbooks=[], inventory=None, variable_manager=None, loader=None, passwords=None)
    assert executor._tqm is None
    mock_set_default_transport.assert_called_once()

def test_playbook_executor_init_syntax(mock_context, mock_task_queue_manager, mock_set_default_transport):
    mock_context.get.side_effect = lambda key: key == 'syntax'
    executor = PlaybookExecutor(playbooks=[], inventory=None, variable_manager=None, loader=None, passwords=None)
    assert executor._tqm is None
    mock_set_default_transport.assert_called_once()

def test_playbook_executor_init_normal(mock_context, mock_task_queue_manager, mock_set_default_transport):
    mock_context.get.side_effect = lambda key: None
    mock_context.get.return_value = None
    executor = PlaybookExecutor(playbooks=[], inventory='inventory', variable_manager='variable_manager', loader='loader', passwords='passwords')
    assert executor._tqm is not None
    mock_task_queue_manager.assert_called_once_with(inventory='inventory', variable_manager='variable_manager', loader='loader', passwords='passwords', forks=None)
    mock_set_default_transport.assert_called_once()
