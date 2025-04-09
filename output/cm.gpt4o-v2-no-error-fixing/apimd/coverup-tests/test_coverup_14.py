# file: apimd/loader.py:36-41
# asked: {"lines": [36, 38, 39, 40, 41], "branches": [[39, 40], [39, 41]]}
# gained: {"lines": [36, 38, 39, 40, 41], "branches": [[39, 40], [39, 41]]}

import pytest
from unittest.mock import patch, MagicMock
from apimd.loader import _site_path

@patch('apimd.loader.find_spec')
def test_site_path_exists(mock_find_spec):
    # Mock the return value of find_spec to simulate a module with submodule_search_locations
    mock_spec = MagicMock()
    mock_spec.submodule_search_locations = ['/path/to/site-packages/module']
    mock_find_spec.return_value = mock_spec

    result = _site_path('module')
    assert result == '/path/to/site-packages'

@patch('apimd.loader.find_spec')
def test_site_path_not_exists(mock_find_spec):
    # Mock the return value of find_spec to simulate a module not found
    mock_find_spec.return_value = None

    result = _site_path('non_existent_module')
    assert result == ''

@patch('apimd.loader.find_spec')
def test_site_path_no_submodule_search_locations(mock_find_spec):
    # Mock the return value of find_spec to simulate a module without submodule_search_locations
    mock_spec = MagicMock()
    mock_spec.submodule_search_locations = None
    mock_find_spec.return_value = mock_spec

    result = _site_path('module_without_submodule_search_locations')
    assert result == ''
