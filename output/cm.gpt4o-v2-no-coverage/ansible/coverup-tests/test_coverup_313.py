# file: lib/ansible/template/vars.py:61-68
# asked: {"lines": [61, 62, 63, 64, 65, 66, 67, 68], "branches": [[62, 63], [62, 64], [64, 65], [64, 66], [66, 67], [66, 68]]}
# gained: {"lines": [61, 62, 63, 64, 65, 66, 67, 68], "branches": [[62, 63], [62, 64], [64, 65], [64, 66], [66, 67], [66, 68]]}

import pytest
from unittest.mock import MagicMock
from ansible.template.vars import AnsibleJ2Vars

@pytest.fixture
def templar():
    return MagicMock()

@pytest.fixture
def globals():
    return {'global_var': 'value'}

@pytest.fixture
def locals():
    return {'local_var': 'value'}

@pytest.fixture
def ansible_j2_vars(templar, globals, locals):
    return AnsibleJ2Vars(templar, globals, locals)

def test_contains_in_locals(ansible_j2_vars):
    assert 'local_var' in ansible_j2_vars

def test_contains_in_templar(ansible_j2_vars, templar):
    templar.available_variables = {'templar_var': 'value'}
    assert 'templar_var' in ansible_j2_vars

def test_contains_in_globals(ansible_j2_vars):
    assert 'global_var' in ansible_j2_vars

def test_contains_not_found(ansible_j2_vars):
    assert 'non_existent_var' not in ansible_j2_vars
