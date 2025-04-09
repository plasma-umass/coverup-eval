# file: lib/ansible/plugins/loader.py:865-876
# asked: {"lines": [865, 867, 868, 870, 871, 873, 874, 876], "branches": [[867, 0], [867, 868], [870, 871], [870, 873], [873, 874], [873, 876]]}
# gained: {"lines": [865, 867, 868, 870, 871, 873, 874, 876], "branches": [[867, 0], [867, 868], [870, 871], [870, 873], [873, 874]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.plugins.loader import PluginLoader
from ansible import constants as C

@pytest.fixture
def plugin_loader():
    return PluginLoader(class_name="test_class", package="test_package", config=None, subdir="test_subdir")

@patch('ansible.plugins.loader.display.debug')
def test_display_plugin_load_debug_on(mock_debug, plugin_loader):
    with patch.object(C, 'DEFAULT_DEBUG', True):
        plugin_loader._display_plugin_load(
            class_name="test_class",
            name="/path/to/plugin",
            searched_paths=["/path/one", "/path/two"],
            path="/path/to/plugin",
            found_in_cache=True,
            class_only=False
        )
        mock_debug.assert_called_once_with("Loading test_class 'plugin' from /path/to/plugin (searched paths: /path/one:/path/two) (found_in_cache=True, class_only=False)")

@patch('ansible.plugins.loader.display.debug')
def test_display_plugin_load_debug_off(mock_debug, plugin_loader):
    with patch.object(C, 'DEFAULT_DEBUG', False):
        plugin_loader._display_plugin_load(
            class_name="test_class",
            name="/path/to/plugin",
            searched_paths=["/path/one", "/path/two"],
            path="/path/to/plugin",
            found_in_cache=True,
            class_only=False
        )
        mock_debug.assert_not_called()

@patch('ansible.plugins.loader.display.debug')
def test_display_plugin_load_single_search_path(mock_debug, plugin_loader):
    with patch.object(C, 'DEFAULT_DEBUG', True):
        plugin_loader._display_plugin_load(
            class_name="test_class",
            name="/path/to/plugin",
            searched_paths=["/path/one"],
            path="/path/to/plugin",
            found_in_cache=False,
            class_only=True
        )
        mock_debug.assert_called_once_with("Loading test_class 'plugin' from /path/to/plugin (found_in_cache=False, class_only=True)")
