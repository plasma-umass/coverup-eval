# file httpie/output/processing.py:26-53
# lines []
# branches ['41->39']

import pytest
from unittest.mock import MagicMock, patch
from httpie.output.processing import Formatting

@pytest.fixture
def mock_plugin_manager():
    with patch('httpie.output.processing.plugin_manager') as mock_plugin_manager:
        yield mock_plugin_manager

@pytest.fixture
def mock_environment():
    with patch('httpie.output.processing.Environment') as mock_environment:
        yield mock_environment

def test_formatting_with_disabled_plugin(mock_plugin_manager, mock_environment):
    # Mock the plugin class and its instance
    mock_plugin_class = MagicMock()
    mock_plugin_instance = MagicMock()
    mock_plugin_instance.enabled = False  # Ensure the plugin is disabled
    mock_plugin_class.return_value = mock_plugin_instance

    # Mock the plugin manager to return the mock plugin class
    mock_plugin_manager.get_formatters_grouped.return_value = {
        'test_group': [mock_plugin_class]
    }

    # Create a Formatting instance with the test group
    formatting = Formatting(groups=['test_group'], env=mock_environment)

    # Assert that the disabled plugin was not added to enabled_plugins
    assert len(formatting.enabled_plugins) == 0

    # Clean up
    mock_plugin_manager.reset_mock()
    mock_environment.reset_mock()
