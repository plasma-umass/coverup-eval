# file lib/ansible/utils/collection_loader/_collection_finder.py:1051-1066
# lines [1054, 1058, 1059, 1064]
# branches ['1053->1054', '1063->1064']

import pytest
from ansible.utils.collection_loader._collection_finder import _get_collection_metadata
from ansible.module_utils._text import to_native
from ansible.module_utils.six import string_types

def test_get_collection_metadata_invalid_name(mocker):
    with pytest.raises(ValueError) as excinfo:
        _get_collection_metadata('')
    assert "collection_name must be a non-empty string of the form namespace.collection" in str(excinfo.value)

    with pytest.raises(ValueError) as excinfo:
        _get_collection_metadata('invalid-collection-name')
    assert "collection_name must be a non-empty string of the form namespace.collection" in str(excinfo.value)

def test_get_collection_metadata_import_error(mocker):
    mocker.patch('ansible.utils.collection_loader._collection_finder.import_module', side_effect=ImportError)
    with pytest.raises(ValueError) as excinfo:
        _get_collection_metadata('namespace.collection')
    assert "unable to locate collection namespace.collection" in str(excinfo.value)

def test_get_collection_metadata_no_metadata(mocker):
    mock_module = mocker.MagicMock()
    mock_module._collection_meta = None
    mocker.patch('ansible.utils.collection_loader._collection_finder.import_module', return_value=mock_module)
    with pytest.raises(ValueError) as excinfo:
        _get_collection_metadata('namespace.collection')
    assert "collection metadata was not loaded for collection namespace.collection" in str(excinfo.value)
