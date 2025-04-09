# file pytutils/lazy/lazy_regex.py:92-95
# lines [92, 93, 94, 95]
# branches ['93->94', '93->95']

import pytest
from pytutils.lazy.lazy_regex import InvalidPattern

def test_invalid_pattern_equality():
    # Create two instances of InvalidPattern with the same attributes
    exc1 = InvalidPattern("Invalid regex pattern")
    exc2 = InvalidPattern("Invalid regex pattern")
    
    # Create an instance of InvalidPattern with different attributes
    exc3 = InvalidPattern("Different invalid regex pattern")
    
    # Test equality of instances with the same attributes
    assert exc1 == exc2
    
    # Test inequality of instances with different attributes
    assert exc1 != exc3
    
    # Test inequality with an instance of a different class
    assert exc1 != ValueError("Invalid regex pattern")
