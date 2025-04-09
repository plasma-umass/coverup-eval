# file: lib/ansible/plugins/loader.py:304-305
# asked: {"lines": [304, 305], "branches": []}
# gained: {"lines": [304, 305], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.plugins.loader import PluginLoader

@pytest.fixture
def plugin_loader():
    return PluginLoader(class_name="test_class", package="test_package", config=None, subdir="test_subdir")

def test_print_paths(plugin_loader, mocker):
    mock_format_paths = mocker.patch.object(plugin_loader, 'format_paths', return_value="formatted_paths")
    mock_get_paths = mocker.patch.object(plugin_loader, '_get_paths', return_value="paths")

    result = plugin_loader.print_paths()

    mock_get_paths.assert_called_once_with(subdirs=False)
    mock_format_paths.assert_called_once_with("paths")
    assert result == "formatted_paths"
