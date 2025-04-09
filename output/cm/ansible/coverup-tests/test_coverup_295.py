# file lib/ansible/template/vars.py:61-68
# lines [61, 62, 63, 64, 65, 66, 67, 68]
# branches ['62->63', '62->64', '64->65', '64->66', '66->67', '66->68']

import pytest
from ansible.template.vars import AnsibleJ2Vars

class MockTemplar:
    def __init__(self, available_variables):
        self.available_variables = available_variables

@pytest.fixture
def ansible_j2_vars():
    templar = MockTemplar(available_variables={'available_var': 'value'})
    globals_dict = {'global_var': 'value'}
    locals_dict = {'local_var': 'value'}
    ansible_j2_vars_instance = AnsibleJ2Vars(templar, globals_dict)
    ansible_j2_vars_instance._locals = locals_dict
    return ansible_j2_vars_instance

def test_ansible_j2_vars_contains(ansible_j2_vars):
    # Test __contains__ for local variable
    assert 'local_var' in ansible_j2_vars
    # Test __contains__ for available variable
    assert 'available_var' in ansible_j2_vars
    # Test __contains__ for global variable
    assert 'global_var' in ansible_j2_vars
    # Test __contains__ for non-existent variable
    assert 'non_existent_var' not in ansible_j2_vars
