# file lib/ansible/plugins/loader.py:865-876
# lines [868, 870, 871, 873, 874, 876]
# branches ['867->868', '870->871', '870->873', '873->874', '873->876']

import pytest
from unittest import mock
import os
from ansible.plugins.loader import PluginLoader
from ansible.utils.display import Display

@pytest.fixture
def mock_display_debug(mocker):
    return mocker.patch.object(Display, 'debug')

@pytest.fixture
def plugin_loader(mocker):
    mocker.patch('ansible.constants.DEFAULT_DEBUG', True)
    return PluginLoader(class_name='test_class', package='test_package', config='test_config', subdir='test_subdir')

def test_display_plugin_load_debug(mock_display_debug, plugin_loader):
    class_name = 'test_class'
    name = '/path/to/plugin'
    searched_paths = ['/path/one', '/path/two']
    path = '/path/to/plugin'
    found_in_cache = True
    class_only = True

    plugin_loader._display_plugin_load(class_name, name, searched_paths, path, found_in_cache, class_only)

    expected_msg = (
        "Loading test_class 'plugin' from /path/to/plugin "
        "(searched paths: /path/one:/path/two) "
        "(found_in_cache=True, class_only=True)"
    )
    mock_display_debug.assert_called_once_with(expected_msg)
