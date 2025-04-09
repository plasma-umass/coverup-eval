# file lib/ansible/cli/vault.py:39-50
# lines [39, 41, 42, 43, 45, 46, 47, 48, 50]
# branches []

import pytest
from ansible.cli.vault import VaultCLI

def test_vault_cli_initialization():
    args = ['arg1', 'arg2']
    vault_cli = VaultCLI(args)
    
    assert vault_cli.b_vault_pass is None
    assert vault_cli.b_new_vault_pass is None
    assert vault_cli.encrypt_string_read_stdin is False
    assert vault_cli.encrypt_secret is None
    assert vault_cli.encrypt_vault_id is None
    assert vault_cli.new_encrypt_secret is None
    assert vault_cli.new_encrypt_vault_id is None
    assert vault_cli.args == args
