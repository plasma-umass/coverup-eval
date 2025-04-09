# file: pytutils/lazy/lazy_regex.py:92-95
# asked: {"lines": [92, 93, 94, 95], "branches": [[93, 94], [93, 95]]}
# gained: {"lines": [92, 93, 94, 95], "branches": [[93, 94], [93, 95]]}

import pytest
from pytutils.lazy.lazy_regex import InvalidPattern

def test_invalid_pattern_equality():
    # Create two instances of InvalidPattern with the same message
    exc1 = InvalidPattern("Invalid regex pattern")
    exc2 = InvalidPattern("Invalid regex pattern")
    
    # Assert that they are considered equal
    assert exc1 == exc2

def test_invalid_pattern_inequality():
    # Create two instances of InvalidPattern with different messages
    exc1 = InvalidPattern("Invalid regex pattern")
    exc2 = InvalidPattern("Different invalid pattern")
    
    # Assert that they are not considered equal
    assert exc1 != exc2

def test_invalid_pattern_different_class():
    # Create an instance of InvalidPattern and a different exception
    exc1 = InvalidPattern("Invalid regex pattern")
    exc2 = ValueError("Invalid regex pattern")
    
    # Assert that they are not considered equal
    assert exc1 != exc2
