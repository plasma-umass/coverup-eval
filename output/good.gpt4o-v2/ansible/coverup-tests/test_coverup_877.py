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
        repr_str = repr(plugin_loader)
        assert repr_str == 'PluginLoader(type=test_type)'

