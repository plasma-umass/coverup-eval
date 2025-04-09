# file: lib/ansible/plugins/loader.py:294-302
# asked: {"lines": [294, 298, 299, 300, 301, 302], "branches": [[299, 300], [299, 302], [300, 299], [300, 301]]}
# gained: {"lines": [294, 298, 299, 300, 301, 302], "branches": [[299, 300], [299, 302], [300, 299], [300, 301]]}

import pytest
import os
from ansible.plugins.loader import PluginLoader

class MockPluginLoader(PluginLoader):
    def __init__(self):
        pass

@pytest.fixture
def plugin_loader():
    return MockPluginLoader()

def test_format_paths_with_duplicates(plugin_loader):
    paths = ['/path/one', '/path/two', '/path/one']
    expected = os.pathsep.join(['/path/one', '/path/two'])
    result = plugin_loader.format_paths(paths)
    assert result == expected

def test_format_paths_without_duplicates(plugin_loader):
    paths = ['/path/one', '/path/two', '/path/three']
    expected = os.pathsep.join(['/path/one', '/path/two', '/path/three'])
    result = plugin_loader.format_paths(paths)
    assert result == expected

def test_format_paths_empty(plugin_loader):
    paths = []
    expected = ''
    result = plugin_loader.format_paths(paths)
    assert result == expected
