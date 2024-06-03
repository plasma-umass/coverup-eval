# file lib/ansible/plugins/loader.py:56-66
# lines []
# branches ['63->60']

import os
import pytest
from unittest import mock
from ansible.plugins.loader import add_all_plugin_dirs

@pytest.fixture
def mock_get_all_plugin_loaders():
    with mock.patch('ansible.plugins.loader.get_all_plugin_loaders') as mock_loader:
        yield mock_loader

@pytest.fixture
def mock_display_warning():
    with mock.patch('ansible.plugins.loader.display.warning') as mock_warning:
        yield mock_warning

def test_add_all_plugin_dirs_invalid_path(mock_get_all_plugin_loaders, mock_display_warning):
    invalid_path = '/invalid/path'
    
    # Ensure the path is not a directory
    assert not os.path.isdir(invalid_path)
    
    add_all_plugin_dirs(invalid_path)
    
    # Verify that the warning was called with the correct message
    mock_display_warning.assert_called_once_with(
        "Ignoring invalid path provided to plugin path: '%s' is not a directory" % invalid_path
    )

def test_add_all_plugin_dirs_valid_path_no_subdir(mock_get_all_plugin_loaders):
    valid_path = '/tmp/test_plugins'
    os.makedirs(valid_path, exist_ok=True)
    
    # Mock the return value of get_all_plugin_loaders
    mock_get_all_plugin_loaders.return_value = [('plugin1', mock.Mock(subdir=None))]
    
    add_all_plugin_dirs(valid_path)
    
    # Verify that add_directory was not called since subdir is None
    for name, obj in mock_get_all_plugin_loaders.return_value:
        obj.add_directory.assert_not_called()
    
    # Clean up
    os.rmdir(valid_path)

def test_add_all_plugin_dirs_valid_path_with_subdir(mock_get_all_plugin_loaders):
    valid_path = '/tmp/test_plugins'
    subdir = 'subdir'
    os.makedirs(os.path.join(valid_path, subdir), exist_ok=True)
    
    # Mock the return value of get_all_plugin_loaders
    mock_plugin = mock.Mock(subdir=subdir)
    mock_get_all_plugin_loaders.return_value = [('plugin1', mock_plugin)]
    
    add_all_plugin_dirs(valid_path)
    
    # Verify that add_directory was called with the correct path
    mock_plugin.add_directory.assert_called_once_with(os.path.join(valid_path, subdir))
    
    # Clean up
    os.rmdir(os.path.join(valid_path, subdir))
    os.rmdir(valid_path)

def test_add_all_plugin_dirs_valid_path_with_nonexistent_subdir(mock_get_all_plugin_loaders):
    valid_path = '/tmp/test_plugins'
    subdir = 'nonexistent_subdir'
    os.makedirs(valid_path, exist_ok=True)
    
    # Mock the return value of get_all_plugin_loaders
    mock_plugin = mock.Mock(subdir=subdir)
    mock_get_all_plugin_loaders.return_value = [('plugin1', mock_plugin)]
    
    add_all_plugin_dirs(valid_path)
    
    # Verify that add_directory was not called since subdir does not exist
    mock_plugin.add_directory.assert_not_called()
    
    # Clean up
    os.rmdir(valid_path)
