# file: lib/ansible/cli/vault.py:457-464
# asked: {"lines": [457, 459, 461, 462, 464], "branches": [[459, 461], [459, 464]]}
# gained: {"lines": [457, 459, 461, 462, 464], "branches": [[459, 461], [459, 464]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.cli.vault import VaultCLI
from ansible.utils.display import Display

@pytest.fixture
def vault_cli():
    # Provide the required 'args' argument to the VaultCLI constructor
    cli = VaultCLI(args=['rekey'])
    cli.editor = MagicMock()
    cli.new_encrypt_secret = 'new_secret'
    cli.new_encrypt_vault_id = 'new_vault_id'
    return cli

def test_execute_rekey(monkeypatch, vault_cli):
    # Mock context.CLIARGS to provide test arguments
    monkeypatch.setattr('ansible.cli.vault.context.CLIARGS', {'args': ['testfile']})
    
    # Mock the display to capture the output
    display = MagicMock()
    monkeypatch.setattr('ansible.cli.vault.display', display)
    
    # Execute the rekey function
    vault_cli.execute_rekey()
    
    # Assert that rekey_file was called with the correct parameters
    vault_cli.editor.rekey_file.assert_called_once_with('testfile', 'new_secret', 'new_vault_id')
    
    # Assert that the display message was called
    display.display.assert_called_once_with("Rekey successful", stderr=True)
