# file: lib/ansible/module_utils/facts/network/generic_bsd.py:248-269
# asked: {"lines": [248, 249, 252, 253, 255, 256, 258, 259, 261, 262, 263, 264, 266, 267, 268, 269], "branches": [[252, 253], [252, 261], [258, 259], [258, 266], [261, 262], [261, 263], [263, 264], [263, 266], [267, 268], [267, 269]]}
# gained: {"lines": [248, 249, 252, 253, 255, 256, 258, 259, 261, 262, 263, 264, 266, 267, 268, 269], "branches": [[252, 253], [252, 261], [258, 259], [258, 266], [261, 262], [261, 263], [263, 264], [263, 266], [267, 268], [267, 269]]}

import pytest
from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork

@pytest.fixture
def network_instance(mocker):
    mock_module = mocker.Mock()
    return GenericBsdIfconfigNetwork(mock_module)

def test_parse_inet6_line_with_cidr(network_instance):
    words = ['inet6', '2001:db8::1/64', 'prefixlen', '64', 'scopeid', '0x20']
    current_if = {'ipv6': []}
    ips = {'all_ipv6_addresses': []}
    
    network_instance.parse_inet6_line(words, current_if, ips)
    
    assert current_if['ipv6'] == [{'address': '2001:db8::1', 'prefix': '64', 'scope': '0x20'}]
    assert ips['all_ipv6_addresses'] == ['2001:db8::1']

def test_parse_inet6_line_without_cidr(network_instance):
    words = ['inet6', '2001:db8::2', 'prefixlen', '64', 'scopeid', '0x20']
    current_if = {'ipv6': []}
    ips = {'all_ipv6_addresses': []}
    
    network_instance.parse_inet6_line(words, current_if, ips)
    
    assert current_if['ipv6'] == [{'address': '2001:db8::2', 'prefix': '64', 'scope': '0x20'}]
    assert ips['all_ipv6_addresses'] == ['2001:db8::2']

def test_parse_inet6_line_localhost(network_instance):
    words = ['inet6', '::1/128', 'prefixlen', '128', 'scopeid', '0x1']
    current_if = {'ipv6': []}
    ips = {'all_ipv6_addresses': []}
    
    network_instance.parse_inet6_line(words, current_if, ips)
    
    assert current_if['ipv6'] == [{'address': '::1', 'prefix': '128', 'scope': '0x1'}]
    assert ips['all_ipv6_addresses'] == []

def test_parse_inet6_line_no_scope(network_instance):
    words = ['inet6', '2001:db8::3/64', 'prefixlen', '64']
    current_if = {'ipv6': []}
    ips = {'all_ipv6_addresses': []}
    
    network_instance.parse_inet6_line(words, current_if, ips)
    
    assert current_if['ipv6'] == [{'address': '2001:db8::3', 'prefix': '64'}]
    assert ips['all_ipv6_addresses'] == ['2001:db8::3']

def test_parse_inet6_line_no_prefixlen(network_instance):
    words = ['inet6', '2001:db8::4']
    current_if = {'ipv6': []}
    ips = {'all_ipv6_addresses': []}
    
    network_instance.parse_inet6_line(words, current_if, ips)
    
    assert current_if['ipv6'] == [{'address': '2001:db8::4'}]
    assert ips['all_ipv6_addresses'] == ['2001:db8::4']
