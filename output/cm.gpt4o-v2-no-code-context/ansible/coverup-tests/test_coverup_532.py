# file: lib/ansible/cli/vault.py:445-455
# asked: {"lines": [445, 448, 454, 455], "branches": [[448, 0], [448, 454]]}
# gained: {"lines": [445, 448, 454, 455], "branches": [[448, 0], [448, 454]]}

import pytest
from unittest.mock import MagicMock, patch

# Assuming the VaultCLI class is imported from ansible.cli.vault
from ansible.cli.vault import VaultCLI

@pytest.fixture
def vault_cli():
    cli = VaultCLI(args=['view'])
    cli.editor = MagicMock()
    cli.pager = MagicMock()
    return cli

def test_execute_view(monkeypatch, vault_cli):
    # Mock the context.CLIARGS to provide test arguments
    monkeypatch.setattr('ansible.cli.vault.context.CLIARGS', {'args': ['testfile']})

    # Mock the plaintext method to return a test string
    vault_cli.editor.plaintext.return_value = b'test plaintext'

    with patch('ansible.cli.vault.to_text', return_value='test plaintext'):
        vault_cli.execute_view()

    # Assertions to verify the expected behavior
    vault_cli.editor.plaintext.assert_called_once_with('testfile')
    vault_cli.pager.assert_called_once_with('test plaintext')
