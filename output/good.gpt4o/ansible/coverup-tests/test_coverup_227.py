# file lib/ansible/plugins/loader.py:56-66
# lines [56, 58, 59, 60, 61, 62, 63, 64, 66]
# branches ['59->60', '59->66', '60->exit', '60->61', '61->60', '61->62', '63->60', '63->64']

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

def test_add_all_plugin_dirs_valid_path(mock_get_all_plugin_loaders):
    # Setup
    valid_path = '/tmp/test_plugins'
    subdir = 'test_subdir'
    os.makedirs(os.path.join(valid_path, subdir), exist_ok=True)
    
    mock_loader_obj = mock.Mock()
    mock_loader_obj.subdir = subdir
    mock_loader_obj.add_directory = mock.Mock()
    mock_get_all_plugin_loaders.return_value = [('test_loader', mock_loader_obj)]
    
    # Execute
    add_all_plugin_dirs(valid_path)
    
    # Assert
    mock_loader_obj.add_directory.assert_called_once_with(os.path.join(valid_path, subdir))
    
    # Cleanup
    os.rmdir(os.path.join(valid_path, subdir))
    os.rmdir(valid_path)

def test_add_all_plugin_dirs_invalid_path(mock_display_warning):
    # Setup
    invalid_path = '/tmp/invalid_path'
    
    # Execute
    add_all_plugin_dirs(invalid_path)
    
    # Assert
    mock_display_warning.assert_called_once_with("Ignoring invalid path provided to plugin path: '%s' is not a directory" % invalid_path)
