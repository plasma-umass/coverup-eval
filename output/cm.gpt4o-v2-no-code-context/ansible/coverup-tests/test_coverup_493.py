# file: lib/ansible/cli/vault.py:431-438
# asked: {"lines": [431, 434, 435, 437, 438], "branches": [[434, 435], [434, 437]]}
# gained: {"lines": [431, 434, 435, 437, 438], "branches": [[434, 435], [434, 437]]}

import pytest
from ansible.cli.vault import VaultCLI
from ansible.errors import AnsibleOptionsError
from unittest.mock import MagicMock, patch

@pytest.fixture
def vault_cli():
    cli = VaultCLI(args=['dummy'])
    cli.editor = MagicMock()
    cli.encrypt_secret = 'dummy_secret'
    cli.encrypt_vault_id = 'dummy_vault_id'
    return cli

def test_execute_create_with_no_args(vault_cli, monkeypatch):
    monkeypatch.setattr('ansible.cli.vault.context.CLIARGS', {'args': []})
    with pytest.raises(AnsibleOptionsError, match="ansible-vault create can take only one filename argument"):
        vault_cli.execute_create()

def test_execute_create_with_multiple_args(vault_cli, monkeypatch):
    monkeypatch.setattr('ansible.cli.vault.context.CLIARGS', {'args': ['file1', 'file2']})
    with pytest.raises(AnsibleOptionsError, match="ansible-vault create can take only one filename argument"):
        vault_cli.execute_create()

def test_execute_create_with_one_arg(vault_cli, monkeypatch):
    monkeypatch.setattr('ansible.cli.vault.context.CLIARGS', {'args': ['file1']})
    vault_cli.execute_create()
    vault_cli.editor.create_file.assert_called_once_with('file1', 'dummy_secret', vault_id='dummy_vault_id')
