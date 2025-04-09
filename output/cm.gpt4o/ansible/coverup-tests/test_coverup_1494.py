# file lib/ansible/plugins/loader.py:316-329
# lines []
# branches ['321->327']

import os
import pytest
from unittest.mock import patch, MagicMock

# Assuming the PluginLoader class is defined in ansible.plugins.loader
from ansible.plugins.loader import PluginLoader

@pytest.fixture
def plugin_loader():
    loader = PluginLoader(class_name='test_class', package='os.path', config=None, subdir=None)
    return loader

def test_get_package_paths_with_subdirs(plugin_loader, mocker):
    mocker.patch.object(plugin_loader, '_all_directories', return_value=['/mocked/path'])
    
    # Ensure 'package_path' attribute is not set initially
    assert not hasattr(plugin_loader, 'package_path')
    
    # Call the method to cover the branch 321->327
    result = plugin_loader._get_package_paths(subdirs=True)
    
    # Verify that the 'package_path' attribute is set
    assert hasattr(plugin_loader, 'package_path')
    
    # Verify the result
    assert result == ['/mocked/path']

def test_get_package_paths_without_subdirs(plugin_loader):
    # Ensure 'package_path' attribute is not set initially
    assert not hasattr(plugin_loader, 'package_path')
    
    # Call the method to cover the branch 321->327
    result = plugin_loader._get_package_paths(subdirs=False)
    
    # Verify that the 'package_path' attribute is set
    assert hasattr(plugin_loader, 'package_path')
    
    # Verify the result
    assert result == [plugin_loader.package_path]

def test_get_package_paths_with_package_path(plugin_loader, mocker):
    mocker.patch.object(plugin_loader, '_all_directories', return_value=['/mocked/path'])
    
    # Manually set the 'package_path' attribute
    plugin_loader.package_path = '/mocked/package/path'
    
    # Call the method to cover the branch 321->327
    result = plugin_loader._get_package_paths(subdirs=True)
    
    # Verify the result
    assert result == ['/mocked/path']
