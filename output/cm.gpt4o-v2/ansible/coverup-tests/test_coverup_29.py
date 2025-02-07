# file: lib/ansible/cli/vault.py:52-118
# asked: {"lines": [52, 53, 54, 55, 58, 59, 60, 62, 63, 65, 66, 67, 68, 71, 72, 73, 74, 76, 77, 78, 80, 81, 82, 84, 85, 86, 88, 89, 90, 92, 93, 94, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 111, 112, 113, 114, 115, 116, 117, 118], "branches": []}
# gained: {"lines": [52, 53, 54, 55, 58, 59, 60, 62, 63, 65, 66, 67, 68, 71, 72, 73, 74, 76, 77, 78, 80, 81, 82, 84, 85, 86, 88, 89, 90, 92, 93, 94, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 111, 112, 113, 114, 115, 116, 117, 118], "branches": []}

import pytest
from unittest.mock import patch, MagicMock
from ansible.cli.vault import VaultCLI
from ansible import context

@pytest.fixture
def vault_cli():
    cli = VaultCLI(['ansible-vault'])
    cli.parser = MagicMock()
    cli.editor = MagicMock()
    cli.pager = MagicMock()
    return cli

def test_init_parser(vault_cli):
    with patch('ansible.cli.vault.opt_help.argparse.ArgumentParser') as mock_argparse:
        mock_parser = MagicMock()
        mock_argparse.return_value = mock_parser
        vault_cli.init_parser()
        assert mock_parser.add_subparsers.called

def test_execute_create(vault_cli):
    context.CLIARGS = {'args': ['testfile']}
    vault_cli.encrypt_secret = 'secret'
    vault_cli.encrypt_vault_id = 'vault_id'
    vault_cli.execute_create()
    vault_cli.editor.create_file.assert_called_once_with('testfile', 'secret', vault_id='vault_id')

def test_execute_decrypt(vault_cli):
    context.CLIARGS = {'args': ['testfile'], 'output_file': None}
    with patch('sys.stdin.isatty', return_value=True):
        vault_cli.execute_decrypt()
        vault_cli.editor.decrypt_file.assert_called_once_with('testfile', output_file=None)

def test_execute_edit(vault_cli):
    context.CLIARGS = {'args': ['testfile']}
    vault_cli.execute_edit()
    vault_cli.editor.edit_file.assert_called_once_with('testfile')

def test_execute_view(vault_cli):
    context.CLIARGS = {'args': ['testfile']}
    vault_cli.editor.plaintext.return_value = 'plaintext'
    vault_cli.execute_view()
    vault_cli.pager.assert_called_once_with('plaintext')

def test_execute_encrypt(vault_cli):
    context.CLIARGS = {'args': ['testfile'], 'output_file': None}
    vault_cli.encrypt_secret = 'secret'
    vault_cli.encrypt_vault_id = 'vault_id'
    with patch('sys.stdin.isatty', return_value=True):
        vault_cli.execute_encrypt()
        vault_cli.editor.encrypt_file.assert_called_once_with('testfile', 'secret', vault_id='vault_id', output_file=None)

def test_execute_encrypt_string(vault_cli):
    context.CLIARGS = {
        'args': ['string_to_encrypt'],
        'encrypt_string_prompt': False,
        'show_string_input': False,
        'encrypt_string_names': ['var_name'],
        'encrypt_string_stdin_name': None
    }
    vault_cli.encrypt_vault_id = 'vault_id'
    with patch('sys.stdin.isatty', return_value=True):
        with patch('sys.stdin.read', return_value='stdin_text'):
            with patch.object(vault_cli, '_format_output_vault_strings', wraps=vault_cli._format_output_vault_strings) as mock_format_output:
                vault_cli.execute_encrypt_string()
                mock_format_output.assert_called()
                vault_cli.editor.encrypt_bytes.assert_called()

def test_execute_rekey(vault_cli):
    context.CLIARGS = {'args': ['testfile']}
    vault_cli.new_encrypt_secret = 'new_secret'
    vault_cli.new_encrypt_vault_id = 'new_vault_id'
    vault_cli.execute_rekey()
    vault_cli.editor.rekey_file.assert_called_once_with('testfile', 'new_secret', 'new_vault_id')
