# file lib/ansible/template/vars.py:70-73
# lines [70, 71, 72, 73]
# branches []

import pytest
from ansible.template.vars import AnsibleJ2Vars

class MockTemplar:
    def __init__(self, available_variables):
        self.available_variables = available_variables

@pytest.fixture
def ansible_j2_vars():
    templar = MockTemplar(available_variables={'var1': 'value1', 'var2': 'value2'})
    ansible_j2_vars_instance = AnsibleJ2Vars(templar, {'global1': 'value4'})
    ansible_j2_vars_instance._locals = {'local1': 'value3'}
    return ansible_j2_vars_instance

def test_ansible_j2_vars_iter(ansible_j2_vars):
    # Test __iter__ method of AnsibleJ2Vars
    keys = list(iter(ansible_j2_vars))
    assert 'var1' in keys
    assert 'var2' in keys
    assert 'local1' in keys
    assert 'global1' in keys
    assert len(keys) == 4  # Ensure no duplicates and all keys are present
