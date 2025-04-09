# file: lib/ansible/cli/vault.py:247-260
# asked: {"lines": [247, 250, 251, 253, 255, 256, 257, 259, 260], "branches": [[250, 251], [250, 253], [253, 255], [253, 259], [259, 0], [259, 260]]}
# gained: {"lines": [247, 250, 251, 253, 255, 256, 257, 259, 260], "branches": [[250, 251], [250, 253], [253, 255], [253, 259], [259, 0], [259, 260]]}

import pytest
import sys
from unittest.mock import MagicMock, patch

# Assuming the necessary imports and context setup
from ansible.cli.vault import VaultCLI
from ansible.utils.display import Display

@pytest.fixture
def vault_cli(mocker):
    mocker.patch('ansible.cli.vault.context.CLIARGS', {'args': [], 'output_file': None})
    cli = VaultCLI(['ansible-vault'])
    cli.editor = MagicMock()
    cli.encrypt_secret = 'secret'
    cli.encrypt_vault_id = 'vault_id'
    return cli

def test_execute_encrypt_no_args_tty(mocker, vault_cli):
    mocker.patch('sys.stdin.isatty', return_value=True)
    mocker.patch('sys.stdout.isatty', return_value=True)
    mocker.patch('ansible.cli.vault.context.CLIARGS', {'args': [], 'output_file': None})
    display_mock = mocker.patch('ansible.utils.display.Display.display')

    vault_cli.execute_encrypt()

    display_mock.assert_any_call("Reading plaintext input from stdin", stderr=True)
    vault_cli.editor.encrypt_file.assert_called_once_with('-', 'secret', vault_id='vault_id', output_file=None)
    display_mock.assert_any_call("Encryption successful", stderr=True)

def test_execute_encrypt_with_args_tty(mocker, vault_cli):
    mocker.patch('sys.stdin.isatty', return_value=True)
    mocker.patch('sys.stdout.isatty', return_value=True)
    mocker.patch('ansible.cli.vault.context.CLIARGS', {'args': ['file1'], 'output_file': None})
    display_mock = mocker.patch('ansible.utils.display.Display.display')

    vault_cli.execute_encrypt()

    vault_cli.editor.encrypt_file.assert_called_once_with('file1', 'secret', vault_id='vault_id', output_file=None)
    display_mock.assert_any_call("Encryption successful", stderr=True)

def test_execute_encrypt_no_tty(mocker, vault_cli):
    mocker.patch('sys.stdin.isatty', return_value=False)
    mocker.patch('sys.stdout.isatty', return_value=False)
    mocker.patch('ansible.cli.vault.context.CLIARGS', {'args': ['file1'], 'output_file': None})
    display_mock = mocker.patch('ansible.utils.display.Display.display')

    vault_cli.execute_encrypt()

    vault_cli.editor.encrypt_file.assert_called_once_with('file1', 'secret', vault_id='vault_id', output_file=None)
    display_mock.assert_not_called()
