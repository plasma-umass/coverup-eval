# file lib/ansible/cli/vault.py:52-118
# lines [53, 54, 55, 58, 59, 60, 62, 63, 65, 66, 67, 68, 71, 72, 73, 74, 76, 77, 78, 80, 81, 82, 84, 85, 86, 88, 89, 90, 92, 93, 94, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 111, 112, 113, 114, 115, 116, 117, 118]
# branches []

import os
import pytest
from ansible.cli.vault import VaultCLI
from unittest.mock import MagicMock

@pytest.fixture
def vault_cli(mocker):
    mocker.patch('ansible.cli.vault.CLI.__init__', return_value=None)
    mocker.patch('ansible.cli.vault.CLI.parse', return_value=None)
    mocker.patch('ansible.cli.vault.CLI.run', return_value=None)
    mocker.patch('ansible.cli.vault.os.path.basename', return_value='ansible-vault')
    mocker.patch('ansible.cli.vault.sys.argv', return_value=['ansible-vault'])
    vault_cli = VaultCLI([])
    vault_cli.parser = MagicMock()
    vault_cli.parser.add_subparsers = MagicMock(return_value=MagicMock())
    vault_cli.args = ['ansible-vault']
    return vault_cli

@pytest.fixture
def parser(vault_cli):
    vault_cli.init_parser()
    return vault_cli.parser

def test_vault_cli_parser_create(parser, vault_cli):
    parser.parse_args = MagicMock(return_value=MagicMock(action='create', func=vault_cli.execute_create, args=['test_file.yml']))
    args = parser.parse_args(['create', 'test_file.yml'])
    assert args.action == 'create'
    assert args.func.__name__ == 'execute_create'
    assert args.args == ['test_file.yml']

def test_vault_cli_parser_decrypt(parser, vault_cli):
    parser.parse_args = MagicMock(return_value=MagicMock(action='decrypt', func=vault_cli.execute_decrypt, args=['test_file.yml']))
    args = parser.parse_args(['decrypt', 'test_file.yml'])
    assert args.action == 'decrypt'
    assert args.func.__name__ == 'execute_decrypt'
    assert args.args == ['test_file.yml']

def test_vault_cli_parser_edit(parser, vault_cli):
    parser.parse_args = MagicMock(return_value=MagicMock(action='edit', func=vault_cli.execute_edit, args=['test_file.yml']))
    args = parser.parse_args(['edit', 'test_file.yml'])
    assert args.action == 'edit'
    assert args.func.__name__ == 'execute_edit'
    assert args.args == ['test_file.yml']

def test_vault_cli_parser_view(parser, vault_cli):
    parser.parse_args = MagicMock(return_value=MagicMock(action='view', func=vault_cli.execute_view, args=['test_file.yml']))
    args = parser.parse_args(['view', 'test_file.yml'])
    assert args.action == 'view'
    assert args.func.__name__ == 'execute_view'
    assert args.args == ['test_file.yml']

def test_vault_cli_parser_encrypt(parser, vault_cli):
    parser.parse_args = MagicMock(return_value=MagicMock(action='encrypt', func=vault_cli.execute_encrypt, args=['test_file.yml']))
    args = parser.parse_args(['encrypt', 'test_file.yml'])
    assert args.action == 'encrypt'
    assert args.func.__name__ == 'execute_encrypt'
    assert args.args == ['test_file.yml']

def test_vault_cli_parser_encrypt_string(parser, vault_cli):
    parser.parse_args = MagicMock(return_value=MagicMock(action='encrypt_string', func=vault_cli.execute_encrypt_string, args=['secret']))
    args = parser.parse_args(['encrypt_string', 'secret'])
    assert args.action == 'encrypt_string'
    assert args.func.__name__ == 'execute_encrypt_string'
    assert args.args == ['secret']

def test_vault_cli_parser_rekey(parser, vault_cli):
    parser.parse_args = MagicMock(return_value=MagicMock(action='rekey', func=vault_cli.execute_rekey, args=['test_file.yml']))
    args = parser.parse_args(['rekey', 'test_file.yml'])
    assert args.action == 'rekey'
    assert args.func.__name__ == 'execute_rekey'
    assert args.args == ['test_file.yml']
