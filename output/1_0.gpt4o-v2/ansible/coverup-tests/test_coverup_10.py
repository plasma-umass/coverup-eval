# file: lib/ansible/module_utils/facts/network/dragonfly.py:31-33
# asked: {"lines": [31, 32, 33], "branches": []}
# gained: {"lines": [31, 32, 33], "branches": []}

import pytest
from ansible.module_utils.facts.network.dragonfly import DragonFlyNetworkCollector
from ansible.module_utils.facts.network.base import NetworkCollector

def test_dragonfly_network_collector_inheritance():
    collector = DragonFlyNetworkCollector()
    assert isinstance(collector, NetworkCollector)
    assert collector._fact_class.__name__ == 'DragonFlyNetwork'
    assert collector._platform == 'DragonFly'
