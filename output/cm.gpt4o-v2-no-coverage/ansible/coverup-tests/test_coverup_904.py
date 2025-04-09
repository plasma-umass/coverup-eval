# file: lib/ansible/plugins/loader.py:238-239
# asked: {"lines": [238, 239], "branches": []}
# gained: {"lines": [238, 239], "branches": []}

import pytest
from unittest.mock import patch
from ansible.plugins.loader import PluginLoader
from ansible.utils.collection_loader import AnsibleCollectionRef

@pytest.fixture
def plugin_loader():
    return PluginLoader(class_name="test_class", package="test_package", config=None, subdir="test_subdir")

def test_plugin_loader_repr(plugin_loader):
    with patch.object(AnsibleCollectionRef, 'legacy_plugin_dir_to_plugin_type', return_value="test_type"):
        result = repr(plugin_loader)
        assert result == "PluginLoader(type=test_type)"

def test_plugin_loader_cleanup(plugin_loader):
    # Ensure no state pollution
    assert plugin_loader.class_name == "test_class"
    assert plugin_loader.package == "test_package"
    assert plugin_loader.config == []
    assert plugin_loader.subdir == "test_subdir"
    assert plugin_loader.aliases == {}
    assert plugin_loader._extra_dirs == []
    assert plugin_loader._searched_paths == set()
