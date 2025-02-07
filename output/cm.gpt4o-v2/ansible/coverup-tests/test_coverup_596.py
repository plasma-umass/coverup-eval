# file: lib/ansible/cli/vault.py:445-455
# asked: {"lines": [445, 448, 454, 455], "branches": [[448, 0], [448, 454]]}
# gained: {"lines": [445, 448, 454, 455], "branches": [[448, 0], [448, 454]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible import context
from ansible.cli.vault import VaultCLI

@pytest.fixture
def vault_cli():
    args = MagicMock()
    cli = VaultCLI(args)
    cli.editor = MagicMock()
    return cli

def test_execute_view(vault_cli, monkeypatch):
    # Mock the context.CLIARGS to provide test arguments
    monkeypatch.setattr(context, 'CLIARGS', {'args': ['testfile']})

    # Mock the editor.plaintext method
    mock_plaintext = MagicMock(return_value=b'secret data')
    vault_cli.editor.plaintext = mock_plaintext

    # Mock the pager method
    mock_pager = MagicMock()
    monkeypatch.setattr(vault_cli, 'pager', mock_pager)

    # Execute the method
    vault_cli.execute_view()

    # Assertions to verify the expected behavior
    mock_plaintext.assert_called_once_with('testfile')
    mock_pager.assert_called_once_with('secret data')
