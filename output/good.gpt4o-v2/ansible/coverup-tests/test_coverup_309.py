# file: lib/ansible/plugins/loader.py:865-876
# asked: {"lines": [865, 867, 868, 870, 871, 873, 874, 876], "branches": [[867, 0], [867, 868], [870, 871], [870, 873], [873, 874], [873, 876]]}
# gained: {"lines": [865, 867, 868, 870, 871, 873, 874, 876], "branches": [[867, 0], [867, 868], [870, 871], [873, 874]]}

import os
import pytest
from unittest.mock import patch, MagicMock
from ansible.plugins.loader import PluginLoader
from ansible import constants as C

@pytest.fixture
def plugin_loader():
    return PluginLoader(class_name='test_class', package='test_package', config=None, subdir='plugins')

def test_display_plugin_load_debug_enabled(plugin_loader, mocker):
    mocker.patch('ansible.constants.DEFAULT_DEBUG', True)
    mock_display_debug = mocker.patch('ansible.utils.display.Display.debug')

    class_name = 'test_class'
    name = 'test_name'
    searched_paths = ['/path/one', '/path/two']
    path = '/path/to/plugin'
    found_in_cache = True
    class_only = False

    plugin_loader._display_plugin_load(class_name, name, searched_paths, path, found_in_cache, class_only)

    expected_msg = "Loading test_class 'test_name' from /path/to/plugin (searched paths: /path/one:/path/two) (found_in_cache=True, class_only=False)"
    mock_display_debug.assert_called_once_with(expected_msg)

def test_display_plugin_load_debug_disabled(plugin_loader, mocker):
    mocker.patch('ansible.constants.DEFAULT_DEBUG', False)
    mock_display_debug = mocker.patch('ansible.utils.display.Display.debug')

    class_name = 'test_class'
    name = 'test_name'
    searched_paths = ['/path/one']
    path = '/path/to/plugin'
    found_in_cache = None
    class_only = None

    plugin_loader._display_plugin_load(class_name, name, searched_paths, path, found_in_cache, class_only)

    mock_display_debug.assert_not_called()
