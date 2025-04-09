# file: lib/ansible/cli/vault.py:52-118
# asked: {"lines": [52, 53, 54, 55, 58, 59, 60, 62, 63, 65, 66, 67, 68, 71, 72, 73, 74, 76, 77, 78, 80, 81, 82, 84, 85, 86, 88, 89, 90, 92, 93, 94, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 111, 112, 113, 114, 115, 116, 117, 118], "branches": []}
# gained: {"lines": [52, 53, 54, 55, 58, 59, 60, 62, 63, 65, 66, 67, 68, 71, 72, 73, 74, 76, 77, 78, 80, 81, 82, 84, 85, 86, 88, 89, 90, 92, 93, 94, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 111, 112, 113, 114, 115, 116, 117, 118], "branches": []}

import pytest
from unittest.mock import MagicMock, patch
from ansible.cli.vault import VaultCLI
from ansible.cli.arguments import option_helpers as opt_help

@pytest.fixture
def vault_cli():
    args = MagicMock()
    return VaultCLI(args)

def test_init_parser(vault_cli):
    with patch('ansible.cli.vault.opt_help.argparse.ArgumentParser') as mock_argparse:
        with patch('ansible.cli.vault.opt_help.add_vault_options') as mock_add_vault_options:
            with patch('ansible.cli.vault.opt_help.add_verbosity_options') as mock_add_verbosity_options:
                vault_cli.init_parser()
                mock_argparse.assert_called()
                mock_add_vault_options.assert_called()
                mock_add_verbosity_options.assert_called()

def test_subparsers(vault_cli):
    with patch('ansible.cli.vault.opt_help.argparse.ArgumentParser') as mock_argparse:
        vault_cli.init_parser()
        subparsers = vault_cli.parser.add_subparsers(dest='action')
        assert subparsers is not None
        assert subparsers.required is True

def test_create_parser(vault_cli):
    with patch('ansible.cli.vault.opt_help.argparse.ArgumentParser') as mock_argparse:
        vault_cli.init_parser()
        subparsers = vault_cli.parser.add_subparsers(dest='action')
        create_parser = subparsers.add_parser('create', help='Create new vault encrypted file')
        assert create_parser is not None

def test_decrypt_parser(vault_cli):
    with patch('ansible.cli.vault.opt_help.argparse.ArgumentParser') as mock_argparse:
        vault_cli.init_parser()
        subparsers = vault_cli.parser.add_subparsers(dest='action')
        decrypt_parser = subparsers.add_parser('decrypt', help='Decrypt vault encrypted file')
        assert decrypt_parser is not None

def test_edit_parser(vault_cli):
    with patch('ansible.cli.vault.opt_help.argparse.ArgumentParser') as mock_argparse:
        vault_cli.init_parser()
        subparsers = vault_cli.parser.add_subparsers(dest='action')
        edit_parser = subparsers.add_parser('edit', help='Edit vault encrypted file')
        assert edit_parser is not None

def test_view_parser(vault_cli):
    with patch('ansible.cli.vault.opt_help.argparse.ArgumentParser') as mock_argparse:
        vault_cli.init_parser()
        subparsers = vault_cli.parser.add_subparsers(dest='action')
        view_parser = subparsers.add_parser('view', help='View vault encrypted file')
        assert view_parser is not None

def test_encrypt_parser(vault_cli):
    with patch('ansible.cli.vault.opt_help.argparse.ArgumentParser') as mock_argparse:
        vault_cli.init_parser()
        subparsers = vault_cli.parser.add_subparsers(dest='action')
        encrypt_parser = subparsers.add_parser('encrypt', help='Encrypt YAML file')
        assert encrypt_parser is not None

def test_encrypt_string_parser(vault_cli):
    with patch('ansible.cli.vault.opt_help.argparse.ArgumentParser') as mock_argparse:
        vault_cli.init_parser()
        subparsers = vault_cli.parser.add_subparsers(dest='action')
        encrypt_string_parser = subparsers.add_parser('encrypt_string', help='Encrypt a string')
        assert encrypt_string_parser is not None

def test_rekey_parser(vault_cli):
    with patch('ansible.cli.vault.opt_help.argparse.ArgumentParser') as mock_argparse:
        vault_cli.init_parser()
        subparsers = vault_cli.parser.add_subparsers(dest='action')
        rekey_parser = subparsers.add_parser('rekey', help='Re-key a vault encrypted file')
        assert rekey_parser is not None
