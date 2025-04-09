# file: lib/ansible/vars/reserved.py:82-83
# asked: {"lines": [82, 83], "branches": []}
# gained: {"lines": [82, 83], "branches": []}

import pytest
from ansible.vars.reserved import is_reserved_name

# Mock the _RESERVED_NAMES to ensure the test is isolated and does not depend on the actual reserved names
@pytest.fixture
def mock_reserved_names(monkeypatch):
    mock_names = {"ansible", "playbook", "host"}
    monkeypatch.setattr("ansible.vars.reserved._RESERVED_NAMES", mock_names)
    return mock_names

def test_is_reserved_name_true(mock_reserved_names):
    for name in mock_reserved_names:
        assert is_reserved_name(name) is True

def test_is_reserved_name_false(mock_reserved_names):
    non_reserved_names = {"task", "role", "inventory"}
    for name in non_reserved_names:
        assert is_reserved_name(name) is False
