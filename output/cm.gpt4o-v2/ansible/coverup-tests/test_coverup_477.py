# file: lib/ansible/cli/arguments/option_helpers.py:381-389
# asked: {"lines": [381, 383, 384, 385, 386, 387, 388, 389], "branches": []}
# gained: {"lines": [381, 383, 384, 385, 386, 387, 388, 389], "branches": []}

import pytest
from argparse import ArgumentParser
from ansible.cli.arguments.option_helpers import add_vault_options
from ansible.utils.path import unfrackpath

@pytest.fixture
def parser():
    return ArgumentParser()

def test_add_vault_options_vault_id(parser):
    add_vault_options(parser)
    args = parser.parse_args(['--vault-id', 'test_id'])
    assert args.vault_ids == ['test_id']

def test_add_vault_options_ask_vault_password(parser):
    add_vault_options(parser)
    args = parser.parse_args(['--ask-vault-password'])
    assert args.ask_vault_pass is True

def test_add_vault_options_vault_password_file(parser, monkeypatch):
    def mock_unfrack_path(value):
        return value

    monkeypatch.setattr('ansible.cli.arguments.option_helpers.unfrack_path', lambda: mock_unfrack_path)
    add_vault_options(parser)
    args = parser.parse_args(['--vault-password-file', 'test_file'])
    assert args.vault_password_files == ['test_file']
