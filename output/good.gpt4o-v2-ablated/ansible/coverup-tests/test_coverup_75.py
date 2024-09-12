# file: lib/ansible/vars/plugins.py:80-95
# asked: {"lines": [80, 82, 83, 85, 86, 87, 88, 89, 91, 93, 95], "branches": [[83, 85], [83, 95], [85, 86], [85, 87], [87, 88], [87, 89], [89, 91], [89, 93]]}
# gained: {"lines": [80, 82, 83, 85, 86, 87, 89, 91, 93, 95], "branches": [[83, 85], [83, 95], [85, 86], [85, 87], [87, 89], [89, 91]]}

import os
import pytest
from unittest.mock import MagicMock, patch

# Assuming combine_vars and get_vars_from_path are imported from ansible/vars/plugins.py
from ansible.vars.plugins import combine_vars, get_vars_from_path, get_vars_from_inventory_sources

@pytest.fixture
def mock_loader():
    return MagicMock()

@pytest.fixture
def mock_combine_vars(mocker):
    return mocker.patch('ansible.vars.plugins.combine_vars', side_effect=lambda x, y: {**x, **y})

@pytest.fixture
def mock_get_vars_from_path(mocker):
    return mocker.patch('ansible.vars.plugins.get_vars_from_path', return_value={'key': 'value'})

def test_get_vars_from_inventory_sources_all_branches(mock_loader, mock_combine_vars, mock_get_vars_from_path, mocker):
    sources = [None, 'host1,host2', '/non/existent/path', '/valid/path/file']
    entities = MagicMock()
    stage = MagicMock()

    mocker.patch('os.path.exists', side_effect=lambda x: x != '/non/existent/path')
    mocker.patch('os.path.isdir', side_effect=lambda x: x == b'/valid/path')

    result = get_vars_from_inventory_sources(mock_loader, sources, entities, stage)

    assert result == {'key': 'value'}
    mock_combine_vars.assert_called()
    mock_get_vars_from_path.assert_called()

def test_get_vars_from_inventory_sources_cleanup(mock_loader, mock_combine_vars, mock_get_vars_from_path, mocker):
    sources = ['/another/valid/path/file']
    entities = MagicMock()
    stage = MagicMock()

    mocker.patch('os.path.exists', return_value=True)
    mocker.patch('os.path.isdir', return_value=False)
    mocker.patch('os.path.dirname', return_value='/another/valid/path')

    result = get_vars_from_inventory_sources(mock_loader, sources, entities, stage)

    assert result == {'key': 'value'}
    mock_combine_vars.assert_called_once()
    mock_get_vars_from_path.assert_called_once_with(mock_loader, '/another/valid/path', entities, stage)
