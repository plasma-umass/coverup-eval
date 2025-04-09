# file: lib/ansible/utils/unsafe_proxy.py:117-118
# asked: {"lines": [117, 118], "branches": []}
# gained: {"lines": [117, 118], "branches": []}

import pytest
from ansible.utils.unsafe_proxy import _wrap_set, wrap_var

class MockAnsibleUnsafe:
    pass

class MockNativeJinjaText:
    def __init__(self, value):
        self.value = value

class MockAnsibleUnsafeText:
    def __init__(self, value):
        self.value = value

class MockAnsibleUnsafeBytes:
    def __init__(self, value):
        self.value = value

@pytest.fixture
def mock_wrap_var(monkeypatch):
    def mock_wrap_var(v):
        if isinstance(v, MockAnsibleUnsafe):
            return v
        if isinstance(v, MockNativeJinjaText):
            return MockAnsibleUnsafeText(v.value)
        if isinstance(v, bytes):
            return MockAnsibleUnsafeBytes(v)
        if isinstance(v, str):
            return MockAnsibleUnsafeText(v)
        return v

    monkeypatch.setattr('ansible.utils.unsafe_proxy.wrap_var', mock_wrap_var)

def test_wrap_set_with_various_types(mock_wrap_var):
    input_set = {None, MockAnsibleUnsafe(), MockNativeJinjaText("text"), b"bytes", "string"}
    wrapped_set = _wrap_set(input_set)

    assert len(wrapped_set) == 5
    assert None in wrapped_set
    assert any(isinstance(item, MockAnsibleUnsafe) for item in wrapped_set)
    assert any(isinstance(item, MockAnsibleUnsafeText) and item.value == "text" for item in wrapped_set)
    assert any(isinstance(item, MockAnsibleUnsafeBytes) and item.value == b"bytes" for item in wrapped_set)
    assert any(isinstance(item, MockAnsibleUnsafeText) and item.value == "string" for item in wrapped_set)
