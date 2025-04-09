# file lib/ansible/vars/manager.py:125-137
# lines [125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137]
# branches []

import pytest
from collections import defaultdict
from unittest.mock import patch
import os
from hashlib import sha1

# Assuming the VariableManager class is defined in ansible.vars.manager
from ansible.vars.manager import VariableManager

def test_variable_manager_setstate():
    data = {
        'fact_cache': {'host1': {'fact1': 'value1'}},
        'np_fact_cache': {'host2': {'fact2': 'value2'}},
        'vars_cache': {'host3': {'var1': 'value3'}},
        'extra_vars': {'extra_var1': 'extra_value1'},
        'host_vars_files': {'host4': {'file1': 'content1'}},
        'group_vars_files': {'group1': {'file2': 'content2'}},
        'omit_token': 'custom_omit_token',
        'inventory': 'custom_inventory',
        'options_vars': {'option1': 'value4'},
        'safe_basedir': True
    }

    vm = VariableManager()
    vm.__setstate__(data)

    assert vm._fact_cache == data['fact_cache']
    assert vm._nonpersistent_fact_cache == data['np_fact_cache']
    assert vm._vars_cache == data['vars_cache']
    assert vm._extra_vars == data['extra_vars']
    assert vm._host_vars_files == data['host_vars_files']
    assert vm._group_vars_files == data['group_vars_files']
    assert vm._omit_token == data['omit_token']
    assert vm._inventory == data['inventory']
    assert vm._options_vars == data['options_vars']
    assert vm.safe_basedir == data['safe_basedir']
    assert vm._loader is None
    assert vm._hostvars is None

def test_variable_manager_setstate_defaults():
    with patch('os.urandom', return_value=b'random_bytes'):
        data = {}
        vm = VariableManager()
        vm.__setstate__(data)

        assert vm._fact_cache == defaultdict(dict)
        assert vm._nonpersistent_fact_cache == defaultdict(dict)
        assert vm._vars_cache == defaultdict(dict)
        assert vm._extra_vars == {}
        assert vm._host_vars_files == defaultdict(dict)
        assert vm._group_vars_files == defaultdict(dict)
        assert vm._omit_token.startswith('__omit_place_holder__')
        assert vm._inventory is None
        assert vm._options_vars == {}
        assert vm.safe_basedir is False
        assert vm._loader is None
        assert vm._hostvars is None
