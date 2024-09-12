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
    cli.plugin_list = {'test_plugin'}
    return cli

def test_get_plugin_list_filenames_directory(mock_loader, doc_cli):
    mock_loader.find_plugin.return_value = '/path/to/directory'
    
    with patch('os.path.isdir', return_value=True):
        result = doc_cli._get_plugin_list_filenames(mock_loader)
    
    assert result == {}

def test_get_plugin_list_filenames_not_directory(mock_loader, doc_cli):
    mock_loader.find_plugin.return_value = '/path/to/file.py'
    
    with patch('os.path.isdir', return_value=False):
        result = doc_cli._get_plugin_list_filenames(mock_loader)
    
    assert result == {'test_plugin': '/path/to/file.py'}

def test_get_plugin_list_filenames_exception(mock_loader, doc_cli):
    mock_loader.find_plugin.side_effect = Exception('Test exception')
    
    with patch('ansible.cli.doc.display.vvv') as mock_display:
        with pytest.raises(AnsibleError, match="Failed reading docs at test_plugin: Test exception"):
            doc_cli._get_plugin_list_filenames(mock_loader)
    
    mock_display.assert_called_once()
