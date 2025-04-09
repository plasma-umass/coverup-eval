# file lib/ansible/cli/vault.py:52-118
# lines [53, 54, 55, 58, 59, 60, 62, 63, 65, 66, 67, 68, 71, 72, 73, 74, 76, 77, 78, 80, 81, 82, 84, 85, 86, 88, 89, 90, 92, 93, 94, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 111, 112, 113, 114, 115, 116, 117, 118]
# branches []

import pytest
import argparse
from unittest import mock
from ansible.cli.vault import VaultCLI

@pytest.fixture
def vault_cli():
    return VaultCLI(['ansible-vault'])

def test_vault_cli_init_parser(vault_cli, mocker):
    mocker.patch('ansible.cli.vault.opt_help.add_vault_options')
    mocker.patch('ansible.cli.vault.opt_help.add_verbosity_options')
    mocker.patch('ansible.cli.vault.opt_help.unfrack_path', return_value=str)
    
    vault_cli.init_parser()
    
    assert vault_cli.parser is not None
    assert vault_cli.parser._subparsers is not None
    subparsers_actions = [action for action in vault_cli.parser._actions if isinstance(action, argparse._SubParsersAction)]
    assert len(subparsers_actions) == 1
    subparsers = subparsers_actions[0]
    assert 'create' in subparsers.choices
    assert 'decrypt' in subparsers.choices
    assert 'edit' in subparsers.choices
    assert 'view' in subparsers.choices
    assert 'encrypt' in subparsers.choices
    assert 'encrypt_string' in subparsers.choices
    assert 'rekey' in subparsers.choices

    # Check if the subparsers have the correct defaults
    assert subparsers.choices['create'].get_default('func') == vault_cli.execute_create
    assert subparsers.choices['decrypt'].get_default('func') == vault_cli.execute_decrypt
    assert subparsers.choices['edit'].get_default('func') == vault_cli.execute_edit
    assert subparsers.choices['view'].get_default('func') == vault_cli.execute_view
    assert subparsers.choices['encrypt'].get_default('func') == vault_cli.execute_encrypt
    assert subparsers.choices['encrypt_string'].get_default('func') == vault_cli.execute_encrypt_string
    assert subparsers.choices['rekey'].get_default('func') == vault_cli.execute_rekey
