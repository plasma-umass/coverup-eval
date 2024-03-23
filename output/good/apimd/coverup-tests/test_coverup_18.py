# file apimd/parser.py:101-106
# lines [101, 103, 104, 106]
# branches ['103->104', '103->106']

import pytest
from apimd.parser import esc_underscore

def test_esc_underscore_single_underscore():
    # Test with a single underscore, which should not be escaped
    input_str = "single_underscore"
    expected_output = "single_underscore"
    assert esc_underscore(input_str) == expected_output

def test_esc_underscore_multiple_underscores():
    # Test with multiple underscores, which should be escaped
    input_str = "multiple_underscores_here"
    expected_output = "multiple\\_underscores\\_here"
    assert esc_underscore(input_str) == expected_output

def test_esc_underscore_no_underscore():
    # Test with no underscore, which should remain unchanged
    input_str = "nounderscore"
    expected_output = "nounderscore"
    assert esc_underscore(input_str) == expected_output
