# file: lib/ansible/utils/unsafe_proxy.py:141-142
# asked: {"lines": [142], "branches": []}
# gained: {"lines": [142], "branches": []}

import pytest
from ansible.module_utils._text import to_bytes
from ansible.utils.unsafe_proxy import to_unsafe_bytes
from ansible.module_utils.six import binary_type, text_type

# Mock wrap_var to control its behavior in tests
def mock_wrap_var(v):
    return f"wrapped_{v}"

@pytest.fixture
def mock_wrap_var_fixture(monkeypatch):
    monkeypatch.setattr("ansible.utils.unsafe_proxy.wrap_var", mock_wrap_var)

def test_to_unsafe_bytes_with_text(mock_wrap_var_fixture):
    result = to_unsafe_bytes("test")
    assert result == "wrapped_b'test'"

def test_to_unsafe_bytes_with_bytes(mock_wrap_var_fixture):
    result = to_unsafe_bytes(b"test")
    assert result == "wrapped_b'test'"

def test_to_unsafe_bytes_with_nonstring(mock_wrap_var_fixture):
    class CustomObject:
        def __str__(self):
            return "custom_object"

    result = to_unsafe_bytes(CustomObject())
    assert result == "wrapped_b'custom_object'"

def test_to_unsafe_bytes_with_nonstring_empty(mock_wrap_var_fixture):
    result = to_unsafe_bytes(123, nonstring='empty')
    assert result == "wrapped_b''"

def test_to_unsafe_bytes_with_nonstring_passthru(mock_wrap_var_fixture):
    result = to_unsafe_bytes(123, nonstring='passthru')
    assert result == "wrapped_123"

def test_to_unsafe_bytes_with_nonstring_strict(mock_wrap_var_fixture):
    with pytest.raises(TypeError):
        to_unsafe_bytes(123, nonstring='strict')
