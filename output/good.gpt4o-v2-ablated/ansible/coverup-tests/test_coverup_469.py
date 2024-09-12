# file: lib/ansible/vars/plugins.py:80-95
# asked: {"lines": [88], "branches": [[87, 88], [89, 93]]}
# gained: {"lines": [88], "branches": [[87, 88], [89, 93]]}

import os
import pytest
from unittest.mock import MagicMock, patch

# Assuming combine_vars and get_vars_from_path are imported from the appropriate module
from ansible.vars.plugins import combine_vars, get_vars_from_path
from ansible.vars.plugins import get_vars_from_inventory_sources

@pytest.fixture
def mock_loader():
    return MagicMock()

@pytest.fixture
def mock_combine_vars(mocker):
    return mocker.patch('ansible.vars.plugins.combine_vars', side_effect=lambda x, y: {**x, **y})

@pytest.fixture
def mock_get_vars_from_path(mocker):
    return mocker.patch('ansible.vars.plugins.get_vars_from_path', return_value={'key': 'value'})

def test_get_vars_from_inventory_sources_all_paths_none(mock_loader, mock_combine_vars, mock_get_vars_from_path):
    sources = [None, None]
    entities = []
    stage = 'test_stage'
    
    result = get_vars_from_inventory_sources(mock_loader, sources, entities, stage)
    
    assert result == {}
    mock_combine_vars.assert_not_called()
    mock_get_vars_from_path.assert_not_called()

def test_get_vars_from_inventory_sources_skip_host_lists(mock_loader, mock_combine_vars, mock_get_vars_from_path):
    sources = ['host1,host2']
    entities = []
    stage = 'test_stage'
    
    with patch('os.path.exists', return_value=False):
        result = get_vars_from_inventory_sources(mock_loader, sources, entities, stage)
    
    assert result == {}
    mock_combine_vars.assert_not_called()
    mock_get_vars_from_path.assert_not_called()

def test_get_vars_from_inventory_sources_not_directory(mock_loader, mock_combine_vars, mock_get_vars_from_path):
    sources = ['/fake/path/file']
    entities = []
    stage = 'test_stage'
    
    with patch('os.path.isdir', return_value=False):
        with patch('os.path.dirname', return_value='/fake/path'):
            result = get_vars_from_inventory_sources(mock_loader, sources, entities, stage)
    
    assert result == {'key': 'value'}
    mock_combine_vars.assert_called_once_with({}, {'key': 'value'})
    mock_get_vars_from_path.assert_called_once_with(mock_loader, '/fake/path', entities, stage)

def test_get_vars_from_inventory_sources_directory(mock_loader, mock_combine_vars, mock_get_vars_from_path):
    sources = ['/fake/path/dir']
    entities = []
    stage = 'test_stage'
    
    with patch('os.path.isdir', return_value=True):
        result = get_vars_from_inventory_sources(mock_loader, sources, entities, stage)
    
    assert result == {'key': 'value'}
    mock_combine_vars.assert_called_once_with({}, {'key': 'value'})
    mock_get_vars_from_path.assert_called_once_with(mock_loader, '/fake/path/dir', entities, stage)
