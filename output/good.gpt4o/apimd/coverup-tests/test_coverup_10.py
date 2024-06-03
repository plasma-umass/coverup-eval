# file apimd/loader.py:36-41
# lines [36, 38, 39, 40, 41]
# branches ['39->40', '39->41']

import pytest
from unittest.mock import patch
from importlib.util import find_spec
from os.path import dirname

# Assuming the function _site_path is imported from apimd.loader
from apimd.loader import _site_path

def test_site_path_exists(mocker):
    # Mocking find_spec to return a mock object with submodule_search_locations
    mock_spec = mocker.Mock()
    mock_spec.submodule_search_locations = ["/mocked/path"]
    mocker.patch('apimd.loader.find_spec', return_value=mock_spec)
    
    result = _site_path("mocked_module")
    assert result == "/mocked", "The path should be '/mocked'"

def test_site_path_not_exists(mocker):
    # Mocking find_spec to return None
    mocker.patch('apimd.loader.find_spec', return_value=None)
    
    result = _site_path("non_existent_module")
    assert result == "", "The path should be an empty string when module does not exist"

def test_site_path_no_submodule_search_locations(mocker):
    # Mocking find_spec to return a mock object with submodule_search_locations as None
    mock_spec = mocker.Mock()
    mock_spec.submodule_search_locations = None
    mocker.patch('apimd.loader.find_spec', return_value=mock_spec)
    
    result = _site_path("module_without_submodule_search_locations")
    assert result == "", "The path should be an empty string when submodule_search_locations is None"
