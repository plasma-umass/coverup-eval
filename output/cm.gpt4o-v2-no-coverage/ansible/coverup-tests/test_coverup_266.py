# file: lib/ansible/plugins/loader.py:56-66
# asked: {"lines": [56, 58, 59, 60, 61, 62, 63, 64, 66], "branches": [[59, 60], [59, 66], [60, 0], [60, 61], [61, 60], [61, 62], [63, 60], [63, 64]]}
# gained: {"lines": [56, 58, 59, 60, 61, 62, 63, 64, 66], "branches": [[59, 60], [59, 66], [60, 0], [60, 61], [61, 60], [61, 62], [63, 64]]}

import os
import pytest
from unittest.mock import MagicMock, patch
from ansible.module_utils._text import to_bytes, to_text
from ansible.plugins.loader import add_all_plugin_dirs

class MockPluginLoader:
    def __init__(self, subdir=None):
        self.subdir = subdir
        self.add_directory = MagicMock()

@pytest.fixture
def mock_get_all_plugin_loaders():
    with patch('ansible.plugins.loader.get_all_plugin_loaders') as mock:
        yield mock

@pytest.fixture
def mock_display_warning():
    with patch('ansible.plugins.loader.display.warning') as mock:
        yield mock

def test_add_all_plugin_dirs_valid_path_with_subdir(mock_get_all_plugin_loaders, mock_display_warning, tmp_path):
    mock_loader = MockPluginLoader(subdir='subdir')
    mock_get_all_plugin_loaders.return_value = [('mock_loader', mock_loader)]
    
    subdir_path = tmp_path / 'subdir'
    subdir_path.mkdir(parents=True)
    
    add_all_plugin_dirs(str(tmp_path))
    
    mock_loader.add_directory.assert_called_once_with(str(subdir_path))

def test_add_all_plugin_dirs_valid_path_without_subdir(mock_get_all_plugin_loaders, mock_display_warning, tmp_path):
    mock_loader = MockPluginLoader(subdir=None)
    mock_get_all_plugin_loaders.return_value = [('mock_loader', mock_loader)]
    
    add_all_plugin_dirs(str(tmp_path))
    
    mock_loader.add_directory.assert_not_called()

def test_add_all_plugin_dirs_invalid_path(mock_get_all_plugin_loaders, mock_display_warning):
    invalid_path = '/invalid/path'
    
    add_all_plugin_dirs(invalid_path)
    
    mock_display_warning.assert_called_once_with("Ignoring invalid path provided to plugin path: '%s' is not a directory" % invalid_path)
