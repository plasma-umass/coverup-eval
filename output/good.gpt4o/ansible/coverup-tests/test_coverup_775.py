# file lib/ansible/module_utils/facts/network/hpux.py:22-30
# lines [22, 23, 29]
# branches []

import pytest
from unittest.mock import Mock
from ansible.module_utils.facts.network.hpux import HPUXNetwork

def test_hpux_network_class():
    # Mock the required 'module' argument for the Network base class
    mock_module = Mock()

    # Create an instance of the HPUXNetwork class with the mocked module
    network = HPUXNetwork(mock_module)

    # Assert that the platform attribute is correctly set
    assert network.platform == 'HP-UX'

    # Assert that the instance is of type HPUXNetwork
    assert isinstance(network, HPUXNetwork)

    # Assert that the instance is a subclass of Network
    from ansible.module_utils.facts.network.base import Network
    assert issubclass(HPUXNetwork, Network)
