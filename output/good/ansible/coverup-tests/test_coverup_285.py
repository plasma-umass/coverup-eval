# file lib/ansible/inventory/host.py:86-100
# lines [86, 88, 89, 90, 92, 93, 95, 96, 98, 99, 100]
# branches ['95->96', '95->98', '98->99', '98->100']

import pytest
from ansible.inventory.host import Host
from unittest.mock import patch

# Assuming get_unique_id function is in the same module, otherwise adjust the import
from ansible.inventory.host import get_unique_id

@pytest.fixture
def cleanup_host():
    # Fixture to clean up any state after a test
    yield
    # No cleanup actions needed as Host instances are not stored outside of the test function

def test_host_init_with_port_and_uuid(cleanup_host):
    with patch('ansible.inventory.host.get_unique_id') as mock_get_unique_id:
        mock_get_unique_id.return_value = 'fake-uuid'
        
        # Test with port and gen_uuid set to True
        host_with_port_and_uuid = Host(name='testhost', port=22, gen_uuid=True)
        
        assert host_with_port_and_uuid.vars['ansible_port'] == 22
        assert host_with_port_and_uuid._uuid == 'fake-uuid'
        assert host_with_port_and_uuid.name == 'testhost'
        assert host_with_port_and_uuid.address == 'testhost'
        assert host_with_port_and_uuid.implicit is False

def test_host_init_without_port_and_without_uuid(cleanup_host):
    # Test with port set to None and gen_uuid set to False
    host_without_port_and_uuid = Host(name='testhost', port=None, gen_uuid=False)
    
    assert 'ansible_port' not in host_without_port_and_uuid.vars
    assert host_without_port_and_uuid._uuid is None
    assert host_without_port_and_uuid.name == 'testhost'
    assert host_without_port_and_uuid.address == 'testhost'
    assert host_without_port_and_uuid.implicit is False
