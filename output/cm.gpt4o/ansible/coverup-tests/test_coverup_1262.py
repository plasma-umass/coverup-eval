# file lib/ansible/plugins/loader.py:56-66
# lines []
# branches ['61->60', '63->60']

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

def test_add_all_plugin_dirs_with_subdir(mock_get_all_plugin_loaders, mock_display_warning, tmp_path):
    # Create a temporary directory to act as the plugin path
    plugin_dir = tmp_path / "plugin_dir"
    plugin_dir.mkdir()

    # Create a subdirectory within the plugin directory
    subdir = plugin_dir / "subdir"
    subdir.mkdir()

    # Mock the return value of get_all_plugin_loaders
    mock_get_all_plugin_loaders.return_value = [("test_loader", mock.Mock(subdir="subdir"))]

    # Mock the add_directory method
    mock_loader_instance = mock_get_all_plugin_loaders.return_value[0][1]
    mock_loader_instance.add_directory = mock.Mock()

    # Call the function with the temporary plugin directory
    add_all_plugin_dirs(str(plugin_dir))

    # Assertions to verify the correct behavior
    mock_loader_instance.add_directory.assert_called_once_with(str(subdir))
    mock_display_warning.assert_not_called()

def test_add_all_plugin_dirs_without_subdir(mock_get_all_plugin_loaders, mock_display_warning, tmp_path):
    # Create a temporary directory to act as the plugin path
    plugin_dir = tmp_path / "plugin_dir"
    plugin_dir.mkdir()

    # Mock the return value of get_all_plugin_loaders
    mock_get_all_plugin_loaders.return_value = [("test_loader", mock.Mock(subdir=None))]

    # Call the function with the temporary plugin directory
    add_all_plugin_dirs(str(plugin_dir))

    # Assertions to verify the correct behavior
    mock_display_warning.assert_not_called()

def test_add_all_plugin_dirs_invalid_path(mock_get_all_plugin_loaders, mock_display_warning):
    # Call the function with an invalid path
    add_all_plugin_dirs("/invalid/path")

    # Assertions to verify the correct behavior
    mock_display_warning.assert_called_once_with("Ignoring invalid path provided to plugin path: '/invalid/path' is not a directory")
