# file lib/ansible/template/vars.py:108-122
# lines [108, 113, 114, 119, 120, 122]
# branches ['113->114', '113->119']

import pytest
from ansible.template.vars import AnsibleJ2Vars

@pytest.fixture
def ansible_j2_vars(mocker):
    templar = mocker.MagicMock()
    globals_dict = {}
    locals_dict = {}
    return AnsibleJ2Vars(templar, globals_dict, locals=locals_dict)

def test_ansible_j2_vars_add_locals(ansible_j2_vars):
    new_locals = {'key': 'value'}
    new_ansible_j2_vars = ansible_j2_vars.add_locals(new_locals)
    
    assert new_ansible_j2_vars is not ansible_j2_vars, "add_locals should return a new object"
    assert new_ansible_j2_vars._locals['key'] == 'value', "new local should be added to the new object"
    assert 'key' not in ansible_j2_vars._locals, "original object's locals should not be modified"

def test_ansible_j2_vars_add_locals_none(ansible_j2_vars):
    new_ansible_j2_vars = ansible_j2_vars.add_locals(None)
    
    assert new_ansible_j2_vars is ansible_j2_vars, "add_locals should return the same object when None is passed"
