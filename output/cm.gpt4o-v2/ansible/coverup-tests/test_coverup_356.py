# file: lib/ansible/cli/vault.py:419-429
# asked: {"lines": [419, 422, 423, 425, 426, 428, 429], "branches": [[422, 423], [422, 425], [425, 426], [425, 428], [428, 0], [428, 429]]}
# gained: {"lines": [419, 422, 423, 425, 426, 428, 429], "branches": [[422, 423], [422, 425], [425, 426], [425, 428], [428, 0], [428, 429]]}

import pytest
import sys
from unittest.mock import patch, MagicMock
from ansible import context
from ansible.cli.vault import VaultCLI

@pytest.fixture
def vault_cli():
    cli = VaultCLI(['test'])
    cli.editor = MagicMock()
    return cli

def test_execute_decrypt_no_args_tty(mocker, vault_cli):
    mocker.patch.object(context, 'CLIARGS', {'args': [], 'output_file': None})
    mocker.patch('sys.stdin.isatty', return_value=True)
    mocker.patch('sys.stdout.isatty', return_value=True)
    mock_display = mocker.patch('ansible.cli.vault.display.display')
    
    vault_cli.execute_decrypt()
    
    mock_display.assert_any_call('Reading ciphertext input from stdin', stderr=True)
    vault_cli.editor.decrypt_file.assert_called_once_with('-', output_file=None)
    mock_display.assert_any_call('Decryption successful', stderr=True)

def test_execute_decrypt_with_args(mocker, vault_cli):
    mocker.patch.object(context, 'CLIARGS', {'args': ['file1', 'file2'], 'output_file': 'output'})
    mocker.patch('sys.stdin.isatty', return_value=False)
    mocker.patch('sys.stdout.isatty', return_value=True)
    mock_display = mocker.patch('ansible.cli.vault.display.display')
    
    vault_cli.execute_decrypt()
    
    vault_cli.editor.decrypt_file.assert_any_call('file1', output_file='output')
    vault_cli.editor.decrypt_file.assert_any_call('file2', output_file='output')
    mock_display.assert_any_call('Decryption successful', stderr=True)

def test_execute_decrypt_no_tty(mocker, vault_cli):
    mocker.patch.object(context, 'CLIARGS', {'args': [], 'output_file': None})
    mocker.patch('sys.stdin.isatty', return_value=False)
    mocker.patch('sys.stdout.isatty', return_value=False)
    mock_display = mocker.patch('ansible.cli.vault.display.display')
    
    vault_cli.execute_decrypt()
    
    mock_display.assert_not_called()
    vault_cli.editor.decrypt_file.assert_called_once_with('-', output_file=None)
