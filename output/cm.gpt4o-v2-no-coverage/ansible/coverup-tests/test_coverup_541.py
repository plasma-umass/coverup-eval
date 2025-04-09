# file: lib/ansible/template/vars.py:108-122
# asked: {"lines": [108, 113, 114, 119, 120, 122], "branches": [[113, 114], [113, 119]]}
# gained: {"lines": [108, 113, 114, 119, 120, 122], "branches": [[113, 114], [113, 119]]}

import pytest
from ansible.template.vars import AnsibleJ2Vars
from unittest.mock import MagicMock

@pytest.fixture
def templar():
    return MagicMock()

@pytest.fixture
def globals():
    return {'global_var': 'global_value'}

@pytest.fixture
def locals():
    return {'local_var': 'local_value'}

def test_add_locals_with_none(templar, globals):
    ansible_vars = AnsibleJ2Vars(templar, globals)
    result = ansible_vars.add_locals(None)
    assert result is ansible_vars

def test_add_locals_with_values(templar, globals, locals):
    ansible_vars = AnsibleJ2Vars(templar, globals)
    result = ansible_vars.add_locals(locals)
    assert isinstance(result, AnsibleJ2Vars)
    assert result._locals['local_var'] == 'local_value'
    assert result._globals == globals
    assert result._templar == templar

def test_add_locals_updates_existing(templar, globals, locals):
    ansible_vars = AnsibleJ2Vars(templar, globals, locals={'existing_var': 'existing_value'})
    new_locals = {'new_var': 'new_value'}
    result = ansible_vars.add_locals(new_locals)
    assert isinstance(result, AnsibleJ2Vars)
    assert result._locals['existing_var'] == 'existing_value'
    assert result._locals['new_var'] == 'new_value'
    assert result._globals == globals
    assert result._templar == templar
