# file: lib/ansible/template/vars.py:75-78
# asked: {"lines": [75, 76, 77, 78], "branches": []}
# gained: {"lines": [75, 76, 77, 78], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.template.vars import AnsibleJ2Vars

@pytest.fixture
def mock_templar():
    templar = MagicMock()
    templar.available_variables = {'var1': 'value1', 'var2': 'value2'}
    return templar

@pytest.fixture
def ansible_j2_vars(mock_templar):
    globals_dict = {'global1': 'value1'}
    locals_dict = {'local1': 'value1'}
    return AnsibleJ2Vars(mock_templar, globals_dict, locals_dict)

def test_ansible_j2_vars_len(ansible_j2_vars):
    assert len(ansible_j2_vars) == 4
