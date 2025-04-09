# file: lib/ansible/vars/plugins.py:42-77
# asked: {"lines": [59], "branches": [[53, 47], [57, 59], [70, 75]]}
# gained: {"lines": [], "branches": [[70, 75]]}

import pytest
from unittest.mock import Mock, patch
from ansible.vars import plugins
from ansible.plugins.loader import vars_loader
from ansible.utils.vars import combine_vars

@pytest.fixture
def mock_loader():
    return Mock()

@pytest.fixture
def mock_path():
    return "mock_path"

@pytest.fixture
def mock_entities():
    return ["entity1", "entity2"]

@pytest.fixture
def mock_stage():
    return "mock_stage"

@pytest.fixture
def mock_vars_loader(monkeypatch):
    mock_vars_loader = Mock()
    monkeypatch.setattr(vars_loader, 'all', mock_vars_loader.all)
    monkeypatch.setattr(vars_loader, 'get', mock_vars_loader.get)
    return mock_vars_loader

@pytest.fixture
def mock_C(monkeypatch):
    mock_C = Mock()
    monkeypatch.setattr(plugins, 'C', mock_C)
    return mock_C

@pytest.fixture
def mock_combine_vars(monkeypatch):
    mock_combine_vars = Mock()
    monkeypatch.setattr(plugins, 'combine_vars', mock_combine_vars)
    return mock_combine_vars

def test_get_vars_from_path_plugin_not_in_list(mock_loader, mock_path, mock_entities, mock_stage, mock_vars_loader, mock_C, mock_combine_vars):
    mock_C.VARIABLE_PLUGINS_ENABLED = ['plugin1']
    mock_C.RUN_VARS_PLUGINS = 'demand'
    mock_vars_loader.all.return_value = []
    mock_plugin = Mock()
    mock_plugin._load_name = 'plugin1'
    mock_plugin.REQUIRES_WHITELIST = True
    mock_vars_loader.get.return_value = mock_plugin

    with patch('ansible.vars.plugins.AnsibleCollectionRef.is_valid_fqcr', return_value=True):
        result = plugins.get_vars_from_path(mock_loader, mock_path, mock_entities, mock_stage)

    assert result == {}
    mock_vars_loader.get.assert_called_with('plugin1')
    mock_combine_vars.assert_not_called()

def test_get_vars_from_path_stage_inventory(mock_loader, mock_path, mock_entities, mock_stage, mock_vars_loader, mock_C, mock_combine_vars):
    mock_C.VARIABLE_PLUGINS_ENABLED = ['plugin1']
    mock_C.RUN_VARS_PLUGINS = 'demand'
    mock_vars_loader.all.return_value = []
    mock_plugin = Mock()
    mock_plugin._load_name = 'plugin1'
    mock_plugin.REQUIRES_WHITELIST = False
    mock_vars_loader.get.return_value = mock_plugin

    with patch('ansible.vars.plugins.AnsibleCollectionRef.is_valid_fqcr', return_value=True):
        result = plugins.get_vars_from_path(mock_loader, mock_path, mock_entities, 'inventory')

    assert result == {}
    mock_vars_loader.get.assert_called_with('plugin1')
    mock_combine_vars.assert_not_called()

def test_get_vars_from_path_stage_task(mock_loader, mock_path, mock_entities, mock_stage, mock_vars_loader, mock_C, mock_combine_vars):
    mock_C.VARIABLE_PLUGINS_ENABLED = ['plugin1']
    mock_C.RUN_VARS_PLUGINS = 'start'
    mock_vars_loader.all.return_value = []
    mock_plugin = Mock()
    mock_plugin._load_name = 'plugin1'
    mock_plugin.REQUIRES_WHITELIST = False
    mock_vars_loader.get.return_value = mock_plugin

    with patch('ansible.vars.plugins.AnsibleCollectionRef.is_valid_fqcr', return_value=True):
        result = plugins.get_vars_from_path(mock_loader, mock_path, mock_entities, 'task')

    assert result == {}
    mock_vars_loader.get.assert_called_with('plugin1')
    mock_combine_vars.assert_not_called()

def test_get_vars_from_path_combine_vars(mock_loader, mock_path, mock_entities, mock_stage, mock_vars_loader, mock_C, mock_combine_vars):
    mock_C.VARIABLE_PLUGINS_ENABLED = ['plugin1']
    mock_C.RUN_VARS_PLUGINS = 'demand'
    mock_vars_loader.all.return_value = []
    mock_plugin = Mock()
    mock_plugin._load_name = 'plugin1'
    mock_plugin.REQUIRES_WHITELIST = False
    mock_plugin.get_option.return_value = None
    mock_vars_loader.get.return_value = mock_plugin

    mock_combine_vars.return_value = {'key': 'value'}

    with patch('ansible.vars.plugins.AnsibleCollectionRef.is_valid_fqcr', return_value=True):
        result = plugins.get_vars_from_path(mock_loader, mock_path, mock_entities, mock_stage)

    assert result == {'key': 'value'}
    mock_vars_loader.get.assert_called_with('plugin1')
    mock_combine_vars.assert_called_once()
