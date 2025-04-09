# file: lib/ansible/executor/playbook_executor.py:275-319
# asked: {"lines": [282, 283, 287, 288, 289, 291, 292, 294, 296, 301, 302, 303, 305, 306, 307, 308, 310, 315, 316, 317, 319], "branches": [[288, 289], [288, 291], [294, 296], [294, 319], [301, 302], [301, 305], [306, 307], [306, 310], [307, 306], [307, 308], [316, 294], [316, 317]]}
# gained: {"lines": [282, 283, 287, 288, 289, 291, 292, 294, 296, 301, 302, 303, 305, 306, 307, 308, 310, 315, 316, 317, 319], "branches": [[288, 289], [288, 291], [294, 296], [294, 319], [301, 302], [301, 305], [306, 307], [306, 310], [307, 306], [307, 308], [316, 294], [316, 317]]}

import pytest
from unittest.mock import MagicMock
from ansible.executor.playbook_executor import PlaybookExecutor
from ansible.playbook.play import Play

@pytest.fixture
def mock_inventory():
    return MagicMock()

@pytest.fixture
def playbook_executor(mock_inventory):
    mock_variable_manager = MagicMock()
    mock_loader = MagicMock()
    mock_passwords = MagicMock()
    executor = PlaybookExecutor(playbooks=[], inventory=mock_inventory, variable_manager=mock_variable_manager, loader=mock_loader, passwords=mock_passwords)
    return executor

def test_get_serialized_batches_empty_serial(playbook_executor, mock_inventory):
    play = MagicMock()
    play.hosts = ['host1', 'host2', 'host3']
    play.order = 'sorted'
    play.serial = []

    mock_inventory.get_hosts.return_value = play.hosts

    result = playbook_executor._get_serialized_batches(play)
    assert result == [['host1', 'host2', 'host3']]

def test_get_serialized_batches_single_serial(playbook_executor, mock_inventory):
    play = MagicMock()
    play.hosts = ['host1', 'host2', 'host3']
    play.order = 'sorted'
    play.serial = [2]

    mock_inventory.get_hosts.return_value = play.hosts

    result = playbook_executor._get_serialized_batches(play)
    assert result == [['host1', 'host2'], ['host3']]

def test_get_serialized_batches_multiple_serial(playbook_executor, mock_inventory):
    play = MagicMock()
    play.hosts = ['host1', 'host2', 'host3', 'host4']
    play.order = 'sorted'
    play.serial = [2, 1]

    mock_inventory.get_hosts.return_value = play.hosts

    result = playbook_executor._get_serialized_batches(play)
    assert result == [['host1', 'host2'], ['host3'], ['host4']]

def test_get_serialized_batches_percentage_serial(playbook_executor, mock_inventory):
    play = MagicMock()
    play.hosts = ['host1', 'host2', 'host3', 'host4']
    play.order = 'sorted'
    play.serial = ['50%']

    mock_inventory.get_hosts.return_value = play.hosts

    result = playbook_executor._get_serialized_batches(play)
    assert result == [['host1', 'host2'], ['host3', 'host4']]

def test_get_serialized_batches_invalid_serial(playbook_executor, mock_inventory):
    play = MagicMock()
    play.hosts = ['host1', 'host2', 'host3']
    play.order = 'sorted'
    play.serial = [-1]

    mock_inventory.get_hosts.return_value = play.hosts

    result = playbook_executor._get_serialized_batches(play)
    assert result == [['host1', 'host2', 'host3']]
