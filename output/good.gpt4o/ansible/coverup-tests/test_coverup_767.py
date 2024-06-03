# file lib/ansible/modules/apt_repository.py:401-405
# lines [401, 402, 405]
# branches []

import pytest
from unittest import mock

# Assuming the SourcesList class is imported from ansible.modules.apt_repository
from ansible.modules.apt_repository import SourcesList

@pytest.fixture
def sources_list(mocker):
    # Mocking the 'module' argument required by SourcesList
    module_mock = mocker.Mock()
    
    # Mocking apt_pkg to avoid AttributeError
    apt_pkg_mock = mocker.patch('ansible.modules.apt_repository.apt_pkg')
    apt_pkg_mock.config.find_file.return_value = '/etc/apt/sources.list'
    
    return SourcesList(module=module_mock)

def test_add_source_with_suggested_filename(sources_list, mocker):
    # Mocking the methods that are not the focus of this test
    mocker.patch.object(sources_list, '_parse', return_value=(None, None, 'deb http://example.com stable main'))
    mocker.patch.object(sources_list, '_add_valid_source')
    mocker.patch.object(sources_list, '_suggest_filename', return_value='example.list')

    # Call the method under test
    sources_list.add_source('deb http://example.com stable main', comment='Test comment')

    # Assertions to verify the expected behavior
    sources_list._parse.assert_called_once_with('deb http://example.com stable main', raise_if_invalid_or_disabled=True)
    sources_list._add_valid_source.assert_called_once_with('deb http://example.com stable main', 'Test comment', file='example.list')
    sources_list._suggest_filename.assert_called_once_with('deb http://example.com stable main')
