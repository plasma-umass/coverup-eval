# file: lib/ansible/module_utils/facts/network/freebsd.py:23-28
# asked: {"lines": [23, 24, 28], "branches": []}
# gained: {"lines": [23, 24, 28], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.module_utils.facts.network.freebsd import FreeBSDNetwork
from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork

def test_freebsd_network_inheritance():
    # Ensure FreeBSDNetwork inherits from GenericBsdIfconfigNetwork
    assert issubclass(FreeBSDNetwork, GenericBsdIfconfigNetwork)

def test_freebsd_network_platform():
    # Mock the required 'module' argument
    mock_module = MagicMock()
    # Ensure the platform attribute is set correctly
    network = FreeBSDNetwork(mock_module)
    assert network.platform == 'FreeBSD'
