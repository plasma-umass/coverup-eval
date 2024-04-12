# file lib/ansible/plugins/loader.py:407-419
# lines []
# branches ['412->exit', '415->exit']

import os
import pytest
from unittest.mock import MagicMock
from ansible.plugins.loader import PluginLoader

# Mock the PluginLoader class to prevent actual initialization during tests
@pytest.fixture
def mock_plugin_loader(mocker):
    mocker.patch('ansible.plugins.loader.PluginLoader.__init__', return_value=None)
    plugin_loader = PluginLoader()
    plugin_loader._extra_dirs = []
    plugin_loader.subdir = ''
    plugin_loader._clear_caches = MagicMock()
    return plugin_loader

@pytest.fixture
def temp_directory(tmp_path):
    dir_path = tmp_path / "testdir"
    dir_path.mkdir()
    return str(dir_path)

def test_add_directory_not_none_and_not_in_extra_dirs(mock_plugin_loader, temp_directory):
    # Ensure the directory is not already in _extra_dirs
    assert temp_directory not in mock_plugin_loader._extra_dirs

    # Call add_directory with a real directory
    mock_plugin_loader.add_directory(temp_directory)

    # Check if the directory was added
    assert temp_directory in mock_plugin_loader._extra_dirs

    # Call add_directory again with the same directory to test the branch where the directory is already in _extra_dirs
    mock_plugin_loader.add_directory(temp_directory)

    # The directory should not be added again
    assert mock_plugin_loader._extra_dirs.count(temp_directory) == 1

def test_add_directory_with_subdir(mock_plugin_loader, temp_directory):
    subdir = "subdir"
    expected_directory = os.path.join(temp_directory, subdir)

    # Ensure the directory with subdir is not already in _extra_dirs
    assert expected_directory not in mock_plugin_loader._extra_dirs

    # Set the subdir attribute to mimic the behavior of the loader
    mock_plugin_loader.subdir = subdir

    # Call add_directory with with_subdir=True
    mock_plugin_loader.add_directory(temp_directory, with_subdir=True)

    # Check if the directory with subdir was added
    assert expected_directory in mock_plugin_loader._extra_dirs

    # Call add_directory again with the same directory and with_subdir=True to test the branch where the directory is already in _extra_dirs
    mock_plugin_loader.add_directory(temp_directory, with_subdir=True)

    # The directory should not be added again
    assert mock_plugin_loader._extra_dirs.count(expected_directory) == 1
