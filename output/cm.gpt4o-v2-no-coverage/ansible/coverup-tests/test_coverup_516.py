# file: lib/ansible/cli/vault.py:39-50
# asked: {"lines": [39, 41, 42, 43, 45, 46, 47, 48, 50], "branches": []}
# gained: {"lines": [39, 41, 42, 43, 45, 46, 47, 48, 50], "branches": []}

import pytest
from ansible.cli.vault import VaultCLI
from ansible.cli import CLI

class MockCLI(CLI):
    def __init__(self, args, callback=None):
        if not args:
            raise ValueError('A non-empty list for args is required')
        self.args = args
        self.parser = None
        self.callback = callback

@pytest.fixture
def mock_cli(monkeypatch):
    monkeypatch.setattr("ansible.cli.vault.CLI", MockCLI)

def test_vault_cli_initialization(mock_cli):
    args = ["arg1", "arg2"]
    vault_cli = VaultCLI(args)
    
    assert vault_cli.b_vault_pass is None
    assert vault_cli.b_new_vault_pass is None
    assert vault_cli.encrypt_string_read_stdin is False
    assert vault_cli.encrypt_secret is None
    assert vault_cli.encrypt_vault_id is None
    assert vault_cli.new_encrypt_secret is None
    assert vault_cli.new_encrypt_vault_id is None
    assert vault_cli.args == args
    assert vault_cli.parser is None
    assert vault_cli.callback is None

def test_vault_cli_initialization_no_args(mock_cli):
    with pytest.raises(ValueError, match='A non-empty list for args is required'):
        VaultCLI([])
