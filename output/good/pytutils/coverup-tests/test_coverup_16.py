# file pytutils/lazy/lazy_regex.py:92-95
# lines [92, 93, 94, 95]
# branches ['93->94', '93->95']

import pytest
from pytutils.lazy.lazy_regex import InvalidPattern

def test_invalid_pattern_equality():
    # Create two instances of InvalidPattern with the same message
    pattern1 = InvalidPattern("Invalid pattern")
    pattern2 = InvalidPattern("Invalid pattern")

    # Create a third instance with a different message
    pattern3 = InvalidPattern("Another invalid pattern")

    # Create an instance of a different class
    other_class_instance = ValueError("Invalid pattern")

    # Assert that two instances with the same message are equal
    assert pattern1 == pattern2

    # Assert that instances with different messages are not equal
    assert pattern1 != pattern3

    # Assert that an instance of InvalidPattern is not equal to an instance of a different class
    assert pattern1 != other_class_instance

    # Assert that comparing with an object of a different type returns NotImplemented
    assert (pattern1.__eq__(42)) is NotImplemented
