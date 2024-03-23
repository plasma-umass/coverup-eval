# file lib/ansible/module_utils/facts/network/freebsd.py:31-33
# lines [31, 32, 33]
# branches []

import pytest
from ansible.module_utils.facts.network.freebsd import FreeBSDNetworkCollector

# Test function to cover FreeBSDNetworkCollector class instantiation
def test_freebsd_network_collector_instantiation(mocker):
    # Mocking the FreeBSDNetwork class inside FreeBSDNetworkCollector
    mocker.patch('ansible.module_utils.facts.network.freebsd.FreeBSDNetworkCollector._fact_class')
    collector = FreeBSDNetworkCollector()
    assert isinstance(collector, FreeBSDNetworkCollector)
    assert collector._platform == 'FreeBSD'
