# file: apimd/loader.py:36-41
# asked: {"lines": [38, 39, 40, 41], "branches": [[39, 40], [39, 41]]}
# gained: {"lines": [38, 39, 40, 41], "branches": [[39, 40], [39, 41]]}

import pytest
from unittest.mock import patch, MagicMock
from apimd.loader import _site_path

def test_site_path_module_found():
    with patch('apimd.loader.find_spec') as mock_find_spec:
        mock_spec = MagicMock()
        mock_spec.submodule_search_locations = ['/path/to/module']
        mock_find_spec.return_value = mock_spec

        result = _site_path('existing_module')
        assert result == '/path/to'

def test_site_path_module_not_found():
    with patch('apimd.loader.find_spec') as mock_find_spec:
        mock_find_spec.return_value = None

        result = _site_path('non_existing_module')
        assert result == ''

def test_site_path_no_submodule_search_locations():
    with patch('apimd.loader.find_spec') as mock_find_spec:
        mock_spec = MagicMock()
        mock_spec.submodule_search_locations = None
        mock_find_spec.return_value = mock_spec

        result = _site_path('module_without_submodule_search_locations')
        assert result == ''
