# file lib/ansible/vars/manager.py:125-137
# lines [126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137]
# branches []

import pytest
from ansible.vars.manager import VariableManager
from collections import defaultdict
import os
from hashlib import sha1

@pytest.fixture
def variable_manager_data():
    return {
        'fact_cache': defaultdict(dict, {'host1': {'fact1': 'value1'}}),
        'np_fact_cache': defaultdict(dict, {'host2': {'fact2': 'value2'}}),
        'vars_cache': defaultdict(dict, {'host3': {'var1': 'value3'}}),
        'extra_vars': {'extra_var1': 'value4'},
        'host_vars_files': defaultdict(dict, {'host_vars_file1': 'value5'}),
        'group_vars_files': defaultdict(dict, {'group_vars_file1': 'value6'}),
        'omit_token': '__omit_place_holder__%s' % sha1(os.urandom(64)).hexdigest(),
        'inventory': 'inventory_instance',
        'options_vars': {'option_var1': 'value7'},
        'safe_basedir': True
    }

@pytest.fixture
def variable_manager(variable_manager_data):
    vm = VariableManager()
    vm.__setstate__(variable_manager_data)
    return vm

def test_variable_manager_setstate(variable_manager, variable_manager_data):
    assert variable_manager._fact_cache == variable_manager_data['fact_cache']
    assert variable_manager._nonpersistent_fact_cache == variable_manager_data['np_fact_cache']
    assert variable_manager._vars_cache == variable_manager_data['vars_cache']
    assert variable_manager._extra_vars == variable_manager_data['extra_vars']
    assert variable_manager._host_vars_files == variable_manager_data['host_vars_files']
    assert variable_manager._group_vars_files == variable_manager_data['group_vars_files']
    assert variable_manager._omit_token == variable_manager_data['omit_token']
    assert variable_manager._inventory == variable_manager_data['inventory']
    assert variable_manager._options_vars == variable_manager_data['options_vars']
    assert variable_manager.safe_basedir == variable_manager_data['safe_basedir']
    assert variable_manager._loader is None
    assert variable_manager._hostvars is None
