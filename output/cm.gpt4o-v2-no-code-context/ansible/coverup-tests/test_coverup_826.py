# file: lib/ansible/vars/reserved.py:82-83
# asked: {"lines": [82, 83], "branches": []}
# gained: {"lines": [82, 83], "branches": []}

import pytest
from ansible.vars.reserved import is_reserved_name

# Assuming _RESERVED_NAMES is a set of reserved names
_RESERVED_NAMES = {"ansible", "hostvars", "group_names"}

def test_is_reserved_name_true(monkeypatch):
    def mock_reserved_names():
        return _RESERVED_NAMES

    monkeypatch.setattr('ansible.vars.reserved._RESERVED_NAMES', mock_reserved_names())
    assert is_reserved_name("ansible") is True

def test_is_reserved_name_false(monkeypatch):
    def mock_reserved_names():
        return _RESERVED_NAMES

    monkeypatch.setattr('ansible.vars.reserved._RESERVED_NAMES', mock_reserved_names())
    assert is_reserved_name("not_reserved") is False
