# file: lib/ansible/cli/vault.py:445-455
# asked: {"lines": [448, 454, 455], "branches": [[448, 0], [448, 454]]}
# gained: {"lines": [448, 454, 455], "branches": [[448, 0], [448, 454]]}

import pytest
from unittest.mock import MagicMock
from ansible.cli.vault import VaultCLI
from ansible.utils.context_objects import CLIArgs
from ansible import context
from ansible.module_utils._text import to_text

@pytest.fixture
def vault_cli():
    args = MagicMock()
    cli = VaultCLI(args)
    cli.editor = MagicMock()
    return cli

def test_execute_view(mocker, vault_cli):
    # Mock the context CLIARGS
    mocker.patch.object(context, 'CLIARGS', CLIArgs({'args': ['fake_file']}))
    
    # Mock the editor.plaintext method
    mock_plaintext = mocker.patch.object(vault_cli.editor, 'plaintext', return_value=b'secret data')
    
    # Mock the pager method
    mock_pager = mocker.patch.object(vault_cli, 'pager')
    
    # Execute the method
    vault_cli.execute_view()
    
    # Assertions
    mock_plaintext.assert_called_once_with('fake_file')
    mock_pager.assert_called_once_with(to_text(b'secret data'))
