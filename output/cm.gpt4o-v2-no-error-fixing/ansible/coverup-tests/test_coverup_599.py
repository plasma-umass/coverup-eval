# file: lib/ansible/plugins/loader.py:238-239
# asked: {"lines": [238, 239], "branches": []}
# gained: {"lines": [238, 239], "branches": []}

import pytest
from ansible.plugins.loader import PluginLoader
from ansible.utils.collection_loader import AnsibleCollectionRef

class MockAnsibleCollectionRef:
    @staticmethod
    def legacy_plugin_dir_to_plugin_type(legacy_plugin_dir_name):
        if legacy_plugin_dir_name == "valid_subdir":
            return "valid_type"
        raise ValueError("Invalid subdir")

def test_plugin_loader_repr(monkeypatch):
    monkeypatch.setattr(AnsibleCollectionRef, "legacy_plugin_dir_to_plugin_type", MockAnsibleCollectionRef.legacy_plugin_dir_to_plugin_type)
    
    loader = PluginLoader(class_name="test_class", package="test_package", config=None, subdir="valid_subdir")
    assert repr(loader) == "PluginLoader(type=valid_type)"
