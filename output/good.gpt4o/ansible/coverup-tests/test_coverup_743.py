# file lib/ansible/modules/apt_repository.py:413-415
# lines [413, 414, 415]
# branches []

import pytest
from unittest import mock

# Assuming the SourcesList class is imported from ansible.modules.apt_repository
from ansible.modules.apt_repository import SourcesList

@pytest.fixture
def sources_list(mocker):
    # Mock the module argument required by SourcesList
    mock_module = mocker.Mock()
    
    # Mock the apt_pkg module and its config attribute
    mock_apt_pkg = mocker.patch('ansible.modules.apt_repository.apt_pkg', autospec=True)
    mock_apt_pkg.config.find_file.return_value = '/etc/apt/sources.list'
    
    return SourcesList(mock_module)

def test_remove_source(sources_list, mocker):
    # Mock the _parse and _remove_valid_source methods
    mock_parse = mocker.patch.object(sources_list, '_parse', return_value=(None, None, 'parsed_source'))
    mock_remove_valid_source = mocker.patch.object(sources_list, '_remove_valid_source')

    # Call the method with a sample line
    sources_list.remove_source('deb http://example.com stable main')

    # Assert _parse was called with the correct arguments
    mock_parse.assert_called_once_with('deb http://example.com stable main', raise_if_invalid_or_disabled=True)
    
    # Assert _remove_valid_source was called with the parsed source
    mock_remove_valid_source.assert_called_once_with('parsed_source')
