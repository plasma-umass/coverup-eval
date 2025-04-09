# file lib/ansible/cli/vault.py:39-50
# lines [39, 41, 42, 43, 45, 46, 47, 48, 50]
# branches []

import pytest
from ansible.cli.vault import VaultCLI

@pytest.fixture
def mock_args(mocker):
    args = mocker.Mock()
    return args

@pytest.fixture
def vault_cli_instance(mock_args):
    return VaultCLI(mock_args)

def test_vault_cli_initialization(vault_cli_instance):
    assert vault_cli_instance.b_vault_pass is None
    assert vault_cli_instance.b_new_vault_pass is None
    assert vault_cli_instance.encrypt_string_read_stdin is False
    assert vault_cli_instance.encrypt_secret is None
    assert vault_cli_instance.encrypt_vault_id is None
    assert vault_cli_instance.new_encrypt_secret is None
    assert vault_cli_instance.new_encrypt_vault_id is None
