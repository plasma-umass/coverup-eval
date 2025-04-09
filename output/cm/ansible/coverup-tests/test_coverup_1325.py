# file lib/ansible/cli/vault.py:457-464
# lines [459, 461, 462, 464]
# branches ['459->461', '459->464']

import pytest
from unittest.mock import MagicMock
from ansible.cli.vault import VaultCLI
from ansible.utils.display import Display

@pytest.fixture
def mock_display(mocker):
    display = Display()
    mocker.patch.object(display, 'display')
    return display

@pytest.fixture
def vault_cli(mocker, mock_display):
    mocker.patch('ansible.cli.vault.VaultEditor')
    mocker.patch('ansible.cli.vault.CLI')
    mocker.patch('ansible.cli.vault.context.CLIARGS', {'args': ['vault_file.yml']})
    vault_cli = VaultCLI(mock_display)
    vault_cli.editor = MagicMock()
    vault_cli.new_encrypt_secret = 'new_secret'
    vault_cli.new_encrypt_vault_id = 'new_vault_id'
    return vault_cli

def test_execute_rekey(vault_cli, mock_display):
    vault_cli.execute_rekey()
    vault_cli.editor.rekey_file.assert_called_once_with('vault_file.yml', 'new_secret', 'new_vault_id')
    mock_display.display.assert_called_once_with("Rekey successful", stderr=True)
