# file: lib/ansible/utils/unsafe_proxy.py:117-118
# asked: {"lines": [117, 118], "branches": []}
# gained: {"lines": [117, 118], "branches": []}

import pytest
from ansible.utils.unsafe_proxy import wrap_var

def test_wrap_set(monkeypatch):
    from ansible.utils.unsafe_proxy import _wrap_set

    class MockWrapVar:
        def __init__(self, value):
            self.value = value

        def __eq__(self, other):
            return self.value == other.value

        def __hash__(self):
            return hash(self.value)

    def mock_wrap_var(item):
        return MockWrapVar(item)

    monkeypatch.setattr('ansible.utils.unsafe_proxy.wrap_var', mock_wrap_var)

    input_set = {1, 2, 3}
    wrapped_set = _wrap_set(input_set)

    expected_set = {MockWrapVar(1), MockWrapVar(2), MockWrapVar(3)}
    assert wrapped_set == expected_set
