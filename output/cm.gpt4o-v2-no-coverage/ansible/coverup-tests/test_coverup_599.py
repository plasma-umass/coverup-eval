# file: lib/ansible/cli/vault.py:457-464
# asked: {"lines": [457, 459, 461, 462, 464], "branches": [[459, 461], [459, 464]]}
# gained: {"lines": [457, 459, 461, 462, 464], "branches": [[459, 461], [459, 464]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.cli.vault import VaultCLI
from ansible import context

@pytest.fixture
def mock_context():
    with patch('ansible.context.CLIARGS', {'args': ['file1', 'file2']}):
        yield

@pytest.fixture
def vault_cli():
    args = MagicMock()
    cli = VaultCLI(args)
    cli.editor = MagicMock()
    cli.new_encrypt_secret = 'new_secret'
    cli.new_encrypt_vault_id = 'new_vault_id'
    return cli

def test_execute_rekey(vault_cli, mock_context):
    with patch('ansible.cli.vault.display.display') as mock_display:
        vault_cli.execute_rekey()
        assert vault_cli.editor.rekey_file.call_count == 2
        vault_cli.editor.rekey_file.assert_any_call('file1', 'new_secret', 'new_vault_id')
        vault_cli.editor.rekey_file.assert_any_call('file2', 'new_secret', 'new_vault_id')
        mock_display.assert_called_once_with('Rekey successful', stderr=True)
