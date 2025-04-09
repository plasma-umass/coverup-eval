# file: lib/ansible/plugins/loader.py:203-236
# asked: {"lines": [203, 204, 206, 207, 208, 209, 212, 214, 215, 216, 217, 219, 221, 222, 223, 224, 225, 226, 229, 232, 233, 234, 236], "branches": [[214, 215], [214, 216], [216, 217], [216, 219], [221, 222], [221, 223], [223, 224], [223, 225], [225, 226], [225, 229]]}
# gained: {"lines": [203, 204, 206, 207, 208, 209, 212, 214, 215, 216, 217, 219, 221, 222, 223, 224, 225, 226, 229, 232, 233, 234, 236], "branches": [[214, 215], [214, 216], [216, 217], [216, 219], [221, 222], [221, 223], [223, 224], [223, 225], [225, 226], [225, 229]]}

import pytest
from collections import defaultdict
from ansible.plugins.loader import PluginLoader
from ansible.plugins import MODULE_CACHE, PATH_CACHE, PLUGIN_PATH_CACHE

@pytest.fixture(autouse=True)
def cleanup():
    # Clean up MODULE_CACHE, PATH_CACHE, and PLUGIN_PATH_CACHE before and after each test
    MODULE_CACHE.clear()
    PATH_CACHE.clear()
    PLUGIN_PATH_CACHE.clear()
    yield
    MODULE_CACHE.clear()
    PATH_CACHE.clear()
    PLUGIN_PATH_CACHE.clear()

def test_plugin_loader_initialization_with_aliases():
    loader = PluginLoader(class_name="test_class", package="test_package", config=None, subdir="test_subdir", aliases={"alias1": "value1"})
    assert loader.aliases == {"alias1": "value1"}
    assert loader.class_name == "test_class"
    assert loader.package == "test_package"
    assert loader.subdir == "test_subdir"
    assert loader.config == []
    assert loader._extra_dirs == []
    assert loader._searched_paths == set()
    assert MODULE_CACHE["test_class"] == {}
    assert PATH_CACHE["test_class"] is None
    assert isinstance(PLUGIN_PATH_CACHE["test_class"], defaultdict)

def test_plugin_loader_initialization_without_aliases():
    loader = PluginLoader(class_name="test_class", package="test_package", config=None, subdir="test_subdir")
    assert loader.aliases == {}
    assert loader.class_name == "test_class"
    assert loader.package == "test_package"
    assert loader.subdir == "test_subdir"
    assert loader.config == []
    assert loader._extra_dirs == []
    assert loader._searched_paths == set()
    assert MODULE_CACHE["test_class"] == {}
    assert PATH_CACHE["test_class"] is None
    assert isinstance(PLUGIN_PATH_CACHE["test_class"], defaultdict)

def test_plugin_loader_initialization_with_config_as_list():
    loader = PluginLoader(class_name="test_class", package="test_package", config=["config1", "config2"], subdir="test_subdir")
    assert loader.config == ["config1", "config2"]
    assert loader.class_name == "test_class"
    assert loader.package == "test_package"
    assert loader.subdir == "test_subdir"
    assert loader._extra_dirs == []
    assert loader._searched_paths == set()
    assert MODULE_CACHE["test_class"] == {}
    assert PATH_CACHE["test_class"] is None
    assert isinstance(PLUGIN_PATH_CACHE["test_class"], defaultdict)

def test_plugin_loader_initialization_with_config_as_single_item():
    loader = PluginLoader(class_name="test_class", package="test_package", config="single_config", subdir="test_subdir")
    assert loader.config == ["single_config"]
    assert loader.class_name == "test_class"
    assert loader.package == "test_package"
    assert loader.subdir == "test_subdir"
    assert loader._extra_dirs == []
    assert loader._searched_paths == set()
    assert MODULE_CACHE["test_class"] == {}
    assert PATH_CACHE["test_class"] is None
    assert isinstance(PLUGIN_PATH_CACHE["test_class"], defaultdict)
