# file: lib/ansible/plugins/loader.py:56-66
# asked: {"lines": [], "branches": [[63, 60]]}
# gained: {"lines": [], "branches": [[63, 60]]}

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

def test_add_all_plugin_dirs_valid_path_with_subdir(monkeypatch, mock_get_all_plugin_loaders):
    # Setup
    test_path = '/tmp/test_plugins'
    subdir = 'test_subdir'
    os.makedirs(os.path.join(test_path, subdir), exist_ok=True)
    
    mock_loader_instance = mock.Mock()
    mock_loader_instance.subdir = subdir
    mock_get_all_plugin_loaders.return_value = [('test_loader', mock_loader_instance)]
    
    # Test
    add_all_plugin_dirs(test_path)
    
    # Assert
    mock_loader_instance.add_directory.assert_called_once_with(os.path.join(test_path, subdir))
    
    # Cleanup
    os.rmdir(os.path.join(test_path, subdir))
    os.rmdir(test_path)

def test_add_all_plugin_dirs_valid_path_with_nonexistent_subdir(monkeypatch, mock_get_all_plugin_loaders):
    # Setup
    test_path = '/tmp/test_plugins'
    subdir = 'nonexistent_subdir'
    os.makedirs(test_path, exist_ok=True)
    
    mock_loader_instance = mock.Mock()
    mock_loader_instance.subdir = subdir
    mock_get_all_plugin_loaders.return_value = [('test_loader', mock_loader_instance)]
    
    # Test
    add_all_plugin_dirs(test_path)
    
    # Assert
    mock_loader_instance.add_directory.assert_not_called()
    
    # Cleanup
    os.rmdir(test_path)

def test_add_all_plugin_dirs_valid_path_without_subdir(monkeypatch, mock_get_all_plugin_loaders):
    # Setup
    test_path = '/tmp/test_plugins'
    os.makedirs(test_path, exist_ok=True)
    
    mock_loader_instance = mock.Mock()
    mock_loader_instance.subdir = None
    mock_get_all_plugin_loaders.return_value = [('test_loader', mock_loader_instance)]
    
    # Test
    add_all_plugin_dirs(test_path)
    
    # Assert
    mock_loader_instance.add_directory.assert_not_called()
    
    # Cleanup
    os.rmdir(test_path)

def test_add_all_plugin_dirs_invalid_path(mock_display_warning):
    # Setup
    invalid_path = '/invalid/path'
    
    # Test
    add_all_plugin_dirs(invalid_path)
    
    # Assert
    mock_display_warning.assert_called_once_with("Ignoring invalid path provided to plugin path: '%s' is not a directory" % invalid_path)
