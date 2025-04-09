# file: lib/ansible/vars/plugins.py:42-77
# asked: {"lines": [42, 44, 46, 47, 48, 49, 50, 52, 53, 54, 56, 57, 59, 61, 65, 67, 68, 69, 70, 71, 72, 73, 75, 77], "branches": [[47, 48], [47, 56], [48, 47], [48, 49], [50, 52], [50, 53], [53, 47], [53, 54], [56, 57], [56, 77], [57, 59], [57, 61], [67, 68], [67, 72], [68, 69], [68, 70], [70, 71], [70, 75], [72, 73], [72, 75]]}
# gained: {"lines": [42, 44, 46, 47, 48, 49, 50, 52, 53, 54, 56, 57, 61, 65, 67, 68, 69, 70, 71, 72, 73, 75, 77], "branches": [[47, 48], [47, 56], [48, 47], [48, 49], [50, 52], [50, 53], [53, 54], [56, 57], [56, 77], [57, 61], [67, 68], [67, 72], [68, 69], [68, 70], [70, 71], [72, 73], [72, 75]]}

import pytest
from unittest.mock import MagicMock, patch

# Mocking necessary components
@pytest.fixture
def mock_loader():
    return MagicMock()

@pytest.fixture
def mock_vars_loader():
    with patch('ansible.vars.plugins.vars_loader') as mock:
        yield mock

@pytest.fixture
def mock_C():
    with patch('ansible.vars.plugins.C') as mock:
        yield mock

@pytest.fixture
def mock_AnsibleCollectionRef():
    with patch('ansible.vars.plugins.AnsibleCollectionRef') as mock:
        yield mock

@pytest.fixture
def mock_combine_vars():
    with patch('ansible.vars.plugins.combine_vars') as mock:
        yield mock

@pytest.fixture
def mock_get_plugin_vars():
    with patch('ansible.vars.plugins.get_plugin_vars') as mock:
        yield mock

def test_get_vars_from_path_all_branches(mock_loader, mock_vars_loader, mock_C, mock_AnsibleCollectionRef, mock_combine_vars, mock_get_plugin_vars):
    from ansible.vars.plugins import get_vars_from_path

    # Setup mocks
    mock_C.VARIABLE_PLUGINS_ENABLED = ['plugin1', 'plugin2']
    mock_C.RUN_VARS_PLUGINS = 'demand'
    mock_AnsibleCollectionRef.is_valid_fqcr.side_effect = lambda x: x == 'plugin1'
    mock_vars_loader.all.return_value = []
    mock_vars_loader.get.side_effect = lambda x: MagicMock(_load_name=x, get_option=lambda y: None if y == 'stage' else 'value', has_option=lambda y: y == 'stage')

    # Test case 1: plugin is None
    mock_vars_loader.get.side_effect = lambda x: None if x == 'plugin1' else MagicMock(_load_name=x, get_option=lambda y: None if y == 'stage' else 'value', has_option=lambda y: y == 'stage')
    result = get_vars_from_path(mock_loader, 'path', 'entities', 'inventory')
    assert result == {}

    # Test case 2: plugin not in vars_plugin_list
    mock_vars_loader.get.side_effect = lambda x: MagicMock(_load_name=x, get_option=lambda y: None if y == 'stage' else 'value', has_option=lambda y: y == 'stage')
    result = get_vars_from_path(mock_loader, 'path', 'entities', 'inventory')
    assert result == {}

    # Test case 3: plugin requires whitelisting
    mock_vars_loader.get.side_effect = lambda x: MagicMock(_load_name=x, REQUIRES_WHITELIST=True, get_option=lambda y: None if y == 'stage' else 'value', has_option=lambda y: y == 'stage')
    result = get_vars_from_path(mock_loader, 'path', 'entities', 'inventory')
    assert result == {}

    # Test case 4: use_global is True and stage is 'inventory'
    mock_vars_loader.get.side_effect = lambda x: MagicMock(_load_name=x, get_option=lambda y: None if y == 'stage' else 'value', has_option=lambda y: y == 'stage')
    result = get_vars_from_path(mock_loader, 'path', 'entities', 'inventory')
    assert result == {}

    # Test case 5: use_global is True and stage is 'task'
    mock_C.RUN_VARS_PLUGINS = 'start'
    result = get_vars_from_path(mock_loader, 'path', 'entities', 'task')
    assert result == {}

    # Test case 6: use_global is False and plugin.get_option('stage') not in ('all', stage)
    mock_vars_loader.get.side_effect = lambda x: MagicMock(_load_name=x, get_option=lambda y: 'other' if y == 'stage' else 'value', has_option=lambda y: y == 'stage')
    result = get_vars_from_path(mock_loader, 'path', 'entities', 'inventory')
    assert result == {}

    # Test case 7: combine_vars and get_plugin_vars are called
    mock_vars_loader.get.side_effect = lambda x: MagicMock(_load_name=x, get_option=lambda y: 'all' if y == 'stage' else 'value', has_option=lambda y: y == 'stage')
    mock_combine_vars.return_value = {'key': 'value'}
    mock_get_plugin_vars.return_value = {'key': 'value'}
    result = get_vars_from_path(mock_loader, 'path', 'entities', 'inventory')
    assert result == {'key': 'value'}
    mock_combine_vars.assert_called()
    mock_get_plugin_vars.assert_called()
