# file: lib/ansible/plugins/loader.py:294-302
# asked: {"lines": [294, 298, 299, 300, 301, 302], "branches": [[299, 300], [299, 302], [300, 299], [300, 301]]}
# gained: {"lines": [294, 298, 299, 300, 301, 302], "branches": [[299, 300], [299, 302], [300, 299], [300, 301]]}

import pytest
from ansible.plugins.loader import PluginLoader

def test_format_paths():
    loader = PluginLoader(class_name="test", package="test_package", config=None, subdir="test_subdir")
    
    # Test with empty paths
    assert loader.format_paths([]) == ""
    
    # Test with unique paths
    paths = ["/path/one", "/path/two"]
    assert loader.format_paths(paths) == "/path/one:/path/two"
    
    # Test with duplicate paths
    paths = ["/path/one", "/path/two", "/path/one"]
    assert loader.format_paths(paths) == "/path/one:/path/two"
    
    # Test with os.pathsep in paths
    paths = ["/path/one", "/path/two:path/three"]
    assert loader.format_paths(paths) == "/path/one:/path/two:path/three"
