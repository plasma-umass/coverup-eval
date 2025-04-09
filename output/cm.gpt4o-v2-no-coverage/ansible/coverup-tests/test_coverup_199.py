# file: lib/ansible/plugins/loader.py:1113-1129
# asked: {"lines": [1113, 1114, 1116, 1118, 1119, 1120, 1121, 1122, 1123, 1124, 1125, 1126, 1127, 1128, 1129], "branches": [[1119, 0], [1119, 1120], [1122, 1123], [1122, 1124], [1124, 0], [1124, 1125]]}
# gained: {"lines": [1113, 1114, 1116, 1118, 1119, 1120, 1121, 1122, 1123, 1124, 1125, 1126, 1127, 1128, 1129], "branches": [[1119, 0], [1119, 1120], [1122, 1123], [1122, 1124], [1124, 1125]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.errors import AnsibleError, AnsibleCollectionUnsupportedVersionError
from ansible.plugins.loader import _on_collection_load_handler

@pytest.fixture
def mock_display():
    with patch('ansible.plugins.loader.display') as mock_display:
        yield mock_display

@pytest.fixture
def mock_get_collection_metadata():
    with patch('ansible.plugins.loader._get_collection_metadata') as mock_get_collection_metadata:
        yield mock_get_collection_metadata

@pytest.fixture
def mock_does_collection_support_ansible_version():
    with patch('ansible.plugins.loader._does_collection_support_ansible_version') as mock_does_collection_support_ansible_version:
        yield mock_does_collection_support_ansible_version

@pytest.fixture
def mock_config():
    with patch('ansible.plugins.loader.C.config.get_config_value') as mock_config:
        yield mock_config

@pytest.fixture
def mock_ansible_version():
    with patch('ansible.plugins.loader.ansible_version', '2.9'):
        yield

def test_on_collection_load_handler_warning(mock_display, mock_get_collection_metadata, mock_does_collection_support_ansible_version, mock_config, mock_ansible_version):
    mock_get_collection_metadata.return_value = {'requires_ansible': '>=2.9'}
    mock_does_collection_support_ansible_version.return_value = False
    mock_config.return_value = 'warning'

    _on_collection_load_handler('test_collection', '/path/to/collection')

    mock_display.vvvv.assert_called_once_with('Loading collection test_collection from /path/to/collection')
    mock_display.warning.assert_called_once_with('Collection test_collection does not support Ansible version 2.9')

def test_on_collection_load_handler_error(mock_display, mock_get_collection_metadata, mock_does_collection_support_ansible_version, mock_config, mock_ansible_version):
    mock_get_collection_metadata.return_value = {'requires_ansible': '>=2.9'}
    mock_does_collection_support_ansible_version.return_value = False
    mock_config.return_value = 'error'

    with pytest.raises(AnsibleCollectionUnsupportedVersionError, match='Collection test_collection does not support Ansible version 2.9'):
        _on_collection_load_handler('test_collection', '/path/to/collection')

    mock_display.vvvv.assert_called_once_with('Loading collection test_collection from /path/to/collection')

def test_on_collection_load_handler_exception(mock_display, mock_get_collection_metadata, mock_does_collection_support_ansible_version, mock_ansible_version):
    mock_get_collection_metadata.return_value = {'requires_ansible': '>=2.9'}
    mock_does_collection_support_ansible_version.side_effect = Exception('Test exception')

    _on_collection_load_handler('test_collection', '/path/to/collection')

    mock_display.vvvv.assert_called_once_with('Loading collection test_collection from /path/to/collection')
    mock_display.warning.assert_called_once_with('Error parsing collection metadata requires_ansible value from collection test_collection: Test exception')

def test_on_collection_load_handler_no_requires_ansible(mock_display, mock_get_collection_metadata, mock_does_collection_support_ansible_version, mock_ansible_version):
    mock_get_collection_metadata.return_value = {}
    mock_does_collection_support_ansible_version.return_value = True

    _on_collection_load_handler('test_collection', '/path/to/collection')

    mock_display.vvvv.assert_called_once_with('Loading collection test_collection from /path/to/collection')
    mock_display.warning.assert_not_called()
