# file: lib/ansible/template/vars.py:43-59
# asked: {"lines": [43, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59], "branches": [[53, 0], [53, 54], [54, 0], [54, 55], [55, 54], [55, 56], [56, 57], [56, 58], [58, 54], [58, 59]]}
# gained: {"lines": [43, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59], "branches": [[53, 0], [53, 54], [54, 0], [54, 55], [55, 56], [56, 57], [56, 58], [58, 54], [58, 59]]}

import pytest
from unittest.mock import MagicMock
from ansible.module_utils.six import iteritems
from ansible.template.vars import AnsibleJ2Vars

@pytest.fixture
def templar():
    return MagicMock()

@pytest.fixture
def globals():
    return {'global_var': 'value'}

def test_ansible_j2_vars_init_with_locals(templar, globals):
    locals = {
        'l_local_var': 'local_value',
        'context': 'should_be_ignored',
        'environment': 'should_be_ignored',
        'template': 'should_be_ignored',
        'other_var': 'other_value'
    }
    ansible_vars = AnsibleJ2Vars(templar, globals, locals)
    
    assert ansible_vars._templar == templar
    assert ansible_vars._globals == globals
    assert ansible_vars._locals == {
        'local_var': 'local_value',
        'other_var': 'other_value'
    }

def test_ansible_j2_vars_init_without_locals(templar, globals):
    ansible_vars = AnsibleJ2Vars(templar, globals)
    
    assert ansible_vars._templar == templar
    assert ansible_vars._globals == globals
    assert ansible_vars._locals == {}
