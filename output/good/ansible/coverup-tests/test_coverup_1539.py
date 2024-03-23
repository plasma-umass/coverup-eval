# file lib/ansible/cli/doc.py:962-983
# lines [963, 964, 966, 968, 970, 971, 972, 973, 974, 975, 977, 979, 980, 981, 983]
# branches ['964->966', '964->983', '970->971', '970->972', '972->973', '972->974', '974->975', '974->977']

import os
import pytest
from ansible.errors import AnsibleError
from ansible.cli.doc import DocCLI
from ansible.plugins.loader import PluginLoader
from unittest.mock import MagicMock

# Define a test case to cover the missing lines in DocCLI._get_plugin_list_filenames
def test_get_plugin_list_filenames_exception(mocker):
    mocker.patch('os.path.isdir', return_value=False)
    mocker.patch('traceback.format_exc', return_value="Mocked traceback")
    display_mock = mocker.patch('ansible.cli.doc.display')
    
    # Mock the PluginLoader to raise an exception when find_plugin is called
    mock_loader = MagicMock(spec=PluginLoader)
    mock_loader.find_plugin.side_effect = Exception("Mocked exception")
    
    # Provide a non-empty list to DocCLI to avoid ValueError
    doc_cli = DocCLI(['ansible-doc', 'test_plugin'])
    doc_cli.plugin_list = ['test_plugin']
    
    # Expect AnsibleError to be raised due to the mocked exception
    with pytest.raises(AnsibleError) as excinfo:
        doc_cli._get_plugin_list_filenames(mock_loader)
    
    # Verify that the exception message matches the expected output
    assert "Failed reading docs at test_plugin: Mocked exception" in str(excinfo.value)
    
    # Verify that the verbose display was called with the mocked traceback
    display_mock.vvv.assert_called_once_with("Mocked traceback")

# Clean up any created files or state here if necessary
