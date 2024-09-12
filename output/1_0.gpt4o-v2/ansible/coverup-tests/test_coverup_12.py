# file: lib/ansible/utils/unicode.py:28-33
# asked: {"lines": [28, 33], "branches": []}
# gained: {"lines": [28, 33], "branches": []}

import pytest
from ansible.utils.unicode import unicode_wrap

def test_unicode_wrap_with_string():
    def sample_func():
        return b"test string"

    result = unicode_wrap(sample_func)
    assert result == "test string"
    assert isinstance(result, str)

def test_unicode_wrap_with_nonstring():
    def sample_func():
        return 12345

    result = unicode_wrap(sample_func)
    assert result == 12345
    assert isinstance(result, int)

def test_unicode_wrap_with_empty_string():
    def sample_func():
        return b""

    result = unicode_wrap(sample_func)
    assert result == ""
    assert isinstance(result, str)
