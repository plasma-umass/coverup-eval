# file: lib/ansible/module_utils/facts/network/sunos.py:114-116
# asked: {"lines": [114, 115, 116], "branches": []}
# gained: {"lines": [114, 115, 116], "branches": []}

import pytest
from ansible.module_utils.facts.network.sunos import SunOSNetworkCollector, SunOSNetwork

def test_sunos_network_collector_class_attributes():
    assert SunOSNetworkCollector._fact_class == SunOSNetwork
    assert SunOSNetworkCollector._platform == 'SunOS'
