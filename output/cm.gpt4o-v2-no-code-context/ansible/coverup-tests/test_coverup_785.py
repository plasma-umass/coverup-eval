# file: lib/ansible/utils/unsafe_proxy.py:141-142
# asked: {"lines": [141, 142], "branches": []}
# gained: {"lines": [141, 142], "branches": []}

import pytest
from ansible.utils.unsafe_proxy import to_unsafe_bytes, wrap_var, to_bytes

def test_to_unsafe_bytes(monkeypatch):
    # Mock the to_bytes function to return a specific value
    def mock_to_bytes(*args, **kwargs):
        return b"mocked_bytes"

    # Mock the wrap_var function to return its input
    def mock_wrap_var(value):
        return value

    monkeypatch.setattr("ansible.utils.unsafe_proxy.to_bytes", mock_to_bytes)
    monkeypatch.setattr("ansible.utils.unsafe_proxy.wrap_var", mock_wrap_var)

    # Call the function with test arguments
    result = to_unsafe_bytes("test")

    # Assert that the result is as expected
    assert result == b"mocked_bytes"
