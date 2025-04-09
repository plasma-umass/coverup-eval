# file: lib/ansible/utils/collection_loader/_collection_finder.py:1051-1066
# asked: {"lines": [1054, 1058, 1059, 1064], "branches": [[1053, 1054], [1063, 1064]]}
# gained: {"lines": [1054, 1058, 1059, 1064], "branches": [[1053, 1054], [1063, 1064]]}

import pytest
from unittest.mock import patch, MagicMock

# Mocking the imports
from ansible.module_utils.common.text.converters import to_native
from ansible.module_utils.six import string_types
from importlib import import_module

# Assuming the function _get_collection_metadata is defined in the module ansible.utils.collection_loader._collection_finder
from ansible.utils.collection_loader._collection_finder import _get_collection_metadata

def test_get_collection_metadata_valid_collection(monkeypatch):
    # Mocking the import_module to return a mock collection package
    mock_collection_pkg = MagicMock()
    mock_collection_pkg._collection_meta = {'key': 'value'}
    
    def mock_import_module(name):
        return mock_collection_pkg
    
    monkeypatch.setattr('ansible.utils.collection_loader._collection_finder.import_module', mock_import_module)
    
    collection_name = 'namespace.collection'
    result = _get_collection_metadata(collection_name)
    
    assert result == {'key': 'value'}

def test_get_collection_metadata_invalid_format():
    with pytest.raises(ValueError, match='collection_name must be a non-empty string of the form namespace.collection'):
        _get_collection_metadata('invalid_collection_name')

def test_get_collection_metadata_import_error(monkeypatch):
    def mock_import_module(name):
        raise ImportError
    
    monkeypatch.setattr('ansible.utils.collection_loader._collection_finder.import_module', mock_import_module)
    
    with pytest.raises(ValueError, match='unable to locate collection namespace.collection'):
        _get_collection_metadata('namespace.collection')

def test_get_collection_metadata_no_metadata(monkeypatch):
    # Mocking the import_module to return a mock collection package without _collection_meta
    mock_collection_pkg = MagicMock()
    mock_collection_pkg._collection_meta = None
    
    def mock_import_module(name):
        return mock_collection_pkg
    
    monkeypatch.setattr('ansible.utils.collection_loader._collection_finder.import_module', mock_import_module)
    
    with pytest.raises(ValueError, match='collection metadata was not loaded for collection namespace.collection'):
        _get_collection_metadata('namespace.collection')
