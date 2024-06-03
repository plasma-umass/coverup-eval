# file pytutils/lazy/lazy_regex.py:36-37
# lines [36, 37]
# branches []

import pytest
from pytutils.lazy.lazy_regex import InvalidPattern

def test_invalid_pattern_exception():
    # Test that the InvalidPattern exception is raised correctly
    with pytest.raises(InvalidPattern) as exc_info:
        raise InvalidPattern("This is an invalid pattern")
    
    # Verify the exception message
    assert exc_info.value.msg == "This is an invalid pattern"
