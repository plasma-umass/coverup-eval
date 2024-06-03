# file lib/ansible/utils/collection_loader/_collection_finder.py:1051-1066
# lines [1051, 1052, 1053, 1054, 1056, 1057, 1058, 1059, 1061, 1063, 1064, 1066]
# branches ['1053->1054', '1053->1056', '1063->1064', '1063->1066']

import pytest
from unittest.mock import patch, MagicMock

# Assuming the function is a standalone function in the module
from ansible.utils.collection_loader._collection_finder import _get_collection_metadata

def test_get_collection_metadata_invalid_name():
    with pytest.raises(ValueError, match='collection_name must be a non-empty string of the form namespace.collection'):
        _get_collection_metadata('invalidname')

def test_get_collection_metadata_import_error():
    with patch('ansible.utils.collection_loader._collection_finder.import_module', side_effect=ImportError):
        with pytest.raises(ValueError, match='unable to locate collection invalid.namespace'):
            _get_collection_metadata('invalid.namespace')

def test_get_collection_metadata_no_meta():
    mock_collection_pkg = MagicMock()
    del mock_collection_pkg._collection_meta
    with patch('ansible.utils.collection_loader._collection_finder.import_module', return_value=mock_collection_pkg):
        with pytest.raises(ValueError, match='collection metadata was not loaded for collection valid.namespace'):
            _get_collection_metadata('valid.namespace')

def test_get_collection_metadata_success():
    mock_collection_meta = {'key': 'value'}
    mock_collection_pkg = MagicMock(_collection_meta=mock_collection_meta)
    with patch('ansible.utils.collection_loader._collection_finder.import_module', return_value=mock_collection_pkg):
        result = _get_collection_metadata('valid.namespace')
        assert result == mock_collection_meta
