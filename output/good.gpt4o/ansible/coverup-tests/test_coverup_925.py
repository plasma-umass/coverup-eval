# file lib/ansible/vars/manager.py:75-79
# lines [75, 77]
# branches []

import pytest
from ansible.vars.manager import VariableManager

def test_variable_manager_allowed():
    # Check if the _ALLOWED attribute is correctly set
    expected_allowed = frozenset(['plugins_by_group', 'groups_plugins_play', 'groups_plugins_inventory', 'groups_inventory',
                                  'all_plugins_play', 'all_plugins_inventory', 'all_inventory'])
    assert VariableManager._ALLOWED == expected_allowed
