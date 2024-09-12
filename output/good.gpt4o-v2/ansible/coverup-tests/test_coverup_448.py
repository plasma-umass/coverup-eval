# file: lib/ansible/plugins/loader.py:294-302
# asked: {"lines": [294, 298, 299, 300, 301, 302], "branches": [[299, 300], [299, 302], [300, 299], [300, 301]]}
# gained: {"lines": [294, 298, 299, 300, 301, 302], "branches": [[299, 300], [299, 302], [300, 299], [300, 301]]}

import pytest
import os
from collections import defaultdict
from ansible.plugins.loader import PluginLoader

@pytest.fixture
def plugin_loader(mocker):
    mocker.patch('ansible.plugins.loader.MODULE_CACHE', {})
    mocker.patch('ansible.plugins.loader.PATH_CACHE', {})
    mocker.patch('ansible.plugins.loader.PLUGIN_PATH_CACHE', defaultdict(dict))
    return PluginLoader(class_name="test_class", package="test_package", config=[], subdir="test_subdir")

def test_format_paths(plugin_loader):
    paths = ["path1", "path2", "path1", "path3"]
    expected_result = os.pathsep.join(["path1", "path2", "path3"])
    result = plugin_loader.format_paths(paths)
    assert result == expected_result

    # Test with empty paths
    paths = []
    expected_result = ""
    result = plugin_loader.format_paths(paths)
    assert result == expected_result

    # Test with no duplicates
    paths = ["path1", "path2", "path3"]
    expected_result = os.pathsep.join(["path1", "path2", "path3"])
    result = plugin_loader.format_paths(paths)
    assert result == expected_result

    # Test with all duplicates
    paths = ["path1", "path1", "path1"]
    expected_result = "path1"
    result = plugin_loader.format_paths(paths)
    assert result == expected_result
