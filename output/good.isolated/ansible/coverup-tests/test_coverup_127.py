# file lib/ansible/module_utils/facts/network/generic_bsd.py:248-269
# lines [248, 249, 252, 253, 255, 256, 258, 259, 261, 262, 263, 264, 266, 267, 268, 269]
# branches ['252->253', '252->261', '258->259', '258->266', '261->262', '261->263', '263->264', '263->266', '267->268', '267->269']

import pytest
from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork

class MockModule(object):
    def __init__(self):
        self.params = {}

@pytest.fixture
def generic_bsd_ifconfig_network():
    return GenericBsdIfconfigNetwork(module=MockModule())

def test_parse_inet6_line_with_cidr_and_scope(generic_bsd_ifconfig_network):
    current_if = {'ipv6': []}
    ips = {'all_ipv6_addresses': []}
    words = ['inet6', '2001:db8::1/64', 'something', 'something', 'scopeid', '0x1']

    generic_bsd_ifconfig_network.parse_inet6_line(words, current_if, ips)

    assert current_if['ipv6'][0]['address'] == '2001:db8::1'
    assert current_if['ipv6'][0]['prefix'] == '64'
    assert current_if['ipv6'][0]['scope'] == '0x1'
    assert ips['all_ipv6_addresses'][0] == '2001:db8::1'

def test_parse_inet6_line_without_cidr_with_prefixlen_and_scopeid(generic_bsd_ifconfig_network):
    current_if = {'ipv6': []}
    ips = {'all_ipv6_addresses': []}
    words = ['inet6', '2001:db8::1', 'prefixlen', '64', 'scopeid', '0x1']

    generic_bsd_ifconfig_network.parse_inet6_line(words, current_if, ips)

    assert current_if['ipv6'][0]['address'] == '2001:db8::1'
    assert current_if['ipv6'][0]['prefix'] == '64'
    assert current_if['ipv6'][0]['scope'] == '0x1'
    assert ips['all_ipv6_addresses'][0] == '2001:db8::1'

def test_parse_inet6_line_with_localhost_address(generic_bsd_ifconfig_network):
    current_if = {'ipv6': []}
    ips = {'all_ipv6_addresses': []}
    words = ['inet6', '::1/128']

    generic_bsd_ifconfig_network.parse_inet6_line(words, current_if, ips)

    assert current_if['ipv6'][0]['address'] == '::1'
    assert current_if['ipv6'][0]['prefix'] == '128'
    assert 'scope' not in current_if['ipv6'][0]
    assert ips['all_ipv6_addresses'] == []
