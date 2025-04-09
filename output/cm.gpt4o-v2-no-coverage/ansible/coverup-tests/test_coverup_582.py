# file: lib/ansible/cli/vault.py:431-438
# asked: {"lines": [431, 434, 435, 437, 438], "branches": [[434, 435], [434, 437]]}
# gained: {"lines": [431, 434, 435, 437, 438], "branches": [[434, 435], [434, 437]]}

import pytest
from ansible.errors import AnsibleOptionsError
from ansible.cli.vault import VaultCLI
from unittest.mock import MagicMock, patch

@pytest.fixture
def vault_cli():
    args = ['create']
    return VaultCLI(args)

def test_execute_create_with_invalid_args_length(vault_cli):
    with patch('ansible.context.CLIARGS', {'args': []}):
        with pytest.raises(AnsibleOptionsError, match="ansible-vault create can take only one filename argument"):
            vault_cli.execute_create()

def test_execute_create_with_valid_args_length(vault_cli):
    with patch('ansible.context.CLIARGS', {'args': ['testfile.txt']}):
        vault_cli.editor = MagicMock()
        vault_cli.encrypt_secret = 'secret'
        vault_cli.encrypt_vault_id = 'vault_id'
        
        vault_cli.execute_create()
        
        vault_cli.editor.create_file.assert_called_once_with('testfile.txt', 'secret', vault_id='vault_id')
