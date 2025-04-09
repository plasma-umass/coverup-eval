# file: lib/ansible/cli/doc.py:962-983
# asked: {"lines": [975], "branches": [[974, 975]]}
# gained: {"lines": [975], "branches": [[974, 975]]}

import os
import pytest
from unittest.mock import Mock, patch
from ansible.errors import AnsibleError
from ansible.cli.doc import DocCLI

@pytest.fixture
def mock_loader():
    return Mock()

@pytest.fixture
def doc_cli():
    args = Mock()
    cli = DocCLI(args)
    cli.plugin_list = {'plugin1', 'plugin2'}
    return cli

def test_get_plugin_list_filenames_handles_directory(mock_loader, doc_cli):
    mock_loader.find_plugin.side_effect = [
        '/path/to/plugin1',  # Not a directory
        '/path/to/plugin2'   # Directory
    ]

    with patch('os.path.isdir', side_effect=lambda x: x == '/path/to/plugin2'):
        result = doc_cli._get_plugin_list_filenames(mock_loader)

    assert 'plugin1' in result
    assert 'plugin2' not in result
    assert result['plugin1'] == '/path/to/plugin1'

def test_get_plugin_list_filenames_handles_exceptions(mock_loader, doc_cli):
    mock_loader.find_plugin.side_effect = Exception("Test exception")

    with patch('ansible.cli.doc.display.vvv'), pytest.raises(AnsibleError, match="Failed reading docs at plugin1: Test exception"):
        doc_cli._get_plugin_list_filenames(mock_loader)
