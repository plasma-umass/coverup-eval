# file lib/ansible/vars/manager.py:139-141
# lines [139, 140, 141]
# branches []

import pytest
from unittest.mock import MagicMock

# Assuming the VariableManager class is imported from ansible.vars.manager
from ansible.vars.manager import VariableManager

@pytest.fixture
def variable_manager():
    manager = VariableManager()
    manager._extra_vars = {'key': 'value'}
    return manager

def test_extra_vars_property(variable_manager):
    assert variable_manager.extra_vars == {'key': 'value'}
