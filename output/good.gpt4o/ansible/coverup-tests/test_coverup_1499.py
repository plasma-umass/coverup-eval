# file lib/ansible/vars/plugins.py:80-95
# lines []
# branches ['89->93']

import os
import pytest
from unittest import mock
from ansible.vars.plugins import get_vars_from_inventory_sources

@pytest.fixture
def mock_loader():
    return mock.Mock()

@pytest.fixture
def mock_entities():
    return mock.Mock()

@pytest.fixture
def mock_stage():
    return mock.Mock()

@pytest.fixture
def mock_combine_vars(mocker):
    return mocker.patch('ansible.vars.plugins.combine_vars', return_value={})

@pytest.fixture
def mock_get_vars_from_path(mocker):
    return mocker.patch('ansible.vars.plugins.get_vars_from_path', return_value={})

def test_get_vars_from_inventory_sources_directory_not_exist(mock_loader, mock_entities, mock_stage, mock_combine_vars, mock_get_vars_from_path, mocker):
    sources = ['/nonexistent_directory']
    mocker.patch('os.path.isdir', return_value=False)
    mocker.patch('os.path.exists', return_value=True)
    mocker.patch('os.path.dirname', return_value='/')

    result = get_vars_from_inventory_sources(mock_loader, sources, mock_entities, mock_stage)

    assert result == {}
    mock_combine_vars.assert_called_once()
    mock_get_vars_from_path.assert_called_once_with(mock_loader, '/', mock_entities, mock_stage)

def test_get_vars_from_inventory_sources_directory_exists(mock_loader, mock_entities, mock_stage, mock_combine_vars, mock_get_vars_from_path, mocker):
    sources = ['/existent_directory']
    mocker.patch('os.path.isdir', return_value=True)
    mocker.patch('os.path.exists', return_value=True)

    result = get_vars_from_inventory_sources(mock_loader, sources, mock_entities, mock_stage)

    assert result == {}
    mock_combine_vars.assert_called_once()
    mock_get_vars_from_path.assert_called_once_with(mock_loader, '/existent_directory', mock_entities, mock_stage)
