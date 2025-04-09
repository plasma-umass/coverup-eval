# file: pytutils/lazy/lazy_regex.py:92-95
# asked: {"lines": [92, 93, 94, 95], "branches": [[93, 94], [93, 95]]}
# gained: {"lines": [92, 93, 94, 95], "branches": [[93, 94], [93, 95]]}

import pytest
from pytutils.lazy.lazy_regex import InvalidPattern

def test_invalid_pattern_equality():
    pattern1 = InvalidPattern("Invalid regex pattern")
    pattern2 = InvalidPattern("Invalid regex pattern")
    pattern3 = InvalidPattern("Different invalid pattern")
    pattern4 = ValueError("Invalid regex pattern")

    # Test equality with same class and same message
    assert pattern1 == pattern2

    # Test inequality with same class but different message
    assert pattern1 != pattern3

    # Test inequality with different class
    assert pattern1 != pattern4

def test_invalid_pattern_not_implemented():
    pattern1 = InvalidPattern("Invalid regex pattern")
    assert pattern1.__eq__(42) == NotImplemented
