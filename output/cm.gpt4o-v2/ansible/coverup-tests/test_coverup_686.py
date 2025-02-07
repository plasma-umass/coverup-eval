# file: lib/ansible/template/vars.py:75-78
# asked: {"lines": [75, 76, 77, 78], "branches": []}
# gained: {"lines": [75, 76, 77, 78], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.template.vars import AnsibleJ2Vars

@pytest.fixture
def templar_mock():
    templar = MagicMock()
    templar.available_variables = {'var1': 'value1', 'var2': 'value2'}
    return templar

@pytest.fixture
def globals_dict():
    return {'global1': 'value1', 'global2': 'value2'}

@pytest.fixture
def locals_dict():
    return {'local1': 'value1', 'local2': 'value2'}

def test_ansiblej2vars_len(templar_mock, globals_dict, locals_dict):
    ansible_vars = AnsibleJ2Vars(templar_mock, globals_dict, locals_dict)
    assert len(ansible_vars) == 6  # 2 from templar, 2 from globals, 2 from locals

def test_ansiblej2vars_len_no_locals(templar_mock, globals_dict):
    ansible_vars = AnsibleJ2Vars(templar_mock, globals_dict)
    assert len(ansible_vars) == 4  # 2 from templar, 2 from globals
