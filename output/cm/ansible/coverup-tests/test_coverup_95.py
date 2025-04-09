# file lib/ansible/module_utils/common/network.py:86-113
# lines [86, 92, 95, 96, 97, 98, 99, 100, 101, 104, 105, 106, 107, 108, 111, 112, 113]
# branches ['96->97', '96->100', '98->96', '98->99', '100->101', '100->104', '105->106', '105->111', '106->107', '106->108', '111->112', '111->113']

import pytest
from ansible.module_utils.common.network import to_ipv6_subnet

def test_to_ipv6_subnet_full():
    # Test with a full IPv6 address without abbreviation
    assert to_ipv6_subnet('2001:0db8:85a3:0000:0000:8a2e:0370:7334') == '2001:0db8:85a3:0000::'

def test_to_ipv6_subnet_abbreviated():
    # Test with an abbreviated IPv6 address
    assert to_ipv6_subnet('2001:db8:85a3::8a2e:370:7334') == '2001:db8:85a3::'

def test_to_ipv6_subnet_less_than_four_groups():
    # Test with less than four groups before abbreviation
    assert to_ipv6_subnet('2001:db8::8a2e:370:7334') == '2001:db8::'

def test_to_ipv6_subnet_empty():
    # Test with an empty string
    assert to_ipv6_subnet('') == '::'

# Removed the invalid tests as the function does not raise ValueError
