# file: lib/ansible/playbook/role_include.py:68-70
# asked: {"lines": [68, 70], "branches": []}
# gained: {"lines": [68, 70], "branches": []}

import pytest
from ansible.playbook.role_include import IncludeRole

@pytest.fixture
def include_role():
    return IncludeRole()

def test_get_name_with_name(include_role, monkeypatch):
    monkeypatch.setattr(include_role, 'name', 'test_name')
    assert include_role.get_name() == 'test_name'

def test_get_name_without_name(include_role, monkeypatch):
    monkeypatch.setattr(include_role, 'name', None)
    monkeypatch.setattr(include_role, 'action', 'test_action')
    monkeypatch.setattr(include_role, '_role_name', 'test_role')
    assert include_role.get_name() == 'test_action : test_role'
