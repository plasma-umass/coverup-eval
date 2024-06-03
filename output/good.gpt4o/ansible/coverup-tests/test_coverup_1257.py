# file lib/ansible/cli/doc.py:962-983
# lines [971]
# branches ['970->971']

import pytest
from unittest.mock import MagicMock, patch

# Assuming the necessary imports and setup for the test environment are done here

@pytest.fixture
def doc_cli(mocker):
    from ansible.cli.doc import DocCLI
    mock_args = mocker.MagicMock()
    return DocCLI(mock_args)

def test_get_plugin_list_filenames_handles_none_filename(doc_cli, mocker):
    loader = mocker.MagicMock()
    loader.find_plugin = mocker.MagicMock(return_value=None)
    doc_cli.plugin_list = ['test_plugin']

    result = doc_cli._get_plugin_list_filenames(loader)

    assert result == {}
    loader.find_plugin.assert_called_once_with('test_plugin', mod_type='.py', ignore_deprecated=True, check_aliases=True)
