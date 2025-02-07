# file: lib/ansible/utils/unsafe_proxy.py:117-118
# asked: {"lines": [117, 118], "branches": []}
# gained: {"lines": [117, 118], "branches": []}

import pytest
from ansible.utils.unsafe_proxy import _wrap_set, wrap_var

def test_wrap_set(monkeypatch):
    class MockUnsafe:
        pass

    def mock_wrap_var(item):
        return f"wrapped_{item}"

    monkeypatch.setattr('ansible.utils.unsafe_proxy.wrap_var', mock_wrap_var)

    input_set = {1, 2, 3}
    expected_output = {"wrapped_1", "wrapped_2", "wrapped_3"}

    result = _wrap_set(input_set)
    assert result == expected_output
