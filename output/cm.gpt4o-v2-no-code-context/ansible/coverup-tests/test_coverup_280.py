# file: lib/ansible/cli/vault.py:419-429
# asked: {"lines": [419, 422, 423, 425, 426, 428, 429], "branches": [[422, 423], [422, 425], [425, 426], [425, 428], [428, 0], [428, 429]]}
# gained: {"lines": [419, 422, 423, 425, 426, 428, 429], "branches": [[422, 423], [422, 425], [425, 426], [425, 428], [428, 0], [428, 429]]}

import pytest
from unittest import mock
from ansible.cli.vault import VaultCLI
from ansible.utils.display import Display

@pytest.fixture
def vault_cli(mocker):
    mock_args = mocker.Mock()
    return VaultCLI(mock_args)

@pytest.fixture
def mock_context(mocker):
    return mocker.patch('ansible.cli.vault.context')

@pytest.fixture
def mock_display(mocker):
    return mocker.patch('ansible.cli.vault.display')

@pytest.fixture
def mock_sys(mocker):
    return mocker.patch('ansible.cli.vault.sys')

def test_execute_decrypt_no_args_tty(vault_cli, mock_context, mock_display, mock_sys):
    mock_context.CLIARGS = {'args': [], 'output_file': None}
    mock_sys.stdin.isatty.return_value = True
    mock_sys.stdout.isatty.return_value = True
    vault_cli.editor = mock.Mock()

    vault_cli.execute_decrypt()

    mock_display.display.assert_any_call("Reading ciphertext input from stdin", stderr=True)
    vault_cli.editor.decrypt_file.assert_called_once_with('-', output_file=None)
    mock_display.display.assert_any_call("Decryption successful", stderr=True)

def test_execute_decrypt_with_args_tty(vault_cli, mock_context, mock_display, mock_sys):
    mock_context.CLIARGS = {'args': ['file1'], 'output_file': None}
    mock_sys.stdin.isatty.return_value = True
    mock_sys.stdout.isatty.return_value = True
    vault_cli.editor = mock.Mock()

    vault_cli.execute_decrypt()

    vault_cli.editor.decrypt_file.assert_called_once_with('file1', output_file=None)
    mock_display.display.assert_any_call("Decryption successful", stderr=True)

def test_execute_decrypt_no_args_no_tty(vault_cli, mock_context, mock_display, mock_sys):
    mock_context.CLIARGS = {'args': [], 'output_file': None}
    mock_sys.stdin.isatty.return_value = False
    mock_sys.stdout.isatty.return_value = False
    vault_cli.editor = mock.Mock()

    vault_cli.execute_decrypt()

    vault_cli.editor.decrypt_file.assert_called_once_with('-', output_file=None)
    mock_display.display.assert_not_called()

def test_execute_decrypt_with_args_no_tty(vault_cli, mock_context, mock_display, mock_sys):
    mock_context.CLIARGS = {'args': ['file1'], 'output_file': None}
    mock_sys.stdin.isatty.return_value = False
    mock_sys.stdout.isatty.return_value = False
    vault_cli.editor = mock.Mock()

    vault_cli.execute_decrypt()

    vault_cli.editor.decrypt_file.assert_called_once_with('file1', output_file=None)
    mock_display.display.assert_not_called()
