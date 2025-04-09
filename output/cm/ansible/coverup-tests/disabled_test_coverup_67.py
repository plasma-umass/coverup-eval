# file lib/ansible/plugins/loader.py:203-236
# lines [203, 204, 206, 207, 208, 209, 212, 214, 215, 216, 217, 219, 221, 222, 223, 224, 225, 226, 229, 232, 233, 234, 236]
# branches ['214->215', '214->216', '216->217', '216->219', '221->222', '221->223', '223->224', '223->225', '225->226', '225->229']

import pytest
from collections import defaultdict
from ansible.plugins.loader import PluginLoader

# Mock global caches
MODULE_CACHE = {}
PATH_CACHE = {}
PLUGIN_PATH_CACHE = defaultdict(dict)

@pytest.fixture
def plugin_loader_cleanup():
    # Fixture to clean up the global state after each test
    yield
    MODULE_CACHE.clear()
    PATH_CACHE.clear()
    PLUGIN_PATH_CACHE.clear()

def test_plugin_loader_initialization(plugin_loader_cleanup, mocker):
    # Test to ensure that the PluginLoader initializes correctly and covers missing branches
    class_name = "TestPlugin"
    package = "test_package"
    config = "test_config"
    subdir = "test_subdir"
    aliases = {"alias1": "original1"}

    # Mock the global caches
    mocker.patch('ansible.plugins.loader.MODULE_CACHE', MODULE_CACHE)
    mocker.patch('ansible.plugins.loader.PATH_CACHE', PATH_CACHE)
    mocker.patch('ansible.plugins.loader.PLUGIN_PATH_CACHE', PLUGIN_PATH_CACHE)

    # Create a PluginLoader instance
    loader = PluginLoader(class_name, package, config, subdir, aliases)

    # Assertions to verify postconditions
    assert loader.class_name == class_name
    assert loader.package == package
    assert loader.subdir == subdir
    assert loader.aliases == aliases
    assert loader.config == [config]  # config should be converted to a list
    assert loader._extra_dirs == []  # _extra_dirs should be initialized as an empty list

    # Verify that the global caches have been updated
    assert MODULE_CACHE[class_name] == loader._module_cache
    assert PATH_CACHE[class_name] == loader._paths
    assert PLUGIN_PATH_CACHE[class_name] == loader._plugin_path_cache

    # Test with config as a list
    config_list = ["config1", "config2"]
    loader_with_list_config = PluginLoader(class_name, package, config_list, subdir, aliases)
    assert loader_with_list_config.config == config_list

    # Test with no config
    loader_with_no_config = PluginLoader(class_name, package, None, subdir, aliases)
    assert loader_with_no_config.config == []

    # Test with empty config
    loader_with_empty_config = PluginLoader(class_name, package, [], subdir, aliases)
    assert loader_with_empty_config.config == []

    # Test with no aliases
    loader_with_no_aliases = PluginLoader(class_name, package, config, subdir)
    assert loader_with_no_aliases.aliases == {}

    # Test with a required base class
    required_base_class = mocker.MagicMock()
    loader_with_base_class = PluginLoader(class_name, package, config, subdir, aliases, required_base_class)
    assert loader_with_base_class.base_class == required_base_class
