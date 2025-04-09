# file: lib/ansible/plugins/loader.py:1113-1129
# asked: {"lines": [1120, 1121, 1122, 1123, 1124, 1125, 1126, 1127, 1128, 1129], "branches": [[1119, 1120], [1122, 1123], [1122, 1124], [1124, 0], [1124, 1125]]}
# gained: {"lines": [1120, 1121, 1122, 1123, 1124, 1125, 1126, 1127, 1128, 1129], "branches": [[1119, 1120], [1122, 1123], [1122, 1124], [1124, 1125]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.plugins.loader import _on_collection_load_handler, AnsibleCollectionUnsupportedVersionError, display, C
from ansible.errors import AnsibleError

@pytest.fixture
def mock_display(mocker):
    return mocker.patch('ansible.plugins.loader.display')

@pytest.fixture
def mock_config(mocker):
    return mocker.patch('ansible.plugins.loader.C.config.get_config_value')

@pytest.fixture
def mock_get_collection_metadata(mocker):
    return mocker.patch('ansible.plugins.loader._get_collection_metadata')

@pytest.fixture
def mock_does_collection_support_ansible_version(mocker):
    return mocker.patch('ansible.plugins.loader._does_collection_support_ansible_version')

@pytest.fixture
def mock_ansible_version(mocker):
    return mocker.patch('ansible.plugins.loader.ansible_version', '2.9')

def test_collection_version_mismatch_warning(mock_display, mock_config, mock_get_collection_metadata, mock_does_collection_support_ansible_version, mock_ansible_version):
    mock_get_collection_metadata.return_value = {'requires_ansible': '2.9'}
    mock_does_collection_support_ansible_version.return_value = False
    mock_config.return_value = 'warning'
    
    _on_collection_load_handler('test_collection', '/path/to/collection')
    
    mock_display.warning.assert_called_once_with('Collection test_collection does not support Ansible version 2.9')

def test_collection_version_mismatch_error(mock_display, mock_config, mock_get_collection_metadata, mock_does_collection_support_ansible_version, mock_ansible_version):
    mock_get_collection_metadata.return_value = {'requires_ansible': '2.9'}
    mock_does_collection_support_ansible_version.return_value = False
    mock_config.return_value = 'error'
    
    with pytest.raises(AnsibleCollectionUnsupportedVersionError, match='Collection test_collection does not support Ansible version 2.9'):
        _on_collection_load_handler('test_collection', '/path/to/collection')

def test_collection_version_mismatch_exception(mock_display, mock_config, mock_get_collection_metadata, mock_does_collection_support_ansible_version, mock_ansible_version):
    mock_get_collection_metadata.return_value = {'requires_ansible': '2.9'}
    mock_does_collection_support_ansible_version.side_effect = Exception('test exception')
    
    _on_collection_load_handler('test_collection', '/path/to/collection')
    
    mock_display.warning.assert_called_once_with('Error parsing collection metadata requires_ansible value from collection test_collection: test exception')

def test_collection_version_mismatch_ansible_error(mock_display, mock_config, mock_get_collection_metadata, mock_does_collection_support_ansible_version, mock_ansible_version):
    mock_get_collection_metadata.return_value = {'requires_ansible': '2.9'}
    mock_does_collection_support_ansible_version.side_effect = AnsibleError('test ansible error')
    
    with pytest.raises(AnsibleError, match='test ansible error'):
        _on_collection_load_handler('test_collection', '/path/to/collection')
