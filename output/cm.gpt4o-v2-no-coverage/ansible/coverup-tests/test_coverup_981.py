# file: lib/ansible/vars/reserved.py:82-83
# asked: {"lines": [82, 83], "branches": []}
# gained: {"lines": [82, 83], "branches": []}

import pytest
from ansible.vars.reserved import is_reserved_name

def test_is_reserved_name(monkeypatch):
    # Mock the _RESERVED_NAMES to control the test environment
    mock_reserved_names = frozenset(['reserved1', 'reserved2'])
    monkeypatch.setattr('ansible.vars.reserved._RESERVED_NAMES', mock_reserved_names)
    
    # Test cases
    assert is_reserved_name('reserved1') == True
    assert is_reserved_name('reserved2') == True
    assert is_reserved_name('not_reserved') == False
