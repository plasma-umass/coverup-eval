# file lib/ansible/cli/doc.py:63-71
# lines [66, 67, 68, 69, 70, 71]
# branches ['67->exit', '67->68']

import pytest
from unittest.mock import patch, MagicMock
from ansible.cli.doc import add_collection_plugins

@pytest.fixture
def mock_list_collection_dirs():
    with patch('ansible.cli.doc.list_collection_dirs') as mock:
        yield mock

@pytest.fixture
def mock_to_text():
    with patch('ansible.cli.doc.to_text') as mock:
        yield mock

@pytest.fixture
def mock_get_collection_name_from_path():
    with patch('ansible.cli.doc._get_collection_name_from_path') as mock:
        yield mock

@pytest.fixture
def mock_find_plugins():
    with patch('ansible.cli.doc.DocCLI.find_plugins') as mock:
        yield mock

def test_add_collection_plugins(mock_list_collection_dirs, mock_to_text, mock_get_collection_name_from_path, mock_find_plugins):
    # Setup mocks
    mock_list_collection_dirs.return_value = ['/fake/path']
    mock_to_text.return_value = '/fake/path'
    mock_get_collection_name_from_path.return_value = 'fake_collection'
    mock_find_plugins.return_value = {'plugin1': 'details1'}

    plugin_list = {}
    plugin_type = 'fake_type'
    coll_filter = None

    add_collection_plugins(plugin_list, plugin_type, coll_filter)

    # Assertions
    mock_list_collection_dirs.assert_called_once_with(coll_filter=coll_filter)
    mock_to_text.assert_called_once_with('/fake/path', errors='surrogate_or_strict')
    mock_get_collection_name_from_path.assert_called_once_with('/fake/path')
    mock_find_plugins.assert_called_once_with('/fake/path/plugins/fake_type', False, plugin_type, collection='fake_collection')
    assert plugin_list == {'plugin1': 'details1'}
