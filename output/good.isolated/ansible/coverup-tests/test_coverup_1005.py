# file lib/ansible/vars/manager.py:75-79
# lines [75, 77]
# branches []

import pytest
from ansible.vars.manager import VariableManager

# Assuming the missing lines/branches are related to accessing the _ALLOWED set
# The test below will access the _ALLOWed set and assert its contents

def test_variable_manager_allowed_set():
    vm = VariableManager()
    assert isinstance(vm._ALLOWED, frozenset)
    assert 'plugins_by_group' in vm._ALLOWED
    assert 'groups_plugins_play' in vm._ALLOWED
    assert 'groups_plugins_inventory' in vm._ALLOWED
    assert 'groups_inventory' in vm._ALLOWED
    assert 'all_plugins_play' in vm._ALLOWED
    assert 'all_plugins_inventory' in vm._ALLOWED
    assert 'all_inventory' in vm._ALLOWED
    assert len(vm._ALLOWED) == 7  # Ensure no unexpected items are in the set
