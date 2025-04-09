# file: lib/ansible/vars/manager.py:125-137
# asked: {"lines": [125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137], "branches": []}
# gained: {"lines": [125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137], "branches": []}

import pytest
from collections import defaultdict
from hashlib import sha1
import os
from ansible.vars.manager import VariableManager

@pytest.fixture
def variable_manager():
    return VariableManager()

def test_setstate_with_empty_data(variable_manager):
    data = {}
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

def test_setstate_with_data(variable_manager):
    data = {
        'fact_cache': {'key1': 'value1'},
        'np_fact_cache': {'key2': 'value2'},
        'vars_cache': {'key3': 'value3'},
        'extra_vars': {'key4': 'value4'},
        'host_vars_files': {'key5': 'value5'},
        'group_vars_files': {'key6': 'value6'},
        'omit_token': 'custom_omit_token',
        'inventory': 'custom_inventory',
        'options_vars': {'key7': 'value7'},
        'safe_basedir': True
    }
    variable_manager.__setstate__(data)
    
    assert variable_manager._fact_cache == {'key1': 'value1'}
    assert variable_manager._nonpersistent_fact_cache == {'key2': 'value2'}
    assert variable_manager._vars_cache == {'key3': 'value3'}
    assert variable_manager._extra_vars == {'key4': 'value4'}
    assert variable_manager._host_vars_files == {'key5': 'value5'}
    assert variable_manager._group_vars_files == {'key6': 'value6'}
    assert variable_manager._omit_token == 'custom_omit_token'
    assert variable_manager._inventory == 'custom_inventory'
    assert variable_manager._options_vars == {'key7': 'value7'}
    assert variable_manager.safe_basedir is True
    assert variable_manager._loader is None
    assert variable_manager._hostvars is None
