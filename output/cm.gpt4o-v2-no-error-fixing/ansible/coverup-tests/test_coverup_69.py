# file: lib/ansible/utils/collection_loader/_collection_finder.py:952-991
# asked: {"lines": [952, 962, 964, 965, 966, 968, 971, 972, 974, 976, 978, 979, 980, 985, 987, 988, 989, 991], "branches": [[965, 966], [965, 968], [971, 972], [971, 974], [988, 989], [988, 991]]}
# gained: {"lines": [952, 962, 964, 965, 966, 968, 971, 972, 974, 976, 978, 979, 980, 985, 987, 988, 989, 991], "branches": [[965, 966], [965, 968], [971, 972], [971, 974], [988, 989], [988, 991]]}

import pytest
import os
from unittest.mock import patch, MagicMock
from ansible.utils.collection_loader._collection_finder import _get_collection_name_from_path

@pytest.fixture
def mock_import_module():
    with patch('ansible.utils.collection_loader._collection_finder.import_module') as mock_import:
        yield mock_import

def test_get_collection_name_from_path_valid_collection(mock_import_module):
    mock_module = MagicMock()
    mock_module.__file__ = '/abs/path/to/ansible_collections/namespace/collection/__init__.py'
    mock_import_module.return_value = mock_module

    path = '/abs/path/to/ansible_collections/namespace/collection/plugins/module.py'
    result = _get_collection_name_from_path(path)
    assert result == 'namespace.collection'

def test_get_collection_name_from_path_no_ansible_collections():
    path = '/abs/path/to/some/other/path/plugins/module.py'
    result = _get_collection_name_from_path(path)
    assert result is None

def test_get_collection_name_from_path_multiple_ansible_collections():
    path = '/abs/path/to/ansible_collections/namespace/ansible_collections/collection/plugins/module.py'
    result = _get_collection_name_from_path(path)
    assert result is None

def test_get_collection_name_from_path_too_short():
    path = '/abs/path/to/ansible_collections/namespace'
    result = _get_collection_name_from_path(path)
    assert result is None

def test_get_collection_name_from_path_import_error(mock_import_module):
    mock_import_module.side_effect = ImportError
    path = '/abs/path/to/ansible_collections/namespace/collection/plugins/module.py'
    result = _get_collection_name_from_path(path)
    assert result is None

def test_get_collection_name_from_path_mismatched_paths(mock_import_module):
    mock_module = MagicMock()
    mock_module.__file__ = '/different/path/to/ansible_collections/namespace/collection/__init__.py'
    mock_import_module.return_value = mock_module

    path = '/abs/path/to/ansible_collections/namespace/collection/plugins/module.py'
    result = _get_collection_name_from_path(path)
    assert result is None
