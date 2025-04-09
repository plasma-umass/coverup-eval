# file: lib/ansible/plugins/loader.py:316-329
# asked: {"lines": [320, 329], "branches": [[319, 320], [321, 327], [327, 329]]}
# gained: {"lines": [320, 329], "branches": [[319, 320], [327, 329]]}

import os
import pytest
from unittest.mock import patch, MagicMock

# Assuming the PluginLoader class is defined in ansible/plugins/loader.py
from ansible.plugins.loader import PluginLoader

@pytest.fixture
def plugin_loader():
    class TestPluginLoader(PluginLoader):
        def __init__(self, package):
            self.package = package
    return TestPluginLoader

def test_get_package_paths_no_package(plugin_loader):
    loader = plugin_loader(None)
    assert loader._get_package_paths() == []

def test_get_package_paths_with_package_no_subdirs(plugin_loader, monkeypatch):
    loader = plugin_loader('os.path')
    
    def mock_to_text(path, errors):
        return path
    
    monkeypatch.setattr('ansible.plugins.loader.to_text', mock_to_text)
    
    assert loader._get_package_paths(subdirs=False) == [os.path.dirname(os.path.__file__)]

def test_get_package_paths_with_package_with_subdirs(plugin_loader, monkeypatch):
    loader = plugin_loader('os.path')
    
    def mock_to_text(path, errors):
        return path
    
    def mock_all_directories(path):
        return [path, os.path.join(path, 'subdir')]
    
    monkeypatch.setattr('ansible.plugins.loader.to_text', mock_to_text)
    monkeypatch.setattr(loader, '_all_directories', mock_all_directories)
    
    assert loader._get_package_paths(subdirs=True) == [os.path.dirname(os.path.__file__), os.path.join(os.path.dirname(os.path.__file__), 'subdir')]

def test_get_package_paths_with_nested_package(plugin_loader, monkeypatch):
    loader = plugin_loader('os.path')
    
    def mock_to_text(path, errors):
        return path
    
    monkeypatch.setattr('ansible.plugins.loader.to_text', mock_to_text)
    
    assert loader._get_package_paths(subdirs=False) == [os.path.dirname(os.path.__file__)]
