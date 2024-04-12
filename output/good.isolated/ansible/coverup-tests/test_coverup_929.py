# file lib/ansible/plugins/loader.py:806-807
# lines [806, 807]
# branches []

import pytest
from ansible.plugins.loader import PluginLoader

# Assuming the PluginLoader class has a get_with_context method that we need to mock
# and that it returns an object with an 'object' attribute.
# Also assuming that PluginLoader requires 'class_name', 'package', 'config', and 'subdir' arguments for initialization.

def test_plugin_loader_get(mocker):
    # Mock the get_with_context method
    mock_get_with_context = mocker.patch.object(PluginLoader, 'get_with_context')
    # Create a mock object to be returned by get_with_context
    mock_plugin = mocker.Mock()
    mock_plugin.object = 'mocked_plugin_object'
    mock_get_with_context.return_value = mock_plugin

    # Mock the required arguments for PluginLoader initialization
    class_name = 'MockClassName'
    package = 'mock_package'
    config = 'mock_config'
    subdir = 'mock_subdir'

    # Instantiate the PluginLoader with mocked arguments
    loader = PluginLoader(class_name, package, config, subdir)

    # Call the get method
    result = loader.get('test_plugin_name')

    # Assert that get_with_context was called with the correct arguments
    mock_get_with_context.assert_called_once_with('test_plugin_name')

    # Assert that the result is what we expect
    assert result == 'mocked_plugin_object', "The get method did not return the expected object"
