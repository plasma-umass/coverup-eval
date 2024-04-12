# file pytutils/lazy/lazy_regex.py:36-37
# lines [36, 37]
# branches []

import pytest
from pytutils.lazy.lazy_regex import InvalidPattern

def test_invalid_pattern_exception():
    with pytest.raises(InvalidPattern) as exc_info:
        raise InvalidPattern("Invalid regex pattern")

    assert exc_info.value.msg == "Invalid regex pattern"
