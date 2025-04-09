# file lib/ansible/module_utils/facts/network/aix.py:25-31
# lines [25, 26, 30]
# branches []

import pytest
from ansible.module_utils.facts.network.aix import AIXNetwork
from unittest.mock import Mock

def test_aix_network_class():
    # Mock the required 'module' argument
    mock_module = Mock()

    # Create an instance of the AIXNetwork class with the mocked module
    aix_network = AIXNetwork(module=mock_module)

    # Assert that the platform attribute is correctly set
    assert aix_network.platform == 'AIX'

    # Assert that the instance is of type AIXNetwork
    assert isinstance(aix_network, AIXNetwork)

    # Assert that the instance is also of type GenericBsdIfconfigNetwork
    from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork
    assert isinstance(aix_network, GenericBsdIfconfigNetwork)
