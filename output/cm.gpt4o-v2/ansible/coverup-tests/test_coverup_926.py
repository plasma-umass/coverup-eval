# file: lib/ansible/utils/unsafe_proxy.py:105-106
# asked: {"lines": [105, 106], "branches": []}
# gained: {"lines": [105, 106], "branches": []}

import pytest
from ansible.utils.unsafe_proxy import _wrap_dict, wrap_var

def test_wrap_dict(monkeypatch):
    class MockAnsibleUnsafe:
        pass

    def mock_wrap_var(v):
        if isinstance(v, MockAnsibleUnsafe):
            return v
        return f"wrapped_{v}"

    monkeypatch.setattr('ansible.utils.unsafe_proxy.wrap_var', mock_wrap_var)

    input_dict = {'key1': 'value1', 'key2': MockAnsibleUnsafe()}
    expected_output = {'wrapped_key1': 'wrapped_value1', 'wrapped_key2': input_dict['key2']}

    result = _wrap_dict(input_dict)
    assert result == expected_output
