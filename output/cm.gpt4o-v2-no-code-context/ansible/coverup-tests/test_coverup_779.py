# file: lib/ansible/utils/unsafe_proxy.py:145-146
# asked: {"lines": [145, 146], "branches": []}
# gained: {"lines": [145, 146], "branches": []}

import pytest
from ansible.utils.unsafe_proxy import to_unsafe_text
from ansible.module_utils._text import to_text

def test_to_unsafe_text(monkeypatch):
    def mock_to_text(*args, **kwargs):
        return "mocked_text"

    def mock_wrap_var(value):
        return f"wrapped_{value}"

    monkeypatch.setattr('ansible.utils.unsafe_proxy.to_text', mock_to_text)
    monkeypatch.setattr('ansible.utils.unsafe_proxy.wrap_var', mock_wrap_var)

    result = to_unsafe_text("input_text")
    assert result == "wrapped_mocked_text"
