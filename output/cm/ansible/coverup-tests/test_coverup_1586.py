# file lib/ansible/plugins/loader.py:1113-1129
# lines [1120, 1121, 1122, 1123, 1124, 1125, 1126, 1127, 1128, 1129]
# branches ['1119->1120', '1122->1123', '1122->1124', '1124->exit', '1124->1125']

import pytest
from ansible.errors import AnsibleCollectionUnsupportedVersionError
from ansible.utils.display import Display
from ansible.plugins.loader import _on_collection_load_handler
from ansible import constants as C

# Mock the display object to capture output
@pytest.fixture
def mock_display(mocker):
    display_mock = mocker.MagicMock(spec=Display)
    mocker.patch('ansible.plugins.loader.display', new=display_mock)
    return display_mock

# Mock the _get_collection_metadata function
@pytest.fixture
def mock_get_collection_metadata(mocker):
    return mocker.patch('ansible.plugins.loader._get_collection_metadata')

# Mock the _does_collection_support_ansible_version function
@pytest.fixture
def mock_does_collection_support_ansible_version(mocker):
    return mocker.patch('ansible.plugins.loader._does_collection_support_ansible_version')

# Test function to cover lines 1120-1129
def test_on_collection_load_handler_version_mismatch(mock_display, mock_get_collection_metadata, mock_does_collection_support_ansible_version, mocker):
    collection_name = 'test.collection'
    collection_path = '/path/to/collection'
    ansible_version = '2.9.0'
    mock_get_collection_metadata.return_value = {'requires_ansible': '>=2.10'}
    mock_does_collection_support_ansible_version.return_value = False

    # Test with COLLECTIONS_ON_ANSIBLE_VERSION_MISMATCH set to 'warning'
    mocker.patch.object(C.config, 'get_config_value', return_value='warning')
    mocker.patch('ansible.plugins.loader.ansible_version', ansible_version)
    _on_collection_load_handler(collection_name, collection_path)
    mock_display.warning.assert_called_once_with('Collection test.collection does not support Ansible version 2.9.0')

    # Reset mock to clear previous call
    mock_display.reset_mock()

    # Test with COLLECTIONS_ON_ANSIBLE_VERSION_MISMATCH set to 'error'
    mocker.patch.object(C.config, 'get_config_value', return_value='error')
    with pytest.raises(AnsibleCollectionUnsupportedVersionError):
        _on_collection_load_handler(collection_name, collection_path)

    # Reset mock to clear previous call
    mock_display.reset_mock()

    # Test with an exception raised during version check
    mock_does_collection_support_ansible_version.side_effect = Exception('Invalid version format')
    mocker.patch.object(C.config, 'get_config_value', return_value='warning')
    _on_collection_load_handler(collection_name, collection_path)
    mock_display.warning.assert_called_with('Error parsing collection metadata requires_ansible value from collection test.collection: Invalid version format')
