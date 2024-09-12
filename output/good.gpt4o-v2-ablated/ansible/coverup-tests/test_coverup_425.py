# file: lib/ansible/utils/collection_loader/_collection_finder.py:659-691
# asked: {"lines": [668, 674, 685, 686, 689, 690, 691], "branches": [[667, 668], [673, 674], [676, 0], [685, 686], [685, 689]]}
# gained: {"lines": [668, 674, 685, 686, 689, 690, 691], "branches": [[667, 668], [673, 674], [676, 0], [685, 686], [685, 689]]}

import pytest
from unittest.mock import patch, MagicMock
import sys

# Assuming _get_collection_metadata and _nested_dict_get are imported from the appropriate module
from ansible.utils.collection_loader._collection_finder import _AnsibleInternalRedirectLoader

@pytest.fixture
def mock_get_collection_metadata(monkeypatch):
    mock = MagicMock()
    monkeypatch.setattr('ansible.utils.collection_loader._collection_finder._get_collection_metadata', mock)
    return mock

@pytest.fixture
def mock_nested_dict_get(monkeypatch):
    mock = MagicMock()
    monkeypatch.setattr('ansible.utils.collection_loader._collection_finder._nested_dict_get', mock)
    return mock

def test_init_not_ansible():
    with pytest.raises(ImportError, match='not interested'):
        _AnsibleInternalRedirectLoader('not.ansible.module', [])

def test_init_no_redirect(mock_get_collection_metadata, mock_nested_dict_get):
    mock_get_collection_metadata.return_value = {}
    mock_nested_dict_get.return_value = None

    with pytest.raises(ImportError, match='not redirected, go ask path_hook'):
        _AnsibleInternalRedirectLoader('ansible.module', [])

def test_init_with_redirect(mock_get_collection_metadata, mock_nested_dict_get):
    mock_get_collection_metadata.return_value = {'import_redirection': {'ansible.module': {'redirect': 'redirect.module'}}}
    mock_nested_dict_get.return_value = {'redirect': 'redirect.module'}

    loader = _AnsibleInternalRedirectLoader('ansible.module', [])
    assert loader._redirect == 'redirect.module'

def test_load_module_no_redirect():
    loader = _AnsibleInternalRedirectLoader.__new__(_AnsibleInternalRedirectLoader)
    loader._redirect = None

    with pytest.raises(ValueError, match='no redirect found for ansible.module'):
        loader.load_module('ansible.module')

@patch('ansible.utils.collection_loader._collection_finder.import_module')
def test_load_module_with_redirect(mock_import_module):
    mock_module = MagicMock()
    mock_import_module.return_value = mock_module

    loader = _AnsibleInternalRedirectLoader.__new__(_AnsibleInternalRedirectLoader)
    loader._redirect = 'redirect.module'

    fullname = 'ansible.module'
    result = loader.load_module(fullname)

    mock_import_module.assert_called_once_with('redirect.module')
    assert sys.modules[fullname] == mock_module
    assert result == mock_module

    # Clean up sys.modules to avoid state pollution
    del sys.modules[fullname]
