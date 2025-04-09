# file: apimd/loader.py:36-41
# asked: {"lines": [38, 39, 40, 41], "branches": [[39, 40], [39, 41]]}
# gained: {"lines": [38, 39, 40, 41], "branches": [[39, 40], [39, 41]]}

import pytest
from unittest.mock import patch, MagicMock
from apimd.loader import _site_path

@patch('apimd.loader.find_spec')
@patch('apimd.loader.dirname')
def test_site_path_exists(mock_dirname, mock_find_spec):
    # Mock the find_spec to return a mock object with submodule_search_locations
    mock_spec = MagicMock()
    mock_spec.submodule_search_locations = ['/mock/path']
    mock_find_spec.return_value = mock_spec

    # Mock the dirname to return a specific path
    mock_dirname.return_value = '/mock'

    result = _site_path('mock_module')
    assert result == '/mock'
    mock_find_spec.assert_called_once_with('mock_module')
    mock_dirname.assert_called_once_with('/mock/path')

@patch('apimd.loader.find_spec')
def test_site_path_no_spec(mock_find_spec):
    # Mock the find_spec to return None
    mock_find_spec.return_value = None

    result = _site_path('nonexistent_module')
    assert result == ''
    mock_find_spec.assert_called_once_with('nonexistent_module')

@patch('apimd.loader.find_spec')
def test_site_path_no_submodule_search_locations(mock_find_spec):
    # Mock the find_spec to return a mock object without submodule_search_locations
    mock_spec = MagicMock()
    mock_spec.submodule_search_locations = None
    mock_find_spec.return_value = mock_spec

    result = _site_path('module_without_submodule_search_locations')
    assert result == ''
    mock_find_spec.assert_called_once_with('module_without_submodule_search_locations')
