# file lib/ansible/template/vars.py:75-78
# lines [75, 76, 77, 78]
# branches []

import pytest
from ansible.template.vars import AnsibleJ2Vars

class MockTemplar:
    def __init__(self, available_variables):
        self.available_variables = available_variables

@pytest.fixture
def ansible_j2_vars():
    templar = MockTemplar(available_variables={'var1': 'value1', 'var2': 'value2'})
    ansible_j2_instance = AnsibleJ2Vars(templar, {'global1': 'value4'})
    ansible_j2_instance._locals = {'local1': 'value3'}
    return ansible_j2_instance

def test_ansible_j2_vars_len(ansible_j2_vars):
    assert len(ansible_j2_vars) == 4, "The length should be the number of unique keys across _templar, _locals, and _globals"
