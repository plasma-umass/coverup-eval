# file lib/ansible/plugins/loader.py:407-419
# lines [407, 410, 412, 413, 414, 415, 417, 418, 419]
# branches ['412->exit', '412->413', '413->414', '413->415', '415->exit', '415->417']

import os
import pytest
from unittest import mock

# Assuming the PluginLoader class is imported from ansible.plugins.loader
from ansible.plugins.loader import PluginLoader

@pytest.fixture
def plugin_loader():
    loader = PluginLoader(class_name='test_class', package='test_package', config='test_config', subdir='subdir')
    loader._extra_dirs = []
    loader._clear_caches = mock.Mock()
    return loader

def test_add_directory(plugin_loader, tmp_path):
    test_dir = tmp_path / "test_dir"
    test_dir.mkdir()

    # Test adding directory without subdir
    plugin_loader.add_directory(str(test_dir))
    assert plugin_loader._clear_caches.called
    assert str(test_dir.resolve()) in plugin_loader._extra_dirs

    # Test adding directory with subdir
    plugin_loader._clear_caches.reset_mock()
    plugin_loader.add_directory(str(test_dir), with_subdir=True)
    assert plugin_loader._clear_caches.called
    assert str((test_dir / plugin_loader.subdir).resolve()) in plugin_loader._extra_dirs

    # Test adding the same directory again should not call _clear_caches
    plugin_loader._clear_caches.reset_mock()
    plugin_loader.add_directory(str(test_dir))
    assert not plugin_loader._clear_caches.called

    # Test adding the same directory with subdir again should not call _clear_caches
    plugin_loader._clear_caches.reset_mock()
    plugin_loader.add_directory(str(test_dir), with_subdir=True)
    assert not plugin_loader._clear_caches.called
