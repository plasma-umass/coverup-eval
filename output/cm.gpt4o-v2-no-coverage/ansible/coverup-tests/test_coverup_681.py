# file: lib/ansible/cli/vault.py:440-443
# asked: {"lines": [440, 442, 443], "branches": [[442, 0], [442, 443]]}
# gained: {"lines": [440, 442, 443], "branches": [[442, 0], [442, 443]]}

import pytest
from unittest.mock import MagicMock
from ansible.cli.vault import VaultCLI
from ansible import context

@pytest.fixture
def mock_editor():
    return MagicMock()

@pytest.fixture
def vault_cli(mock_editor):
    cli = VaultCLI(args=['dummy'])
    cli.editor = mock_editor
    return cli

def test_execute_edit(vault_cli, mock_editor, monkeypatch):
    # Setup the context CLIARGS
    monkeypatch.setattr(context, 'CLIARGS', {'args': ['file1', 'file2']})

    # Execute the method
    vault_cli.execute_edit()

    # Assertions to ensure the editor's edit_file method was called with the correct arguments
    mock_editor.edit_file.assert_any_call('file1')
    mock_editor.edit_file.assert_any_call('file2')
    assert mock_editor.edit_file.call_count == 2
