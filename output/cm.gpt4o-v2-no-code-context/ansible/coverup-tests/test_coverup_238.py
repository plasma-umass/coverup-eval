# file: lib/ansible/plugins/loader.py:407-419
# asked: {"lines": [407, 410, 412, 413, 414, 415, 417, 418, 419], "branches": [[412, 0], [412, 413], [413, 414], [413, 415], [415, 0], [415, 417]]}
# gained: {"lines": [407, 410, 412, 413, 414, 415, 417, 418, 419], "branches": [[412, 413], [413, 414], [413, 415], [415, 0], [415, 417]]}

import os
import pytest
from unittest import mock

# Assuming the PluginLoader class is defined in ansible/plugins/loader.py
from ansible.plugins.loader import PluginLoader

@pytest.fixture
def plugin_loader():
    loader = PluginLoader(class_name='test_class', package='test_package', config='test_config', subdir='subdir')
    loader._extra_dirs = []
    loader._clear_caches = mock.Mock()
    return loader

def test_add_directory_with_subdir(plugin_loader, monkeypatch):
    test_dir = '/test/directory'
    realpath = os.path.realpath(test_dir)
    expected_dir = os.path.join(realpath, plugin_loader.subdir)

    monkeypatch.setattr(os.path, 'realpath', lambda x: realpath)
    plugin_loader.add_directory(test_dir, with_subdir=True)

    assert expected_dir in plugin_loader._extra_dirs
    plugin_loader._clear_caches.assert_called_once()

def test_add_directory_without_subdir(plugin_loader, monkeypatch):
    test_dir = '/test/directory'
    realpath = os.path.realpath(test_dir)

    monkeypatch.setattr(os.path, 'realpath', lambda x: realpath)
    plugin_loader.add_directory(test_dir, with_subdir=False)

    assert realpath in plugin_loader._extra_dirs
    plugin_loader._clear_caches.assert_called_once()

def test_add_directory_already_exists(plugin_loader, monkeypatch):
    test_dir = '/test/directory'
    realpath = os.path.realpath(test_dir)

    monkeypatch.setattr(os.path, 'realpath', lambda x: realpath)
    plugin_loader._extra_dirs.append(realpath)
    plugin_loader.add_directory(test_dir, with_subdir=False)

    assert plugin_loader._extra_dirs.count(realpath) == 1
    plugin_loader._clear_caches.assert_not_called()
