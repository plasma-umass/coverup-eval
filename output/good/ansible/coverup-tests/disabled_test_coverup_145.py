# file lib/ansible/cli/doc.py:962-983
# lines [962, 963, 964, 966, 968, 970, 971, 972, 973, 974, 975, 977, 979, 980, 981, 983]
# branches ['964->966', '964->983', '970->971', '970->972', '972->973', '972->974', '974->975', '974->977']

import os
import pytest
from ansible.errors import AnsibleError
from ansible.cli.doc import DocCLI
from ansible.utils.display import Display
from unittest.mock import MagicMock

# Mock the Display class to capture verbose output
display = Display()
display.vvv = MagicMock()

# Create a pytest fixture to mock the PluginLoader
@pytest.fixture
def mock_loader(mocker):
    mock_loader = mocker.MagicMock()
    mock_loader.find_plugin.side_effect = lambda *args, **kwargs: args[0] + ".py"
    return mock_loader

# Test function to improve coverage
def test__get_plugin_list_filenames_exception_handling(mock_loader, mocker):
    mocker.patch('ansible.cli.doc.display', display)
    # Provide a non-empty list for args to avoid ValueError
    doc_cli = DocCLI(['ansible-doc'])
    doc_cli.plugin_list = ['test_plugin']

    # Mock os.path.isdir to return False
    mocker.patch('os.path.isdir', return_value=False)

    # Force an exception when calling find_plugin
    mock_loader.find_plugin.side_effect = Exception("Test exception")

    with pytest.raises(AnsibleError) as excinfo:
        doc_cli._get_plugin_list_filenames(mock_loader)

    assert "Failed reading docs at test_plugin" in str(excinfo.value)
    assert "Test exception" in str(excinfo.value)
    # Check if the verbose output was captured
    display.vvv.assert_called_once()

    # Cleanup: Unpatch the display
    mocker.stopall()
