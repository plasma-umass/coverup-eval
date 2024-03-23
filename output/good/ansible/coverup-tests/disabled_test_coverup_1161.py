# file lib/ansible/executor/playbook_executor.py:275-319
# lines [282, 283, 287, 288, 289, 291, 292, 294, 296, 301, 302, 303, 305, 306, 307, 308, 310, 315, 316, 317, 319]
# branches ['288->289', '288->291', '294->296', '294->319', '301->302', '301->305', '306->307', '306->310', '307->306', '307->308', '316->294', '316->317']

import pytest
from ansible.executor.playbook_executor import PlaybookExecutor
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.vars.manager import VariableManager

@pytest.fixture
def mock_inventory(mocker):
    inventory = mocker.MagicMock(spec=InventoryManager)
    inventory.get_hosts.return_value = ['host1', 'host2', 'host3', 'host4']
    return inventory

@pytest.fixture
def mock_variable_manager(mocker):
    return mocker.MagicMock(spec=VariableManager)

@pytest.fixture
def mock_loader(mocker):
    return mocker.MagicMock()

@pytest.fixture
def playbook_executor(mock_inventory, mock_variable_manager, mock_loader):
    return PlaybookExecutor(playbooks=[], inventory=mock_inventory, variable_manager=mock_variable_manager, loader=mock_loader, passwords={})

def test_get_serialized_batches(playbook_executor, mock_inventory):
    play = Play()
    play.hosts = 'all'
    play.order = 'inventory'
    play.serial = [2, 1]

    batches = playbook_executor._get_serialized_batches(play)

    # Assertions to verify the postconditions
    assert len(batches) == 3
    assert batches[0] == ['host1', 'host2']
    assert batches[1] == ['host3']
    assert batches[2] == ['host4']
    # Verify that get_hosts was called with the correct parameters
    mock_inventory.get_hosts.assert_called_once_with(play.hosts, order=play.order)
