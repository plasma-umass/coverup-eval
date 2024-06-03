# file lib/ansible/vars/manager.py:80-108
# lines [80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 91, 95, 96, 99, 102, 103, 104, 107, 108]
# branches []

import pytest
from unittest.mock import patch, MagicMock
from collections import defaultdict
import os
from hashlib import sha1
from ansible.errors import AnsibleError
from ansible.vars.manager import VariableManager

# Mock functions to replace actual implementations
def mock_load_options_vars(version_info):
    return {'basedir': ''}

def mock_load_extra_vars(loader):
    return {'extra_var_key': 'extra_var_value'}

class MockFactCache:
    pass

@pytest.fixture
def mock_display_warning(mocker):
    return mocker.patch('ansible.utils.display.Display.warning')

@pytest.fixture
def mock_fact_cache(mocker):
    return mocker.patch('ansible.vars.manager.FactCache', side_effect=MockFactCache)

@pytest.fixture
def mock_fact_cache_error(mocker):
    return mocker.patch('ansible.vars.manager.FactCache', side_effect=AnsibleError("Mocked AnsibleError"))

@pytest.fixture
def mock_to_text(mocker):
    return mocker.patch('ansible.utils.display.to_text', side_effect=lambda x: str(x))

@pytest.fixture
def mock_sha1(mocker):
    return mocker.patch('hashlib.sha1', side_effect=lambda x: sha1(x))

@pytest.fixture
def mock_urandom(mocker):
    return mocker.patch('os.urandom', side_effect=lambda x: b'random_bytes')

@pytest.fixture
def mock_load_options_vars_func(mocker):
    return mocker.patch('ansible.vars.manager.load_options_vars', side_effect=mock_load_options_vars)

@pytest.fixture
def mock_load_extra_vars_func(mocker):
    return mocker.patch('ansible.vars.manager.load_extra_vars', side_effect=mock_load_extra_vars)

def test_variable_manager_initialization(mock_display_warning, mock_fact_cache, mock_to_text, mock_sha1, mock_urandom, mock_load_options_vars_func, mock_load_extra_vars_func):
    loader = MagicMock()
    inventory = MagicMock()
    version_info = MagicMock()

    vm = VariableManager(loader=loader, inventory=inventory, version_info=version_info)

    assert vm._nonpersistent_fact_cache == defaultdict(dict)
    assert vm._vars_cache == defaultdict(dict)
    assert vm._extra_vars == {'extra_var_key': 'extra_var_value'}
    assert vm._host_vars_files == defaultdict(dict)
    assert vm._group_vars_files == defaultdict(dict)
    assert vm._inventory == inventory
    assert vm._loader == loader
    assert vm._hostvars is None
    assert vm._omit_token.startswith('__omit_place_holder__')
    assert vm.safe_basedir is False
    assert isinstance(vm._fact_cache, MockFactCache)

def test_variable_manager_fact_cache_error(mock_display_warning, mock_fact_cache_error, mock_to_text, mock_sha1, mock_urandom, mock_load_options_vars_func, mock_load_extra_vars_func):
    loader = MagicMock()
    inventory = MagicMock()
    version_info = MagicMock()

    vm = VariableManager(loader=loader, inventory=inventory, version_info=version_info)

    assert vm._nonpersistent_fact_cache == defaultdict(dict)
    assert vm._vars_cache == defaultdict(dict)
    assert vm._extra_vars == {'extra_var_key': 'extra_var_value'}
    assert vm._host_vars_files == defaultdict(dict)
    assert vm._group_vars_files == defaultdict(dict)
    assert vm._inventory == inventory
    assert vm._loader == loader
    assert vm._hostvars is None
    assert vm._omit_token.startswith('__omit_place_holder__')
    assert vm.safe_basedir is False
    assert isinstance(vm._fact_cache, dict)
    mock_display_warning.assert_called_once_with('Mocked AnsibleError')
