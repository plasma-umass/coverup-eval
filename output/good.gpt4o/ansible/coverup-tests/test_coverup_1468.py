# file lib/ansible/module_utils/facts/network/generic_bsd.py:248-269
# lines []
# branches ['258->266', '261->263', '263->266']

import pytest
from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork
from ansible.module_utils.facts.network.base import Network

class MockModule:
    pass

@pytest.fixture
def network():
    module = MockModule()
    return GenericBsdIfconfigNetwork(module)

def test_parse_inet6_line(network):
    current_if = {'ipv6': []}
    ips = {'all_ipv6_addresses': []}

    # Test branch 258->266
    words = ['inet6', '2001:db8::1/64', 'prefixlen', '64', 'scopeid', '0x20']
    network.parse_inet6_line(words, current_if, ips)
    assert current_if['ipv6'][0]['address'] == '2001:db8::1'
    assert current_if['ipv6'][0]['prefix'] == '64'
    assert current_if['ipv6'][0]['scope'] == '0x20'
    assert '2001:db8::1' in ips['all_ipv6_addresses']

    # Test branch 261->263
    current_if = {'ipv6': []}
    ips = {'all_ipv6_addresses': []}
    words = ['inet6', '2001:db8::2', 'prefixlen', '64']
    network.parse_inet6_line(words, current_if, ips)
    assert current_if['ipv6'][0]['address'] == '2001:db8::2'
    assert current_if['ipv6'][0]['prefix'] == '64'
    assert 'scope' not in current_if['ipv6'][0]
    assert '2001:db8::2' in ips['all_ipv6_addresses']

    # Test branch 263->266
    current_if = {'ipv6': []}
    ips = {'all_ipv6_addresses': []}
    words = ['inet6', '2001:db8::3', 'prefixlen', '64', 'scopeid', '0x30']
    network.parse_inet6_line(words, current_if, ips)
    assert current_if['ipv6'][0]['address'] == '2001:db8::3'
    assert current_if['ipv6'][0]['prefix'] == '64'
    assert current_if['ipv6'][0]['scope'] == '0x30'
    assert '2001:db8::3' in ips['all_ipv6_addresses']
