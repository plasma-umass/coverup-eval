# file: lib/ansible/vars/manager.py:125-137
# asked: {"lines": [125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137], "branches": []}
# gained: {"lines": [125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137], "branches": []}

import pytest
from collections import defaultdict
from unittest.mock import patch
import os
from hashlib import sha1

# Assuming the VariableManager class is defined in ansible.vars.manager
from ansible.vars.manager import VariableManager

@pytest.fixture
def variable_manager():
    return VariableManager()

def test_variable_manager_setstate(variable_manager):
    data = {
        'fact_cache': {'host1': {'fact1': 'value1'}},
        'np_fact_cache': {'host2': {'fact2': 'value2'}},
        'vars_cache': {'host3': {'var1': 'value3'}},
        'extra_vars': {'extra_var1': 'extra_value1'},
        'host_vars_files': {'host4': {'file1': 'path1'}},
        'group_vars_files': {'group1': {'file2': 'path2'}},
        'omit_token': 'custom_omit_token',
        'inventory': 'custom_inventory',
        'options_vars': {'option1': 'value4'},
        'safe_basedir': True
    }

    with patch('os.urandom', return_value=b'random_bytes'):
        variable_manager.__setstate__(data)

    assert variable_manager._fact_cache == data['fact_cache']
    assert variable_manager._nonpersistent_fact_cache == data['np_fact_cache']
    assert variable_manager._vars_cache == data['vars_cache']
    assert variable_manager._extra_vars == data['extra_vars']
    assert variable_manager._host_vars_files == data['host_vars_files']
    assert variable_manager._group_vars_files == data['group_vars_files']
    assert variable_manager._omit_token == 'custom_omit_token'
    assert variable_manager._inventory == data['inventory']
    assert variable_manager._options_vars == data['options_vars']
    assert variable_manager.safe_basedir == data['safe_basedir']
    assert variable_manager._loader is None
    assert variable_manager._hostvars is None

def test_variable_manager_setstate_defaults(variable_manager):
    data = {}

    with patch('os.urandom', return_value=b'random_bytes'):
        variable_manager.__setstate__(data)

    assert variable_manager._fact_cache == defaultdict(dict)
    assert variable_manager._nonpersistent_fact_cache == defaultdict(dict)
    assert variable_manager._vars_cache == defaultdict(dict)
    assert variable_manager._extra_vars == {}
    assert variable_manager._host_vars_files == defaultdict(dict)
    assert variable_manager._group_vars_files == defaultdict(dict)
    assert variable_manager._omit_token.startswith('__omit_place_holder__')
    assert variable_manager._inventory is None
    assert variable_manager._options_vars == {}
    assert variable_manager.safe_basedir is False
    assert variable_manager._loader is None
    assert variable_manager._hostvars is None
