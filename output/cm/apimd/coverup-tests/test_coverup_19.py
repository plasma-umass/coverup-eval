# file apimd/loader.py:36-41
# lines [36, 38, 39, 40, 41]
# branches ['39->40', '39->41']

import os
import pytest
from unittest.mock import patch, MagicMock
from apimd.loader import _site_path
from os.path import dirname

def test_site_path_not_found():
    with patch('apimd.loader.find_spec') as mock_find_spec:
        mock_find_spec.return_value = None
        assert _site_path('nonexistent_package') == ""

def test_site_path_without_submodule_search_locations():
    with patch('apimd.loader.find_spec') as mock_find_spec:
        mock_spec = MagicMock(submodule_search_locations=None)
        mock_find_spec.return_value = mock_spec
        assert _site_path('package_without_submodule_search_locations') == ""

def test_site_path_with_submodule_search_locations(tmpdir):
    package_name = 'existent_package'
    package_dir = tmpdir.mkdir(package_name)
    with patch('apimd.loader.find_spec') as mock_find_spec:
        mock_spec = MagicMock(submodule_search_locations=[str(package_dir)])
        mock_find_spec.return_value = mock_spec
        expected_path = dirname(str(package_dir))
        assert _site_path(package_name) == expected_path
