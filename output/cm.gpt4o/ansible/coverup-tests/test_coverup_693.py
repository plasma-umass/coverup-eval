# file lib/ansible/module_utils/facts/network/hurd.py:24-31
# lines [24, 25, 29, 30]
# branches []

import pytest
from ansible.module_utils.facts.network.hurd import HurdPfinetNetwork
from ansible.module_utils.facts.network.base import Network

class MockModule:
    pass

@pytest.fixture
def mock_module():
    return MockModule()

def test_hurd_pfinet_network_initialization(mock_module):
    # Test the initialization of HurdPfinetNetwork
    network = HurdPfinetNetwork(mock_module)
    assert network.platform == 'GNU'
    assert network._socket_dir == '/servers/socket/'

def test_hurd_pfinet_network_attributes(mock_module):
    # Test the attributes of HurdPfinetNetwork
    network = HurdPfinetNetwork(mock_module)
    assert hasattr(network, 'platform')
    assert hasattr(network, '_socket_dir')
