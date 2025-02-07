# file: lib/ansible/plugins/loader.py:331-382
# asked: {"lines": [], "branches": [[343, 360], [346, 353], [350, 348], [354, 344]]}
# gained: {"lines": [], "branches": [[343, 360], [346, 353]]}

import pytest
import os
import glob
from unittest.mock import patch, MagicMock
from ansible.plugins.loader import PluginLoader, PluginPathContext

@pytest.fixture
def plugin_loader():
    loader = PluginLoader(class_name='test_class', package='test_package', config=None, subdir='test_subdir')
    loader._paths = None
    loader._extra_dirs = []
    loader.config = None
    return loader

def test_get_paths_with_context_no_config(plugin_loader):
    plugin_loader.config = None
    plugin_loader._extra_dirs = ['/extra/dir']
    
    with patch('ansible.plugins.loader.PluginLoader._get_package_paths', return_value=['/package/path']):
        paths = plugin_loader._get_paths_with_context(subdirs=True)
    
    assert len(paths) == 2
    assert paths[0].path == '/extra/dir'
    assert paths[1].path == '/package/path'

def test_get_paths_with_context_with_config_subdirs(plugin_loader, monkeypatch):
    plugin_loader.config = ['/config/path']
    plugin_loader._extra_dirs = []
    
    def mock_isdir(path):
        return path in ['/config/path/subdir1', '/config/path/subdir2']
    
    def mock_glob(path):
        if path == '/config/path/*':
            return ['/config/path/subdir1']
        elif path == '/config/path/*/*':
            return ['/config/path/subdir2']
        return []
    
    monkeypatch.setattr(glob, 'glob', mock_glob)
    monkeypatch.setattr(os.path, 'isdir', mock_isdir)
    
    with patch('ansible.plugins.loader.PluginLoader._get_package_paths', return_value=[]):
        paths = plugin_loader._get_paths_with_context(subdirs=True)
    
    assert len(paths) == 3
    assert paths[0].path == '/config/path/subdir1'
    assert paths[1].path == '/config/path/subdir2'
    assert paths[2].path == '/config/path'

def test_get_paths_with_context_with_config_no_subdirs(plugin_loader, monkeypatch):
    plugin_loader.config = ['/config/path']
    plugin_loader._extra_dirs = []
    
    monkeypatch.setattr(glob, 'glob', lambda path: [])
    monkeypatch.setattr(os.path, 'isdir', lambda path: False)
    
    with patch('ansible.plugins.loader.PluginLoader._get_package_paths', return_value=[]):
        paths = plugin_loader._get_paths_with_context(subdirs=False)
    
    assert len(paths) == 1
    assert paths[0].path == '/config/path'

def test_get_paths_with_context_with_package_paths(plugin_loader):
    plugin_loader.config = None
    plugin_loader._extra_dirs = []
    
    with patch('ansible.plugins.loader.PluginLoader._get_package_paths', return_value=['/package/path']):
        paths = plugin_loader._get_paths_with_context(subdirs=True)
    
    assert len(paths) == 1
    assert paths[0].path == '/package/path'
