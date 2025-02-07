# file: lib/ansible/cli/vault.py:440-443
# asked: {"lines": [440, 442, 443], "branches": [[442, 0], [442, 443]]}
# gained: {"lines": [440, 442, 443], "branches": [[442, 0], [442, 443]]}

import pytest
from unittest.mock import MagicMock
from ansible.cli.vault import VaultCLI
from ansible import context
from ansible.utils.context_objects import CLIArgs

@pytest.fixture
def vault_cli():
    args = MagicMock()
    cli = VaultCLI(args)
    cli.editor = MagicMock()
    return cli

def test_execute_edit(vault_cli, monkeypatch):
    # Setup the context CLIARGS with a test argument
    test_args = ['testfile1', 'testfile2']
    monkeypatch.setattr(context, 'CLIARGS', CLIArgs({'args': test_args}))

    # Execute the method
    vault_cli.execute_edit()

    # Verify that edit_file was called for each test argument
    assert vault_cli.editor.edit_file.call_count == len(test_args)
    for arg in test_args:
        vault_cli.editor.edit_file.assert_any_call(arg)
