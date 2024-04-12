# file lib/ansible/inventory/manager.py:605-615
# lines [605, 611, 612, 613, 614, 615]
# branches ['611->612', '611->613', '613->614', '613->615']

import pytest
from ansible.inventory.manager import InventoryManager
from ansible.inventory.host import Host

# Mocking the to_text function to ensure it is called with the correct arguments
@pytest.fixture
def mock_to_text(mocker):
    return mocker.patch('ansible.inventory.manager.to_text', side_effect=lambda x: str(x))

# Test function to cover the branches in restrict_to_hosts
def test_restrict_to_hosts(mock_to_text):
    # Create an instance of InventoryManager
    inventory_manager = InventoryManager(loader=None, sources='localhost,')

    # Test with None restriction
    inventory_manager.restrict_to_hosts(None)
    assert inventory_manager._restriction is None

    # Test with a single host restriction
    host1 = Host(name='host1')
    inventory_manager.restrict_to_hosts(host1)
    assert inventory_manager._restriction == set(['host1'])
    # Check that to_text was called with 'host1' at least once
    mock_to_text.assert_any_call(host1.name)

    # Reset mock call count
    mock_to_text.reset_mock()

    # Test with a list of hosts restriction
    host2 = Host(name='host2')
    inventory_manager.restrict_to_hosts([host1, host2])
    assert inventory_manager._restriction == set(['host1', 'host2'])
    # Check that to_text was called twice, once for each host
    assert mock_to_text.call_count == 2
    mock_to_text.assert_any_call(host1.name)
    mock_to_text.assert_any_call(host2.name)

    # Clean up after the test
    del inventory_manager._restriction
