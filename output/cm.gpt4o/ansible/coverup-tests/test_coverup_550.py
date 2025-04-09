# file lib/ansible/cli/vault.py:431-438
# lines [431, 434, 435, 437, 438]
# branches ['434->435', '434->437']

import pytest
from unittest import mock
from ansible.cli.vault import VaultCLI
from ansible.errors import AnsibleOptionsError
from ansible import context

@pytest.fixture
def mock_editor():
    return mock.Mock()

@pytest.fixture
def vault_cli(mock_editor):
    cli = VaultCLI(args=['test'])
    cli.editor = mock_editor
    return cli

def test_execute_create_with_no_args(vault_cli):
    context.CLIARGS = {'args': []}
    with pytest.raises(AnsibleOptionsError, match="ansible-vault create can take only one filename argument"):
        vault_cli.execute_create()

def test_execute_create_with_multiple_args(vault_cli):
    context.CLIARGS = {'args': ['file1', 'file2']}
    with pytest.raises(AnsibleOptionsError, match="ansible-vault create can take only one filename argument"):
        vault_cli.execute_create()

def test_execute_create_with_one_arg(vault_cli):
    context.CLIARGS = {'args': ['file1']}
    vault_cli.encrypt_secret = 'secret'
    vault_cli.encrypt_vault_id = 'vault_id'
    
    vault_cli.execute_create()
    
    vault_cli.editor.create_file.assert_called_once_with('file1', 'secret', vault_id='vault_id')
