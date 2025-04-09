# file: lib/ansible/template/vars.py:70-73
# asked: {"lines": [70, 71, 72, 73], "branches": []}
# gained: {"lines": [70, 71, 72, 73], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.template.vars import AnsibleJ2Vars

@pytest.fixture
def templar():
    mock_templar = MagicMock()
    mock_templar.available_variables = {'var1': 'value1', 'var2': 'value2'}
    return mock_templar

@pytest.fixture
def globals():
    return {'global1': 'value1', 'global2': 'value2'}

@pytest.fixture
def locals():
    return {'local1': 'value1', 'local2': 'value2'}

def test_ansiblej2vars_iter(templar, globals, locals):
    ansible_vars = AnsibleJ2Vars(templar, globals, locals)
    keys = set(ansible_vars)
    expected_keys = {'var1', 'var2', 'global1', 'global2', 'local1', 'local2'}
    assert keys == expected_keys

