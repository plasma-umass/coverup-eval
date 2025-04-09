# file: lib/ansible/utils/collection_loader/_collection_finder.py:1051-1066
# asked: {"lines": [1051, 1052, 1053, 1054, 1056, 1057, 1058, 1059, 1061, 1063, 1064, 1066], "branches": [[1053, 1054], [1053, 1056], [1063, 1064], [1063, 1066]]}
# gained: {"lines": [1051, 1052, 1053, 1054, 1056, 1057, 1058, 1059, 1061, 1063, 1064, 1066], "branches": [[1053, 1054], [1053, 1056], [1063, 1064], [1063, 1066]]}

import pytest
from unittest.mock import patch, MagicMock

# Assuming the function is part of a module named `collection_loader`
from ansible.utils.collection_loader._collection_finder import _get_collection_metadata

def test_get_collection_metadata_valid(monkeypatch):
    mock_meta = {'name': 'test_collection'}
    mock_collection_pkg = MagicMock()
    mock_collection_pkg._collection_meta = mock_meta

    def mock_import_module(name):
        return mock_collection_pkg

    monkeypatch.setattr('ansible.utils.collection_loader._collection_finder.import_module', mock_import_module)

    result = _get_collection_metadata('namespace.collection')
    assert result == mock_meta

def test_get_collection_metadata_invalid_name():
    with pytest.raises(ValueError, match='collection_name must be a non-empty string of the form namespace.collection'):
        _get_collection_metadata('invalid_collection_name')

def test_get_collection_metadata_import_error(monkeypatch):
    def mock_import_module(name):
        raise ImportError

    monkeypatch.setattr('ansible.utils.collection_loader._collection_finder.import_module', mock_import_module)

    with pytest.raises(ValueError, match='unable to locate collection namespace.collection'):
        _get_collection_metadata('namespace.collection')

def test_get_collection_metadata_no_meta(monkeypatch):
    mock_collection_pkg = MagicMock()
    mock_collection_pkg._collection_meta = None

    def mock_import_module(name):
        return mock_collection_pkg

    monkeypatch.setattr('ansible.utils.collection_loader._collection_finder.import_module', mock_import_module)

    with pytest.raises(ValueError, match='collection metadata was not loaded for collection namespace.collection'):
        _get_collection_metadata('namespace.collection')
