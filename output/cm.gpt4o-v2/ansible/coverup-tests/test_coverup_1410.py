# file: lib/ansible/module_utils/facts/network/generic_bsd.py:248-269
# asked: {"lines": [], "branches": [[258, 266], [261, 263], [263, 266]]}
# gained: {"lines": [], "branches": [[261, 263], [263, 266]]}

import pytest
from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork
from unittest.mock import MagicMock

@pytest.fixture
def network_instance():
    module = MagicMock()
    return GenericBsdIfconfigNetwork(module)

def test_parse_inet6_line_scope(network_instance):
    words = ['inet6', '2001:db8::1/64', 'prefixlen', '64', 'scopeid', '0x20']
    current_if = {'ipv6': []}
    ips = {'all_ipv6_addresses': []}
    
    network_instance.parse_inet6_line(words, current_if, ips)
    
    assert current_if['ipv6'][0]['address'] == '2001:db8::1'
    assert current_if['ipv6'][0]['prefix'] == '64'
    assert current_if['ipv6'][0]['scope'] == '0x20'
    assert '2001:db8::1' in ips['all_ipv6_addresses']

def test_parse_inet6_line_prefixlen(network_instance):
    words = ['inet6', '2001:db8::2', 'prefixlen', '64']
    current_if = {'ipv6': []}
    ips = {'all_ipv6_addresses': []}
    
    network_instance.parse_inet6_line(words, current_if, ips)
    
    assert current_if['ipv6'][0]['address'] == '2001:db8::2'
    assert current_if['ipv6'][0]['prefix'] == '64'
    assert 'scope' not in current_if['ipv6'][0]
    assert '2001:db8::2' in ips['all_ipv6_addresses']

def test_parse_inet6_line_no_scope_no_prefixlen(network_instance):
    words = ['inet6', '2001:db8::3']
    current_if = {'ipv6': []}
    ips = {'all_ipv6_addresses': []}
    
    network_instance.parse_inet6_line(words, current_if, ips)
    
    assert current_if['ipv6'][0]['address'] == '2001:db8::3'
    assert 'prefix' not in current_if['ipv6'][0]
    assert 'scope' not in current_if['ipv6'][0]
    assert '2001:db8::3' in ips['all_ipv6_addresses']
