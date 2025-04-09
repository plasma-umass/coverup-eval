# file: lib/ansible/vars/manager.py:80-108
# asked: {"lines": [80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 91, 95, 96, 99, 102, 103, 104, 107, 108], "branches": []}
# gained: {"lines": [80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 91, 95, 96, 99, 102, 103, 104, 107, 108], "branches": []}

import pytest
from unittest.mock import patch, MagicMock
from ansible.errors import AnsibleError
from ansible.vars.manager import VariableManager

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
def mock_fact_cache():
    with patch('ansible.vars.manager.FactCache', autospec=True) as mock:
        yield mock

@pytest.fixture
def mock_load_options_vars():
    with patch('ansible.vars.manager.load_options_vars', autospec=True) as mock:
        yield mock

@pytest.fixture
def mock_load_extra_vars():
    with patch('ansible.vars.manager.load_extra_vars', autospec=True) as mock:
        yield mock

@pytest.fixture
def mock_display_warning():
    with patch('ansible.vars.manager.display.warning', autospec=True) as mock:
        yield mock

def test_variable_manager_init_success(mock_loader, mock_inventory, mock_version_info, mock_fact_cache, mock_load_options_vars, mock_load_extra_vars):
    mock_load_options_vars.return_value = {'basedir': '/some/path'}
    mock_load_extra_vars.return_value = {'some_var': 'some_value'}
    mock_fact_cache.return_value = MagicMock()

    vm = VariableManager(loader=mock_loader, inventory=mock_inventory, version_info=mock_version_info)

    assert vm._loader == mock_loader
    assert vm._inventory == mock_inventory
    assert vm._options_vars == {'basedir': '/some/path'}
    assert vm.safe_basedir is True
    assert vm._extra_vars == {'some_var': 'some_value'}
    assert isinstance(vm._fact_cache, MagicMock)

def test_variable_manager_init_no_basedir(mock_loader, mock_inventory, mock_version_info, mock_fact_cache, mock_load_options_vars, mock_load_extra_vars):
    mock_load_options_vars.return_value = {}
    mock_load_extra_vars.return_value = {'some_var': 'some_value'}
    mock_fact_cache.return_value = MagicMock()

    vm = VariableManager(loader=mock_loader, inventory=mock_inventory, version_info=mock_version_info)

    assert vm.safe_basedir is True

def test_variable_manager_init_fact_cache_error(mock_loader, mock_inventory, mock_version_info, mock_fact_cache, mock_load_options_vars, mock_load_extra_vars, mock_display_warning):
    mock_load_options_vars.return_value = {'basedir': '/some/path'}
    mock_load_extra_vars.return_value = {'some_var': 'some_value'}
    mock_fact_cache.side_effect = AnsibleError("Cache plugin error")

    vm = VariableManager(loader=mock_loader, inventory=mock_inventory, version_info=mock_version_info)

    mock_display_warning.assert_called_once_with("Cache plugin error")
    assert vm._fact_cache == {}
