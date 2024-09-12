# file: lib/ansible/module_utils/facts/network/openbsd.py:40-42
# asked: {"lines": [40, 41, 42], "branches": []}
# gained: {"lines": [40, 41, 42], "branches": []}

import pytest
from ansible.module_utils.facts.network.openbsd import OpenBSDNetworkCollector
from ansible.module_utils.facts.network.base import NetworkCollector

def test_openbsd_network_collector_inheritance():
    collector = OpenBSDNetworkCollector()
    assert isinstance(collector, NetworkCollector)

def test_openbsd_network_collector_fact_class():
    collector = OpenBSDNetworkCollector()
    assert collector._fact_class.__name__ == 'OpenBSDNetwork'

def test_openbsd_network_collector_platform():
    collector = OpenBSDNetworkCollector()
    assert collector._platform == 'OpenBSD'
