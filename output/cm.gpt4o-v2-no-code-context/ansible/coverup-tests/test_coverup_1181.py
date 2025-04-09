# file: lib/ansible/cli/vault.py:440-443
# asked: {"lines": [442, 443], "branches": [[442, 0], [442, 443]]}
# gained: {"lines": [442, 443], "branches": [[442, 0], [442, 443]]}

import pytest
from unittest.mock import MagicMock, patch

# Assuming the VaultCLI class and context are imported from ansible.cli.vault
from ansible.cli.vault import VaultCLI
from ansible import context

@pytest.fixture
def setup_vault_cli(monkeypatch):
    # Mocking the required arguments for VaultCLI initialization
    mock_args = MagicMock()
    monkeypatch.setattr(context, 'CLIARGS', {'args': []})
    cli = VaultCLI(mock_args)
    cli.editor = MagicMock()
    return cli

def test_execute_edit_with_args(setup_vault_cli, monkeypatch):
    cli = setup_vault_cli
    test_args = ['file1', 'file2']
    
    # Mocking context.CLIARGS to include test arguments
    monkeypatch.setattr(context, 'CLIARGS', {'args': test_args})
    
    cli.execute_edit()
    
    # Assert that edit_file was called for each file in test_args
    for f in test_args:
        cli.editor.edit_file.assert_any_call(f)
    
    # Assert that edit_file was called exactly the number of times as the length of test_args
    assert cli.editor.edit_file.call_count == len(test_args)
