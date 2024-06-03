# file lib/ansible/plugins/loader.py:294-302
# lines [294, 298, 299, 300, 301, 302]
# branches ['299->300', '299->302', '300->299', '300->301']

import pytest
import os
from ansible.plugins.loader import PluginLoader

class TestPluginLoader(PluginLoader):
    def __init__(self):
        pass

@pytest.fixture
def plugin_loader():
    return TestPluginLoader()

def test_format_paths(plugin_loader):
    paths = ['/path/one', '/path/two', '/path/one']
    expected_result = os.pathsep.join(['/path/one', '/path/two'])
    
    result = plugin_loader.format_paths(paths)
    
    assert result == expected_result

def test_format_paths_empty(plugin_loader):
    paths = []
    expected_result = ''
    
    result = plugin_loader.format_paths(paths)
    
    assert result == expected_result

def test_format_paths_single(plugin_loader):
    paths = ['/path/one']
    expected_result = '/path/one'
    
    result = plugin_loader.format_paths(paths)
    
    assert result == expected_result
