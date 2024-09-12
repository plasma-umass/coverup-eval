# file: lib/ansible/plugins/loader.py:407-419
# asked: {"lines": [407, 410, 412, 413, 414, 415, 417, 418, 419], "branches": [[412, 0], [412, 413], [413, 414], [413, 415], [415, 0], [415, 417]]}
# gained: {"lines": [407, 410, 412, 413, 414, 415, 417, 418, 419], "branches": [[412, 413], [413, 414], [413, 415], [415, 0], [415, 417]]}

import pytest
import os
from unittest.mock import MagicMock, patch
from ansible.plugins.loader import PluginLoader

@pytest.fixture
def plugin_loader():
    loader = PluginLoader(
        class_name='test_class',
        package='test_package',
        config=None,
        subdir='subdir'
    )
    loader._extra_dirs = []
    loader._clear_caches = MagicMock()
    return loader

def test_add_directory_without_subdir(plugin_loader):
    directory = '/tmp/testdir'
    real_path = os.path.realpath(directory)

    with patch('os.path.realpath', return_value=real_path):
        plugin_loader.add_directory(directory, with_subdir=False)

    assert real_path in plugin_loader._extra_dirs
    plugin_loader._clear_caches.assert_called_once()

def test_add_directory_with_subdir(plugin_loader):
    directory = '/tmp/testdir'
    real_path = os.path.realpath(directory)
    subdir_path = os.path.join(real_path, plugin_loader.subdir)

    with patch('os.path.realpath', return_value=real_path):
        plugin_loader.add_directory(directory, with_subdir=True)

    assert subdir_path in plugin_loader._extra_dirs
    plugin_loader._clear_caches.assert_called_once()

def test_add_directory_already_exists(plugin_loader):
    directory = '/tmp/testdir'
    real_path = os.path.realpath(directory)
    plugin_loader._extra_dirs.append(real_path)

    with patch('os.path.realpath', return_value=real_path):
        plugin_loader.add_directory(directory, with_subdir=False)

    assert plugin_loader._extra_dirs.count(real_path) == 1
    plugin_loader._clear_caches.assert_not_called()
