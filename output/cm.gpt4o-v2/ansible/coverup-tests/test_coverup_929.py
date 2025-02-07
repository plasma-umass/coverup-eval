# file: lib/ansible/utils/unsafe_proxy.py:141-142
# asked: {"lines": [141, 142], "branches": []}
# gained: {"lines": [141, 142], "branches": []}

import pytest
from ansible.utils.unsafe_proxy import to_unsafe_bytes
from ansible.module_utils._text import to_bytes
from ansible.utils.unsafe_proxy import wrap_var

def test_to_unsafe_bytes():
    # Test with a simple string
    result = to_unsafe_bytes("test")
    assert result == wrap_var(to_bytes("test"))

    # Test with a byte string
    result = to_unsafe_bytes(b"test")
    assert result == wrap_var(to_bytes(b"test"))

    # Test with a non-string object
    result = to_unsafe_bytes(123)
    assert result == wrap_var(to_bytes(123))

    # Test with encoding and errors parameters
    result = to_unsafe_bytes("test", encoding="utf-8", errors="strict")
    assert result == wrap_var(to_bytes("test", encoding="utf-8", errors="strict"))

    # Test with nonstring parameter
    result = to_unsafe_bytes(123, nonstring="simplerepr")
    assert result == wrap_var(to_bytes(123, nonstring="simplerepr"))
