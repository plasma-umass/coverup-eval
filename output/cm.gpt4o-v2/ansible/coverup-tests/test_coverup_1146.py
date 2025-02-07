# file: lib/ansible/utils/collection_loader/_collection_finder.py:952-991
# asked: {"lines": [968, 971, 972, 974, 976, 978, 979, 980, 985, 987, 988, 989, 991], "branches": [[965, 968], [971, 972], [971, 974], [988, 989], [988, 991]]}
# gained: {"lines": [968, 971, 972, 974, 976, 978, 979, 980, 985, 987, 988, 989, 991], "branches": [[965, 968], [971, 972], [971, 974], [988, 989], [988, 991]]}

import pytest
import os
from unittest.mock import patch, MagicMock
from ansible.utils.collection_loader._collection_finder import _get_collection_name_from_path

@pytest.fixture
def mock_import_module():
    with patch('ansible.utils.collection_loader._collection_finder.import_module') as mock:
        yield mock

@pytest.fixture
def mock_to_native():
    with patch('ansible.utils.collection_loader._collection_finder.to_native', side_effect=lambda x: x):
        yield

@pytest.fixture
def mock_to_bytes():
    with patch('ansible.utils.collection_loader._collection_finder.to_bytes', side_effect=lambda x: x):
        yield

def test_get_collection_name_from_path_valid(mock_import_module, mock_to_native, mock_to_bytes):
    mock_import_module.return_value.__file__ = '/ansible_collections/namespace/collection/__init__.py'
    path = '/ansible_collections/namespace/collection/plugins/module.py'
    result = _get_collection_name_from_path(path)
    assert result == 'namespace.collection'

def test_get_collection_name_from_path_no_ansible_collections(mock_to_native, mock_to_bytes):
    path = '/some/other/path/plugins/module.py'
    result = _get_collection_name_from_path(path)
    assert result is None

def test_get_collection_name_from_path_too_short(mock_to_native, mock_to_bytes):
    path = '/ansible_collections/namespace'
    result = _get_collection_name_from_path(path)
    assert result is None

def test_get_collection_name_from_path_import_error(mock_import_module, mock_to_native, mock_to_bytes):
    mock_import_module.side_effect = ImportError
    path = '/ansible_collections/namespace/collection/plugins/module.py'
    result = _get_collection_name_from_path(path)
    assert result is None

def test_get_collection_name_from_path_mismatch(mock_import_module, mock_to_native, mock_to_bytes):
    mock_import_module.return_value.__file__ = '/different/path/namespace/collection/__init__.py'
    path = '/ansible_collections/namespace/collection/plugins/module.py'
    result = _get_collection_name_from_path(path)
    assert result is None
