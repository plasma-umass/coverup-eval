# file lib/ansible/executor/playbook_executor.py:275-319
# lines [282, 283, 287, 288, 289, 291, 292, 294, 296, 301, 302, 303, 305, 306, 307, 308, 310, 315, 316, 317, 319]
# branches ['288->289', '288->291', '294->296', '294->319', '301->302', '301->305', '306->307', '306->310', '307->306', '307->308', '316->294', '316->317']

import pytest
from unittest.mock import MagicMock

@pytest.fixture
def playbook_executor(mock_inventory):
    from ansible.executor.playbook_executor import PlaybookExecutor
    return PlaybookExecutor(playbooks=[], inventory=mock_inventory, variable_manager=MagicMock(), loader=MagicMock(), passwords=MagicMock())

@pytest.fixture
def mock_inventory():
    return MagicMock()

@pytest.fixture
def mock_play():
    mock_play = MagicMock()
    mock_play.hosts = 'all'
    mock_play.order = 'sorted'
    return mock_play

def test_get_serialized_batches(playbook_executor, mock_inventory, mock_play):
    playbook_executor._inventory = mock_inventory

    # Test case 1: serial_batch_list is empty
    mock_play.serial = []
    mock_inventory.get_hosts.return_value = ['host1', 'host2', 'host3']
    result = playbook_executor._get_serialized_batches(mock_play)
    assert result == [['host1', 'host2', 'host3']]

    # Test case 2: serial_batch_list has one element which is -1
    mock_play.serial = [-1]
    mock_inventory.get_hosts.return_value = ['host1', 'host2', 'host3']
    result = playbook_executor._get_serialized_batches(mock_play)
    assert result == [['host1', 'host2', 'host3']]

    # Test case 3: serial_batch_list has one element which is positive
    mock_play.serial = [2]
    mock_inventory.get_hosts.return_value = ['host1', 'host2', 'host3']
    result = playbook_executor._get_serialized_batches(mock_play)
    assert result == [['host1', 'host2'], ['host3']]

    # Test case 4: serial_batch_list has multiple elements
    mock_play.serial = [1, 2]
    mock_inventory.get_hosts.return_value = ['host1', 'host2', 'host3', 'host4']
    result = playbook_executor._get_serialized_batches(mock_play)
    assert result == [['host1'], ['host2', 'host3'], ['host4']]

    # Test case 5: serial_batch_list has a zero value
    mock_play.serial = [0]
    mock_inventory.get_hosts.return_value = ['host1', 'host2', 'host3']
    result = playbook_executor._get_serialized_batches(mock_play)
    assert result == [['host1', 'host2', 'host3']]

    # Test case 6: serial_batch_list has a negative value
    mock_play.serial = [-2]
    mock_inventory.get_hosts.return_value = ['host1', 'host2', 'host3']
    result = playbook_executor._get_serialized_batches(mock_play)
    assert result == [['host1', 'host2', 'host3']]
