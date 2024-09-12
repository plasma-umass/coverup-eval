# file: pytutils/lazy/lazy_regex.py:92-95
# asked: {"lines": [92, 93, 94, 95], "branches": [[93, 94], [93, 95]]}
# gained: {"lines": [92, 93, 94, 95], "branches": [[93, 94], [93, 95]]}

import pytest
from pytutils.lazy.lazy_regex import InvalidPattern

def test_invalid_pattern_equality():
    # Create two instances with the same message
    pattern1 = InvalidPattern("Test message")
    pattern2 = InvalidPattern("Test message")
    
    # Create an instance with a different message
    pattern3 = InvalidPattern("Different message")
    
    # Test equality with the same message
    assert pattern1 == pattern2
    
    # Test inequality with a different message
    assert pattern1 != pattern3
    
    # Test inequality with a different class
    assert pattern1 != ValueError("Test message")
