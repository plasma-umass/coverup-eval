# file: pytutils/lazy/lazy_regex.py:36-37
# asked: {"lines": [36, 37], "branches": []}
# gained: {"lines": [36, 37], "branches": []}

import pytest
from pytutils.lazy.lazy_regex import InvalidPattern

def test_invalid_pattern_initialization():
    msg = "Invalid regex pattern"
    exc = InvalidPattern(msg)
    assert exc.msg == msg

def test_invalid_pattern_exception():
    with pytest.raises(InvalidPattern) as exc_info:
        raise InvalidPattern("This is an invalid pattern")
    assert exc_info.value.msg == "This is an invalid pattern"
