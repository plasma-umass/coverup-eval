# file lib/ansible/plugins/loader.py:407-419
# lines [407, 410, 412, 413, 414, 415, 417, 418, 419]
# branches ['412->exit', '412->413', '413->414', '413->415', '415->exit', '415->417']

import os
import pytest
from unittest.mock import MagicMock
from ansible.plugins.loader import PluginLoader

# Mock the Display class to prevent actual output during tests
@pytest.fixture
def mock_display(mocker):
    mocker.patch('ansible.utils.display.Display')

# Test function to cover add_directory method with with_subdir=False
def test_add_directory_without_subdir(tmp_path, mock_display):
    # Create a mock PluginLoader with the necessary attributes
    loader = PluginLoader(class_name='test', package='test_package', config={}, subdir='test_subdir')
    loader._extra_dirs = []
    loader._clear_caches = MagicMock()  # Mocking _clear_caches

    # Create a temporary directory to add
    temp_dir = tmp_path / "temp_dir"
    temp_dir.mkdir()

    # Assert that the directory is not already in _extra_dirs
    assert str(temp_dir) not in loader._extra_dirs

    # Call add_directory without with_subdir
    loader.add_directory(str(temp_dir), with_subdir=False)

    # Assert that the directory was added
    assert str(temp_dir) in loader._extra_dirs
    loader._clear_caches.assert_called_once()

# Test function to cover add_directory method with with_subdir=True
def test_add_directory_with_subdir(tmp_path, mock_display):
    # Create a mock PluginLoader with the necessary attributes
    loader = PluginLoader(class_name='test', package='test_package', config={}, subdir='test_subdir')
    loader._extra_dirs = []
    loader._clear_caches = MagicMock()  # Mocking _clear_caches

    # Create a temporary directory to add
    temp_dir = tmp_path / "temp_dir"
    temp_dir.mkdir()

    # Create the expected subdir
    expected_subdir = temp_dir / loader.subdir

    # Assert that the subdir is not already in _extra_dirs
    assert str(expected_subdir) not in loader._extra_dirs

    # Call add_directory with with_subdir
    loader.add_directory(str(temp_dir), with_subdir=True)

    # Assert that the subdir was added
    assert str(expected_subdir) in loader._extra_dirs
    loader._clear_caches.assert_called_once()
