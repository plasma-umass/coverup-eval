# file lib/ansible/cli/vault.py:419-429
# lines [419, 422, 423, 425, 426, 428, 429]
# branches ['422->423', '422->425', '425->426', '425->428', '428->exit', '428->429']

import pytest
from unittest import mock
from ansible.cli.vault import VaultCLI
from ansible.utils.display import Display

@pytest.fixture
def mock_context(mocker):
    context = mocker.patch('ansible.cli.vault.context')
    context.CLIARGS = {'args': [], 'output_file': None}
    return context

@pytest.fixture
def mock_display(mocker):
    display = mocker.patch('ansible.cli.vault.display', autospec=True)
    return display

@pytest.fixture
def mock_editor(mocker):
    editor = mocker.Mock()
    return editor

@pytest.fixture
def vault_cli(mock_context, mock_editor):
    cli = VaultCLI(['dummy_arg'])
    cli.editor = mock_editor
    return cli

def test_execute_decrypt_no_args_stdin_tty(mocker, vault_cli, mock_context, mock_display):
    mocker.patch('sys.stdin.isatty', return_value=True)
    mocker.patch('sys.stdout.isatty', return_value=True)
    
    vault_cli.execute_decrypt()
    
    mock_display.display.assert_any_call("Reading ciphertext input from stdin", stderr=True)
    mock_display.display.assert_any_call("Decryption successful", stderr=True)
    vault_cli.editor.decrypt_file.assert_called_once_with('-', output_file=None)

def test_execute_decrypt_with_args(mocker, vault_cli, mock_context, mock_display):
    mock_context.CLIARGS['args'] = ['testfile']
    mocker.patch('sys.stdin.isatty', return_value=True)
    mocker.patch('sys.stdout.isatty', return_value=True)
    
    vault_cli.execute_decrypt()
    
    mock_display.display.assert_called_once_with("Decryption successful", stderr=True)
    vault_cli.editor.decrypt_file.assert_called_once_with('testfile', output_file=None)
