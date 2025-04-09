# file: lib/ansible/plugins/loader.py:316-329
# asked: {"lines": [320, 329], "branches": [[319, 320], [321, 327], [327, 329]]}
# gained: {"lines": [320, 329], "branches": [[319, 320], [327, 329]]}

import os
import pytest
from unittest.mock import patch, MagicMock
from ansible.module_utils._text import to_text
from ansible.plugins.loader import PluginLoader

@pytest.fixture
def plugin_loader():
    loader = PluginLoader(class_name='test_class', package='some_package', config=None, subdir='test_subdir')
    return loader

def test_get_package_paths_no_package(plugin_loader):
    plugin_loader.package = None
    assert plugin_loader._get_package_paths() == []

def test_get_package_paths_with_package_no_subdirs(plugin_loader, monkeypatch):
    mock_module = MagicMock()
    mock_module.__file__ = '/path/to/some_package/__init__.py'
    monkeypatch.setattr('builtins.__import__', lambda name, globals=None, locals=None, fromlist=(), level=0: mock_module)
    monkeypatch.setattr('os.path.dirname', lambda path: '/path/to/some_package')
    monkeypatch.setattr('ansible.module_utils._text.to_text', lambda path, errors: path)
    
    result = plugin_loader._get_package_paths(subdirs=False)
    assert result == ['/path/to/some_package']

def test_get_package_paths_with_package_with_subdirs(plugin_loader, monkeypatch):
    mock_module = MagicMock()
    mock_module.__file__ = '/path/to/some_package/__init__.py'
    monkeypatch.setattr('builtins.__import__', lambda name, globals=None, locals=None, fromlist=(), level=0: mock_module)
    monkeypatch.setattr('os.path.dirname', lambda path: '/path/to/some_package')
    monkeypatch.setattr('ansible.module_utils._text.to_text', lambda path, errors: path)
    
    mock_all_directories = MagicMock(return_value=['/path/to/some_package', '/path/to/some_package/subdir'])
    monkeypatch.setattr(plugin_loader, '_all_directories', mock_all_directories)
    
    result = plugin_loader._get_package_paths(subdirs=True)
    assert result == ['/path/to/some_package', '/path/to/some_package/subdir']
    mock_all_directories.assert_called_once_with('/path/to/some_package')

def test_all_directories(monkeypatch):
    mock_os_walk = MagicMock(return_value=[
        ('/path/to/some_package', ['subdir'], ['__init__.py']),
        ('/path/to/some_package/subdir', [], ['__init__.py'])
    ])
    monkeypatch.setattr('os.walk', mock_os_walk)
    
    loader = PluginLoader(class_name='test_class', package='some_package', config=None, subdir='test_subdir')
    result = loader._all_directories('/path/to/some_package')
    assert result == ['/path/to/some_package', '/path/to/some_package/subdir']
