# file: lib/ansible/utils/unsafe_proxy.py:109-114
# asked: {"lines": [113, 114], "branches": []}
# gained: {"lines": [113, 114], "branches": []}

import pytest
from ansible.utils.unsafe_proxy import _wrap_sequence, wrap_var

def test_wrap_sequence_with_list(monkeypatch):
    class MockUnsafe:
        pass

    def mock_wrap_var(item):
        return MockUnsafe()

    monkeypatch.setattr('ansible.utils.unsafe_proxy.wrap_var', mock_wrap_var)

    input_list = [1, 2, 3]
    result = _wrap_sequence(input_list)

    assert all(isinstance(item, MockUnsafe) for item in result)
    assert isinstance(result, list)

def test_wrap_sequence_with_tuple(monkeypatch):
    class MockUnsafe:
        pass

    def mock_wrap_var(item):
        return MockUnsafe()

    monkeypatch.setattr('ansible.utils.unsafe_proxy.wrap_var', mock_wrap_var)

    input_tuple = (1, 2, 3)
    result = _wrap_sequence(input_tuple)

    assert all(isinstance(item, MockUnsafe) for item in result)
    assert isinstance(result, tuple)
