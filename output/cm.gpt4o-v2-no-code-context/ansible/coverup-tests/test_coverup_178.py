# file: lib/ansible/vars/manager.py:80-108
# asked: {"lines": [80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 91, 95, 96, 99, 102, 103, 104, 107, 108], "branches": []}
# gained: {"lines": [80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 91, 95, 96, 99, 102, 103, 104, 107, 108], "branches": []}

import pytest
from unittest.mock import patch, MagicMock
from ansible.vars.manager import VariableManager
from ansible.errors import AnsibleError
from ansible.utils.display import Display
from collections import defaultdict
import os
from hashlib import sha1

@pytest.fixture
def mock_loader():
    return MagicMock()

@pytest.fixture
def mock_inventory():
    return MagicMock()

@pytest.fixture
def mock_version_info():
    return MagicMock()

@pytest.fixture
def mock_display(mocker):
    return mocker.patch('ansible.utils.display.Display.warning')

@pytest.fixture
def mock_fact_cache(mocker):
    return mocker.patch('ansible.vars.manager.FactCache')

@pytest.fixture
def mock_load_options_vars(mocker):
    return mocker.patch('ansible.vars.manager.load_options_vars', return_value={'basedir': False})

@pytest.fixture
def mock_load_extra_vars(mocker):
    return mocker.patch('ansible.vars.manager.load_extra_vars', return_value=defaultdict(dict))

def test_variable_manager_init_success(mock_loader, mock_inventory, mock_version_info, mock_load_options_vars, mock_load_extra_vars, mock_fact_cache):
    vm = VariableManager(loader=mock_loader, inventory=mock_inventory, version_info=mock_version_info)
    
    assert isinstance(vm._nonpersistent_fact_cache, defaultdict)
    assert isinstance(vm._vars_cache, defaultdict)
    assert isinstance(vm._extra_vars, defaultdict)
    assert isinstance(vm._host_vars_files, defaultdict)
    assert isinstance(vm._group_vars_files, defaultdict)
    assert vm._inventory == mock_inventory
    assert vm._loader == mock_loader
    assert vm._hostvars is None
    assert vm._omit_token.startswith('__omit_place_holder__')
    assert vm._options_vars == {'basedir': False}
    assert vm.safe_basedir is True
    assert vm._extra_vars == defaultdict(dict)
    assert isinstance(vm._fact_cache, MagicMock)

def test_variable_manager_init_fact_cache_error(mock_loader, mock_inventory, mock_version_info, mock_load_options_vars, mock_load_extra_vars, mocker, mock_display):
    mock_fact_cache = mocker.patch('ansible.vars.manager.FactCache', side_effect=AnsibleError('Test error'))
    
    vm = VariableManager(loader=mock_loader, inventory=mock_inventory, version_info=mock_version_info)
    
    mock_display.assert_called_once_with('Test error')
    assert vm._fact_cache == {}
