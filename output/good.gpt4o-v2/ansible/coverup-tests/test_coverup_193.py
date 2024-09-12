# file: lib/ansible/vars/manager.py:80-108
# asked: {"lines": [80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 91, 95, 96, 99, 102, 103, 104, 107, 108], "branches": []}
# gained: {"lines": [80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 91, 95, 96, 99, 102, 103, 104, 107, 108], "branches": []}

import pytest
from unittest.mock import patch, MagicMock
from collections import defaultdict
from ansible.vars.manager import VariableManager
from ansible.errors import AnsibleError

@pytest.fixture
def mock_loader():
    return MagicMock()

@pytest.fixture
def mock_inventory():
    return MagicMock()

@pytest.fixture
def mock_version_info():
    return MagicMock()

def test_variable_manager_init_success(mock_loader, mock_inventory, mock_version_info):
    with patch('ansible.vars.manager.load_options_vars', return_value={'basedir': '/some/path'}), \
         patch('ansible.vars.manager.load_extra_vars', return_value={'some_var': 'some_value'}), \
         patch('ansible.vars.manager.FactCache', return_value={'fact_key': 'fact_value'}):
        
        vm = VariableManager(loader=mock_loader, inventory=mock_inventory, version_info=mock_version_info)
        
        assert vm._nonpersistent_fact_cache == defaultdict(dict)
        assert vm._vars_cache == defaultdict(dict)
        assert vm._extra_vars == {'some_var': 'some_value'}
        assert vm._host_vars_files == defaultdict(dict)
        assert vm._group_vars_files == defaultdict(dict)
        assert vm._inventory == mock_inventory
        assert vm._loader == mock_loader
        assert vm._hostvars is None
        assert vm._omit_token.startswith('__omit_place_holder__')
        assert vm._options_vars == {'basedir': '/some/path'}
        assert vm.safe_basedir is True
        assert vm._fact_cache == {'fact_key': 'fact_value'}

def test_variable_manager_init_no_basedir(mock_loader, mock_inventory, mock_version_info):
    with patch('ansible.vars.manager.load_options_vars', return_value={}), \
         patch('ansible.vars.manager.load_extra_vars', return_value={'some_var': 'some_value'}), \
         patch('ansible.vars.manager.FactCache', return_value={'fact_key': 'fact_value'}):
        
        vm = VariableManager(loader=mock_loader, inventory=mock_inventory, version_info=mock_version_info)
        
        assert vm.safe_basedir is True

def test_variable_manager_init_fact_cache_error(mock_loader, mock_inventory, mock_version_info):
    with patch('ansible.vars.manager.load_options_vars', return_value={'basedir': '/some/path'}), \
         patch('ansible.vars.manager.load_extra_vars', return_value={'some_var': 'some_value'}), \
         patch('ansible.vars.manager.FactCache', side_effect=AnsibleError('Cache error')), \
         patch('ansible.vars.manager.display.warning') as mock_warning:
        
        vm = VariableManager(loader=mock_loader, inventory=mock_inventory, version_info=mock_version_info)
        
        mock_warning.assert_called_once_with('Cache error')
        assert vm._fact_cache == {}
