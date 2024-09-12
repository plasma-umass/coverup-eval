# file: lib/ansible/cli/vault.py:39-50
# asked: {"lines": [39, 41, 42, 43, 45, 46, 47, 48, 50], "branches": []}
# gained: {"lines": [39, 41, 42, 43, 45, 46, 47, 48, 50], "branches": []}

import pytest
from ansible.cli.vault import VaultCLI

@pytest.fixture
def vault_cli():
    args = ['arg1', 'arg2']
    return VaultCLI(args)

def test_vault_cli_initialization(vault_cli):
    assert vault_cli.b_vault_pass is None
    assert vault_cli.b_new_vault_pass is None
    assert vault_cli.encrypt_string_read_stdin is False
    assert vault_cli.encrypt_secret is None
    assert vault_cli.encrypt_vault_id is None
    assert vault_cli.new_encrypt_secret is None
    assert vault_cli.new_encrypt_vault_id is None

def test_vault_cli_super_init(mocker):
    mock_super_init = mocker.patch('ansible.cli.vault.CLI.__init__')
    args = ['arg1', 'arg2']
    vault_cli = VaultCLI(args)
    mock_super_init.assert_called_once_with(args)
