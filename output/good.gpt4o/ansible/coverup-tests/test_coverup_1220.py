# file lib/ansible/plugins/loader.py:316-329
# lines [320, 329]
# branches ['319->320', '321->327', '327->329']

import pytest
import os
from unittest.mock import patch, MagicMock

# Assuming the PluginLoader class is defined in ansible.plugins.loader
from ansible.plugins.loader import PluginLoader

@pytest.fixture
def plugin_loader():
    loader = PluginLoader(class_name='test_class', package='os.path', config=None, subdir=None)
    return loader

def test_get_package_paths_no_package(plugin_loader):
    plugin_loader.package = None
    assert plugin_loader._get_package_paths() == []

def test_get_package_paths_no_package_path(plugin_loader, mocker):
    mocker.patch('ansible.plugins.loader.to_text', side_effect=lambda x, errors: x)
    mocker.patch('os.path.dirname', return_value='/mocked/path')
    mock_import = mocker.patch('builtins.__import__', return_value=os)
    
    result = plugin_loader._get_package_paths(subdirs=False)
    
    assert result == ['/mocked/path']
    assert plugin_loader.package_path == '/mocked/path'
    mock_import.assert_called_once_with('os.path')

def test_get_package_paths_with_subdirs(plugin_loader, mocker):
    mocker.patch('ansible.plugins.loader.to_text', side_effect=lambda x, errors: x)
    mocker.patch('os.path.dirname', return_value='/mocked/path')
    mock_import = mocker.patch('builtins.__import__', return_value=os)
    mock_all_directories = mocker.patch.object(plugin_loader, '_all_directories', return_value=['/mocked/path/subdir1', '/mocked/path/subdir2'])
    
    result = plugin_loader._get_package_paths(subdirs=True)
    
    assert result == ['/mocked/path/subdir1', '/mocked/path/subdir2']
    assert plugin_loader.package_path == '/mocked/path'
    mock_import.assert_called_once_with('os.path')
    mock_all_directories.assert_called_once_with('/mocked/path')
