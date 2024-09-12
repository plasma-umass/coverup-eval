# file: lib/ansible/vars/manager.py:139-141
# asked: {"lines": [139, 140, 141], "branches": []}
# gained: {"lines": [139, 140, 141], "branches": []}

import pytest
from ansible.vars.manager import VariableManager

def test_extra_vars_property():
    # Create an instance of VariableManager
    variable_manager = VariableManager()

    # Access the extra_vars property
    extra_vars = variable_manager.extra_vars

    # Assert that the extra_vars property returns the expected value
    assert extra_vars == variable_manager._extra_vars
