# file: pytutils/lazy/lazy_regex.py:92-95
# asked: {"lines": [92, 93, 94, 95], "branches": [[93, 94], [93, 95]]}
# gained: {"lines": [92, 93, 94, 95], "branches": [[93, 94], [93, 95]]}

import pytest
from pytutils.lazy.lazy_regex import InvalidPattern

def test_invalid_pattern_equality():
    # Create two instances of InvalidPattern with the same message
    pattern1 = InvalidPattern("Test message")
    pattern2 = InvalidPattern("Test message")
    
    # Create another instance with a different message
    pattern3 = InvalidPattern("Different message")
    
    # Assert that two instances with the same message are equal
    assert pattern1 == pattern2
    
    # Assert that instances with different messages are not equal
    assert pattern1 != pattern3
    
    # Assert that an instance is not equal to an object of a different class
    assert pattern1 != "Test message"
