# file: apimd/loader.py:36-41
# asked: {"lines": [36, 38, 39, 40, 41], "branches": [[39, 40], [39, 41]]}
# gained: {"lines": [36, 38, 39, 40, 41], "branches": [[39, 40], [39, 41]]}

import pytest
from unittest.mock import patch
from apimd.loader import _site_path

def test_site_path_module_found(monkeypatch):
    mock_spec = type('MockSpec', (object,), {'submodule_search_locations': ['/mock/path']})
    monkeypatch.setattr('apimd.loader.find_spec', lambda name: mock_spec)
    
    result = _site_path('mock_module')
    assert result == '/mock'

def test_site_path_module_not_found(monkeypatch):
    monkeypatch.setattr('apimd.loader.find_spec', lambda name: None)
    
    result = _site_path('non_existent_module')
    assert result == ''

def test_site_path_no_submodule_search_locations(monkeypatch):
    mock_spec = type('MockSpec', (object,), {'submodule_search_locations': None})
    monkeypatch.setattr('apimd.loader.find_spec', lambda name: mock_spec)
    
    result = _site_path('module_without_submodule_search_locations')
    assert result == ''
