# file: lib/ansible/cli/arguments/option_helpers.py:381-389
# asked: {"lines": [383, 384, 385, 386, 387, 388, 389], "branches": []}
# gained: {"lines": [383, 384, 385, 386, 387, 388, 389], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.cli.arguments.option_helpers import add_vault_options
from ansible import constants as C

@pytest.fixture
def parser():
    return MagicMock()

def test_add_vault_options_vault_id(parser):
    add_vault_options(parser)
    parser.add_argument.assert_any_call('--vault-id', default=[], dest='vault_ids', action='append', type=str, help='the vault identity to use')

def test_add_vault_options_ask_vault_password(parser):
    add_vault_options(parser)
    parser.add_mutually_exclusive_group.return_value.add_argument.assert_any_call('--ask-vault-password', '--ask-vault-pass', default=C.DEFAULT_ASK_VAULT_PASS, dest='ask_vault_pass', action='store_true', help='ask for vault password')

def test_add_vault_options_vault_password_file(parser, monkeypatch):
    mock_unfrack_path = MagicMock()
    monkeypatch.setattr('ansible.cli.arguments.option_helpers.unfrack_path', lambda: mock_unfrack_path)
    add_vault_options(parser)
    parser.add_mutually_exclusive_group.return_value.add_argument.assert_any_call('--vault-password-file', '--vault-pass-file', default=[], dest='vault_password_files', help='vault password file', type=mock_unfrack_path, action='append')
