# file: lib/ansible/plugins/loader.py:1113-1129
# asked: {"lines": [1120, 1121, 1122, 1123, 1124, 1125, 1126, 1127, 1128, 1129], "branches": [[1119, 1120], [1122, 1123], [1122, 1124], [1124, 0], [1124, 1125]]}
# gained: {"lines": [1120, 1121, 1122, 1123, 1124, 1125, 1126, 1127, 1128, 1129], "branches": [[1119, 1120], [1122, 1123], [1122, 1124], [1124, 1125]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.errors import AnsibleCollectionUnsupportedVersionError
from ansible.plugins.loader import _on_collection_load_handler

@pytest.fixture
def mock_collection_metadata():
    with patch('ansible.plugins.loader._get_collection_metadata') as mock:
        yield mock

@pytest.fixture
def mock_ansible_version():
    with patch('ansible.plugins.loader.ansible_version', '2.10.0'):
        yield

@pytest.fixture
def mock_config():
    with patch('ansible.plugins.loader.C.config.get_config_value') as mock:
        yield mock

@pytest.fixture
def mock_display():
    with patch('ansible.plugins.loader.display') as mock:
        yield mock

@pytest.fixture
def mock_does_collection_support_ansible_version():
    with patch('ansible.plugins.loader._does_collection_support_ansible_version') as mock:
        yield mock

def test_on_collection_load_handler_warning(mock_collection_metadata, mock_ansible_version, mock_config, mock_display, mock_does_collection_support_ansible_version):
    mock_collection_metadata.return_value = {'requires_ansible': '>=2.9.0'}
    mock_config.return_value = 'warning'
    mock_does_collection_support_ansible_version.return_value = False

    _on_collection_load_handler('test_collection', '/path/to/collection')

    mock_display.warning.assert_called_once_with('Collection test_collection does not support Ansible version 2.10.0')

def test_on_collection_load_handler_error(mock_collection_metadata, mock_ansible_version, mock_config, mock_does_collection_support_ansible_version):
    mock_collection_metadata.return_value = {'requires_ansible': '>=2.9.0'}
    mock_config.return_value = 'error'
    mock_does_collection_support_ansible_version.return_value = False

    with pytest.raises(AnsibleCollectionUnsupportedVersionError, match='Collection test_collection does not support Ansible version 2.10.0'):
        _on_collection_load_handler('test_collection', '/path/to/collection')

def test_on_collection_load_handler_exception(mock_collection_metadata, mock_ansible_version, mock_config, mock_display, mock_does_collection_support_ansible_version):
    mock_collection_metadata.return_value = {'requires_ansible': '>=2.9.0'}
    mock_does_collection_support_ansible_version.side_effect = Exception('Test Exception')

    _on_collection_load_handler('test_collection', '/path/to/collection')

    mock_display.warning.assert_called_once_with('Error parsing collection metadata requires_ansible value from collection test_collection: Test Exception')
