# file: lib/ansible/template/vars.py:70-73
# asked: {"lines": [70, 71, 72, 73], "branches": []}
# gained: {"lines": [70, 71, 72, 73], "branches": []}

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

def test_ansiblej2vars_iter(templar, globals, locals):
    ansible_vars = AnsibleJ2Vars(templar, globals, locals)
    keys = set(['global_var', 'local_var'])
    assert set(ansible_vars) == keys

