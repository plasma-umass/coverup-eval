# file: lib/ansible/cli/vault.py:457-464
# asked: {"lines": [457, 459, 461, 462, 464], "branches": [[459, 461], [459, 464]]}
# gained: {"lines": [457, 459, 461, 462, 464], "branches": [[459, 461], [459, 464]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.cli.vault import VaultCLI
from ansible.utils.context_objects import CLIArgs

@pytest.fixture
def vault_cli():
    args = ['rekey', 'testfile.yml']
    return VaultCLI(args)

def test_execute_rekey(vault_cli, monkeypatch):
    # Mock the necessary attributes and methods
    vault_cli.editor = MagicMock()
    vault_cli.new_encrypt_secret = 'new_secret'
    vault_cli.new_encrypt_vault_id = 'new_vault_id'
    
    # Set the CLIARGS to include a test file
    cliargs = CLIArgs({'args': ['testfile.yml']})
    monkeypatch.setattr('ansible.context.CLIARGS', cliargs)
    
    with patch('ansible.cli.vault.display.display') as mock_display:
        vault_cli.execute_rekey()
        
        # Check that rekey_file was called with the correct parameters
        vault_cli.editor.rekey_file.assert_called_once_with('testfile.yml', 'new_secret', 'new_vault_id')
        
        # Check that the display message was called
        mock_display.assert_called_once_with("Rekey successful", stderr=True)
