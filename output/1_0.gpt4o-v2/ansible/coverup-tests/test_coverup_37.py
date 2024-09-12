# file: lib/ansible/module_utils/facts/network/dragonfly.py:23-28
# asked: {"lines": [23, 24, 28], "branches": []}
# gained: {"lines": [23, 24, 28], "branches": []}

import pytest
from unittest.mock import Mock
from ansible.module_utils.facts.network.dragonfly import DragonFlyNetwork
from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork

@pytest.fixture
def mock_module():
    return Mock()

def test_dragonfly_network_inheritance():
    # Ensure DragonFlyNetwork inherits from GenericBsdIfconfigNetwork
    assert issubclass(DragonFlyNetwork, GenericBsdIfconfigNetwork)

def test_dragonfly_network_platform(mock_module):
    # Ensure the platform attribute is set correctly
    network = DragonFlyNetwork(mock_module)
    assert network.platform == 'DragonFly'
