# file: lib/ansible/executor/playbook_executor.py:275-319
# asked: {"lines": [275, 282, 283, 287, 288, 289, 291, 292, 294, 296, 301, 302, 303, 305, 306, 307, 308, 310, 315, 316, 317, 319], "branches": [[288, 289], [288, 291], [294, 296], [294, 319], [301, 302], [301, 305], [306, 307], [306, 310], [307, 306], [307, 308], [316, 294], [316, 317]]}
# gained: {"lines": [275, 282, 283, 287, 288, 289, 291, 292, 294, 296, 301, 302, 303, 305, 306, 307, 308, 310, 315, 316, 317, 319], "branches": [[288, 289], [288, 291], [294, 296], [294, 319], [301, 302], [301, 305], [306, 307], [306, 310], [307, 306], [307, 308], [316, 294], [316, 317]]}

import pytest
from unittest.mock import MagicMock
from ansible.executor.playbook_executor import PlaybookExecutor
from ansible.playbook.play import Play

@pytest.fixture
def mock_inventory():
    return MagicMock()

@pytest.fixture
def playbook_executor(mock_inventory):
    variable_manager = MagicMock()
    loader = MagicMock()
    passwords = MagicMock()
    executor = PlaybookExecutor(playbooks=[], inventory=mock_inventory, variable_manager=variable_manager, loader=loader, passwords=passwords)
    return executor

def test_get_serialized_batches_empty_serial(mock_inventory, playbook_executor):
    play = MagicMock()
    play.hosts = 'all'
    play.order = 'sorted'
    play.serial = []

    mock_inventory.get_hosts.return_value = ['host1', 'host2', 'host3']

    result = playbook_executor._get_serialized_batches(play)
    assert result == [['host1', 'host2', 'host3']]

def test_get_serialized_batches_single_batch(mock_inventory, playbook_executor):
    play = MagicMock()
    play.hosts = 'all'
    play.order = 'sorted'
    play.serial = [2]

    mock_inventory.get_hosts.return_value = ['host1', 'host2', 'host3']

    result = playbook_executor._get_serialized_batches(play)
    assert result == [['host1', 'host2'], ['host3']]

def test_get_serialized_batches_multiple_batches(mock_inventory, playbook_executor):
    play = MagicMock()
    play.hosts = 'all'
    play.order = 'sorted'
    play.serial = [1, 2]

    mock_inventory.get_hosts.return_value = ['host1', 'host2', 'host3', 'host4']

    result = playbook_executor._get_serialized_batches(play)
    assert result == [['host1'], ['host2', 'host3'], ['host4']]

def test_get_serialized_batches_percentage_serial(mock_inventory, playbook_executor):
    play = MagicMock()
    play.hosts = 'all'
    play.order = 'sorted'
    play.serial = ['50%']

    mock_inventory.get_hosts.return_value = ['host1', 'host2', 'host3', 'host4']

    result = playbook_executor._get_serialized_batches(play)
    assert result == [['host1', 'host2'], ['host3', 'host4']]

def test_get_serialized_batches_zero_serial(mock_inventory, playbook_executor):
    play = MagicMock()
    play.hosts = 'all'
    play.order = 'sorted'
    play.serial = [0]

    mock_inventory.get_hosts.return_value = ['host1', 'host2', 'host3']

    result = playbook_executor._get_serialized_batches(play)
    assert result == [['host1', 'host2', 'host3']]
