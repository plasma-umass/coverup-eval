# file lib/ansible/module_utils/facts/network/openbsd.py:40-42
# lines [40, 41, 42]
# branches []

import pytest
from ansible.module_utils.facts.network.openbsd import OpenBSDNetworkCollector

# Since the class is very simple and doesn't have any methods to test directly,
# we'll create a test that simply instantiates the class and checks its attributes.

def test_openbsd_network_collector_instantiation():
    collector = OpenBSDNetworkCollector()
    assert collector._fact_class.__name__ == "OpenBSDNetwork"
    assert collector._platform == "OpenBSD"
