# file: lib/ansible/vars/manager.py:125-137
# asked: {"lines": [125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137], "branches": []}
# gained: {"lines": [125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137], "branches": []}

import pytest
from collections import defaultdict
from hashlib import sha1
import os

from ansible.vars.manager import VariableManager

def test_setstate():
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

    vm = VariableManager()
    vm.__setstate__(data)

    assert vm._fact_cache == {'key1': 'value1'}
    assert vm._nonpersistent_fact_cache == {'key2': 'value2'}
    assert vm._vars_cache == {'key3': 'value3'}
    assert vm._extra_vars == {'key4': 'value4'}
    assert vm._host_vars_files == {'key5': 'value5'}
    assert vm._group_vars_files == {'key6': 'value6'}
    assert vm._omit_token == 'custom_omit_token'
    assert vm._inventory == 'custom_inventory'
    assert vm._options_vars == {'key7': 'value7'}
    assert vm.safe_basedir is True
    assert vm._loader is None
    assert vm._hostvars is None

def test_setstate_defaults():
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
