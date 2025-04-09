# file lib/ansible/plugins/loader.py:865-876
# lines [868, 870, 871, 873, 874, 876]
# branches ['867->868', '870->871', '870->873', '873->874', '873->876']

import os
import pytest
from unittest.mock import MagicMock

# Assuming the existence of the following within the ansible.plugins.loader module
from ansible.plugins.loader import PluginLoader
from ansible.utils.display import Display
from ansible import constants as C

# Mock the Display class to capture debug messages
@pytest.fixture
def mock_display(mocker):
    display_mock = mocker.patch('ansible.utils.display.Display.debug')
    return display_mock

# Test function to cover lines 868-876
def test_plugin_loader_display_plugin_load(mock_display, mocker):
    # Set the debug constant to True to ensure the debug message is generated
    mocker.patch.object(C, 'DEFAULT_DEBUG', True)

    # Mock the PluginLoader constructor to avoid TypeError
    mocker.patch.object(PluginLoader, '__init__', return_value=None)

    # Create an instance of PluginLoader
    plugin_loader = PluginLoader()

    # Define test data
    class_name = 'TestPlugin'
    name = '/path/to/plugin/test_plugin.py'
    searched_paths = ['/path/to/plugin', '/another/path']
    path = '/path/to/plugin'
    found_in_cache = True
    class_only = False

    # Mock the format_paths method to return a string representation of the paths
    mocker.patch.object(PluginLoader, 'format_paths', return_value=str(searched_paths))

    # Call the method we want to test
    plugin_loader._display_plugin_load(class_name, name, searched_paths, path, found_in_cache, class_only)

    # Construct the expected message
    basename = os.path.basename(name)
    expected_msg = f"Loading {class_name} '{basename}' from {path} (searched paths: {searched_paths}) (found_in_cache={found_in_cache}, class_only={class_only})"

    # Assert that Display.debug was called with the expected message
    mock_display.assert_called_once_with(expected_msg)

    # Clean up by resetting the DEFAULT_DEBUG constant
    mocker.stopall()
