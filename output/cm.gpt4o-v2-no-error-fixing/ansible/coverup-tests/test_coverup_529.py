# file: lib/ansible/vars/manager.py:139-141
# asked: {"lines": [139, 140, 141], "branches": []}
# gained: {"lines": [139, 140, 141], "branches": []}

import pytest
from unittest.mock import patch, MagicMock
from ansible.vars.manager import VariableManager

@pytest.fixture
def variable_manager():
    with patch('ansible.vars.manager.load_extra_vars', return_value={'key': 'value'}):
        return VariableManager()

def test_extra_vars_property(variable_manager):
    assert variable_manager.extra_vars == {'key': 'value'}
