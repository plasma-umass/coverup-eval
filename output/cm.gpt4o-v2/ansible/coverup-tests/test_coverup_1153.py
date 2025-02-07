# file: lib/ansible/plugins/loader.py:56-66
# asked: {"lines": [58, 59, 60, 61, 62, 63, 64, 66], "branches": [[59, 60], [59, 66], [60, 0], [60, 61], [61, 60], [61, 62], [63, 60], [63, 64]]}
# gained: {"lines": [58, 59, 60, 61, 62, 63, 64, 66], "branches": [[59, 60], [59, 66], [60, 0], [60, 61], [61, 62], [63, 64]]}

import os
import pytest
from unittest.mock import MagicMock, patch
from ansible.module_utils._text import to_bytes, to_text
from ansible.plugins.loader import add_all_plugin_dirs, get_all_plugin_loaders

class MockPluginLoader:
    def __init__(self, subdir=None):
        self.subdir = subdir

    def add_directory(self, path):
        pass

@pytest.fixture
def mock_get_all_plugin_loaders(monkeypatch):
    mock_loader = MockPluginLoader(subdir='valid_subdir')
    monkeypatch.setattr('ansible.plugins.loader.get_all_plugin_loaders', lambda: [('mock_loader', mock_loader)])
    return mock_loader

def test_add_all_plugin_dirs_valid_path(mock_get_all_plugin_loaders, monkeypatch):
    mock_loader = mock_get_all_plugin_loaders
    mock_add_directory = MagicMock()
    mock_loader.add_directory = mock_add_directory

    with patch('os.path.isdir', return_value=True):
        with patch('os.path.expanduser', side_effect=lambda x: x):
            add_all_plugin_dirs('valid_path')

    mock_add_directory.assert_called_once_with('valid_path/valid_subdir')

def test_add_all_plugin_dirs_invalid_path(monkeypatch):
    mock_warning = MagicMock()
    monkeypatch.setattr('ansible.plugins.loader.display.warning', mock_warning)

    with patch('os.path.isdir', return_value=False):
        with patch('os.path.expanduser', side_effect=lambda x: x):
            add_all_plugin_dirs('invalid_path')

    mock_warning.assert_called_once_with("Ignoring invalid path provided to plugin path: 'invalid_path' is not a directory")
