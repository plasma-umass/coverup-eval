# file: lib/ansible/module_utils/facts/network/darwin.py:47-49
# asked: {"lines": [47, 48, 49], "branches": []}
# gained: {"lines": [47, 48, 49], "branches": []}

import pytest

def test_darwin_network_collector_inheritance():
    from ansible.module_utils.facts.network.darwin import DarwinNetworkCollector
    from ansible.module_utils.facts.network.base import NetworkCollector
    assert issubclass(DarwinNetworkCollector, NetworkCollector)

def test_darwin_network_collector_fact_class():
    from ansible.module_utils.facts.network.darwin import DarwinNetworkCollector
    assert DarwinNetworkCollector._fact_class.__name__ == 'DarwinNetwork'

def test_darwin_network_collector_platform():
    from ansible.module_utils.facts.network.darwin import DarwinNetworkCollector
    assert DarwinNetworkCollector._platform == 'Darwin'
