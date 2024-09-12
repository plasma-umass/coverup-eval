# file: lib/ansible/plugins/loader.py:56-66
# asked: {"lines": [], "branches": [[61, 60], [63, 60]]}
# gained: {"lines": [], "branches": [[61, 60]]}

import os
import pytest
from unittest.mock import MagicMock, patch
from ansible.module_utils._text import to_bytes, to_text
from ansible.plugins.loader import add_all_plugin_dirs

class MockPluginLoader:
    def __init__(self, subdir=None):
        self.subdir = subdir

    def add_directory(self, path):
        pass

def mock_get_all_plugin_loaders():
    return [
        ('loader_with_subdir', MockPluginLoader(subdir='valid_subdir')),
        ('loader_without_subdir', MockPluginLoader(subdir=None)),
    ]

@pytest.fixture
def mock_display_warning(mocker):
    return mocker.patch('ansible.plugins.loader.display.warning')

@pytest.fixture
def setup_filesystem(tmp_path):
    valid_path = tmp_path / "valid_path"
    valid_path.mkdir()
    (valid_path / "valid_subdir").mkdir()
    return valid_path

def test_add_all_plugin_dirs_with_valid_path_and_subdir(setup_filesystem, mocker, mock_display_warning):
    mocker.patch('ansible.plugins.loader.get_all_plugin_loaders', side_effect=mock_get_all_plugin_loaders)
    mock_loader = MagicMock()
    mocker.patch.object(MockPluginLoader, 'add_directory', mock_loader.add_directory)

    add_all_plugin_dirs(str(setup_filesystem))

    mock_loader.add_directory.assert_called_once_with(str(setup_filesystem / "valid_subdir"))
    mock_display_warning.assert_not_called()

def test_add_all_plugin_dirs_with_valid_path_without_subdir(setup_filesystem, mocker, mock_display_warning):
    mocker.patch('ansible.plugins.loader.get_all_plugin_loaders', side_effect=mock_get_all_plugin_loaders)
    mock_loader = MagicMock()
    mocker.patch.object(MockPluginLoader, 'add_directory', mock_loader.add_directory)

    add_all_plugin_dirs(str(setup_filesystem))

    mock_loader.add_directory.assert_called_once_with(str(setup_filesystem / "valid_subdir"))
    mock_display_warning.assert_not_called()

def test_add_all_plugin_dirs_with_invalid_path(mocker, mock_display_warning):
    invalid_path = "/invalid_path"
    mocker.patch('ansible.plugins.loader.get_all_plugin_loaders', side_effect=mock_get_all_plugin_loaders)

    add_all_plugin_dirs(invalid_path)

    mock_display_warning.assert_called_once_with("Ignoring invalid path provided to plugin path: '%s' is not a directory" % invalid_path)
