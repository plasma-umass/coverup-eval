# file lib/ansible/inventory/manager.py:94-137
# lines [94, 106, 107, 109, 110, 111, 115, 116, 121, 122, 123, 124, 128, 129, 134, 137]
# branches ['106->107', '106->110', '110->111', '110->115', '115->116', '115->121']

import pytest
import itertools
from ansible.inventory.manager import split_host_pattern
from ansible.module_utils._text import to_text
from ansible.module_utils.six import string_types
import re

# Since parse_address cannot be imported, we will mock it directly in the test
# where it is used, without importing it.

@pytest.fixture
def cleanup():
    # Setup code if necessary
    yield
    # Teardown code if necessary

def test_split_host_pattern_with_colon_separated_patterns(cleanup, mocker):
    # Mocking parse_address to raise an exception to trigger the colon-separated pattern handling
    parse_address_mock = mocker.patch('ansible.inventory.manager.parse_address', side_effect=Exception)
    
    pattern = "host1: host2: host3"
    expected_patterns = ['host1', 'host2', 'host3']
    
    result = split_host_pattern(pattern)
    
    assert result == expected_patterns, "The split_host_pattern function did not correctly split colon-separated patterns"
    parse_address_mock.assert_called()

def test_split_host_pattern_with_ipv6_address(cleanup, mocker):
    # Mocking parse_address to return a tuple to simulate an IPv6 address
    parse_address_mock = mocker.patch('ansible.inventory.manager.parse_address', return_value=("::1", None))
    
    pattern = "::1"
    expected_patterns = ["::1"]
    
    result = split_host_pattern(pattern)
    
    assert result == expected_patterns, "The split_host_pattern function did not correctly handle an IPv6 address"
    parse_address_mock.assert_called()

def test_split_host_pattern_with_host_range(cleanup, mocker):
    # Mocking parse_address to return a tuple to simulate a host range
    parse_address_mock = mocker.patch('ansible.inventory.manager.parse_address', return_value=("host[1:3]", None))
    
    pattern = "host[1:3]"
    expected_patterns = ["host[1:3]"]
    
    result = split_host_pattern(pattern)
    
    assert result == expected_patterns, "The split_host_pattern function did not correctly handle a host range"
    parse_address_mock.assert_called()

def test_split_host_pattern_with_list_input(cleanup):
    patterns = ["host1,host2", "host3,host4"]
    expected_patterns = ["host1", "host2", "host3", "host4"]
    
    result = split_host_pattern(patterns)
    
    assert result == expected_patterns, "The split_host_pattern function did not correctly handle a list of patterns"

def test_split_host_pattern_with_non_string_input(cleanup):
    pattern = 123
    expected_patterns = ["123"]
    
    result = split_host_pattern(pattern)
    
    assert result == expected_patterns, "The split_host_pattern function did not correctly handle non-string input"
