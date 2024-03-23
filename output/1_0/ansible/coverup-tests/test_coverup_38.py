# file lib/ansible/module_utils/facts/network/dragonfly.py:31-33
# lines [31, 32, 33]
# branches []

import pytest
from ansible.module_utils.facts.network.dragonfly import DragonFlyNetworkCollector

# Test function to improve coverage
def test_dragonfly_network_collector_initialization():
    collector = DragonFlyNetworkCollector()
    
    assert collector._platform == 'DragonFly'
    # Since we are not mocking here, we should check for the original class
    from ansible.module_utils.facts.network.dragonfly import DragonFlyNetwork
    assert collector._fact_class is DragonFlyNetwork
