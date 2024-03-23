# file tornado/escape.py:147-167
# lines [147, 148, 159, 160, 161, 162, 164, 165, 166, 167]
# branches ['159->160', '159->161', '165->166', '165->167']

import pytest
from tornado.escape import parse_qs_bytes

def test_parse_qs_bytes_with_bytes_input():
    # Setup
    query_string = b'name=John+Doe&occupation=developer'
    
    # Exercise
    result = parse_qs_bytes(query_string)
    
    # Verify
    expected = {
        'name': [b'John Doe'],
        'occupation': [b'developer']
    }
    assert result == expected
    
    # Cleanup - nothing to clean up as the function does not modify any external state

def test_parse_qs_bytes_with_str_input():
    # Setup
    query_string = 'name=John+Doe&occupation=developer'
    
    # Exercise
    result = parse_qs_bytes(query_string)
    
    # Verify
    expected = {
        'name': [b'John Doe'],
        'occupation': [b'developer']
    }
    assert result == expected
    
    # Cleanup - nothing to clean up as the function does not modify any external state

def test_parse_qs_bytes_with_bytes_input_and_blank_values():
    # Setup
    query_string = b'name=John+Doe&occupation='
    
    # Exercise
    result = parse_qs_bytes(query_string, keep_blank_values=True)
    
    # Verify
    expected = {
        'name': [b'John Doe'],
        'occupation': [b'']
    }
    assert result == expected
    
    # Cleanup - nothing to clean up as the function does not modify any external state

def test_parse_qs_bytes_with_bytes_input_and_strict_parsing():
    # Setup
    query_string = b'name=John+Doe&occupation=developer&empty'
    
    # Exercise
    with pytest.raises(ValueError):
        parse_qs_bytes(query_string, strict_parsing=True)
    
    # Cleanup - nothing to clean up as the function does not modify any external state
