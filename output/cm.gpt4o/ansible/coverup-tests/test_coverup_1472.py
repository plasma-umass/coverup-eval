# file lib/ansible/plugins/loader.py:865-876
# lines []
# branches ['870->873', '873->876']

import pytest
from unittest import mock
from ansible.plugins.loader import PluginLoader
import ansible.constants as C
import os

@pytest.fixture
def mock_display_debug(mocker):
    return mocker.patch('ansible.utils.display.Display.debug')

@pytest.fixture
def plugin_loader():
    class MockPluginLoader(PluginLoader):
        def __init__(self):
            pass

        def format_paths(self, paths):
            return ':'.join(paths)
            
    return MockPluginLoader()

def test_display_plugin_load_with_multiple_searched_paths_and_cache(plugin_loader, mock_display_debug):
    C.DEFAULT_DEBUG = True
    class_name = 'test_class'
    name = 'test_name'
    searched_paths = ['/path/one', '/path/two']
    path = '/path/to/plugin'
    found_in_cache = True
    class_only = True

    plugin_loader._display_plugin_load(class_name, name, searched_paths, path, found_in_cache, class_only)

    expected_msg = (
        "Loading test_class 'test_name' from /path/to/plugin "
        "(searched paths: /path/one:/path/two) "
        "(found_in_cache=True, class_only=True)"
    )
    mock_display_debug.assert_called_once_with(expected_msg)

def test_display_plugin_load_with_multiple_searched_paths_no_cache(plugin_loader, mock_display_debug):
    C.DEFAULT_DEBUG = True
    class_name = 'test_class'
    name = 'test_name'
    searched_paths = ['/path/one', '/path/two']
    path = '/path/to/plugin'
    found_in_cache = False
    class_only = False

    plugin_loader._display_plugin_load(class_name, name, searched_paths, path, found_in_cache, class_only)

    expected_msg = (
        "Loading test_class 'test_name' from /path/to/plugin "
        "(searched paths: /path/one:/path/two)"
    )
    mock_display_debug.assert_called_once_with(expected_msg)

def test_display_plugin_load_with_single_searched_path_and_cache(plugin_loader, mock_display_debug):
    C.DEFAULT_DEBUG = True
    class_name = 'test_class'
    name = 'test_name'
    searched_paths = ['/path/one']
    path = '/path/to/plugin'
    found_in_cache = True
    class_only = True

    plugin_loader._display_plugin_load(class_name, name, searched_paths, path, found_in_cache, class_only)

    expected_msg = (
        "Loading test_class 'test_name' from /path/to/plugin "
        "(found_in_cache=True, class_only=True)"
    )
    mock_display_debug.assert_called_once_with(expected_msg)

def test_display_plugin_load_with_single_searched_path_no_cache(plugin_loader, mock_display_debug):
    C.DEFAULT_DEBUG = True
    class_name = 'test_class'
    name = 'test_name'
    searched_paths = ['/path/one']
    path = '/path/to/plugin'
    found_in_cache = False
    class_only = False

    plugin_loader._display_plugin_load(class_name, name, searched_paths, path, found_in_cache, class_only)

    expected_msg = "Loading test_class 'test_name' from /path/to/plugin"
    mock_display_debug.assert_called_once_with(expected_msg)
