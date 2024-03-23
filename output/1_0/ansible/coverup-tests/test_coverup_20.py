# file lib/ansible/module_utils/facts/network/freebsd.py:23-28
# lines [23, 24, 28]
# branches []

import pytest
from unittest.mock import MagicMock
from ansible.module_utils.facts.network.freebsd import FreeBSDNetwork

# Since the FreeBSDNetwork class inherits from a class that requires a module
# argument, we need to mock that dependency.

def test_freebsd_network_class():
    mock_module = MagicMock()
    freebsd_network = FreeBSDNetwork(module=mock_module)
    assert freebsd_network.platform == 'FreeBSD'
