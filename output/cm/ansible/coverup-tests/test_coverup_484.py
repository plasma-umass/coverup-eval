# file lib/ansible/cli/arguments/option_helpers.py:381-389
# lines [381, 383, 384, 385, 386, 387, 388, 389]
# branches []

import pytest
from ansible.cli.arguments.option_helpers import add_vault_options
from argparse import ArgumentParser
from unittest.mock import MagicMock

# Mock the unfrack_path function as it is not provided in the snippet
def mock_unfrack_path():
    return str

@pytest.fixture
def parser():
    return ArgumentParser()

@pytest.fixture
def mock_unfrack_path_fixture(mocker):
    mocker.patch('ansible.cli.arguments.option_helpers.unfrack_path', new=mock_unfrack_path)

def test_add_vault_options(parser, mock_unfrack_path_fixture):
    add_vault_options(parser)
    args = parser.parse_args(['--vault-id', 'my_vault_id', '--ask-vault-pass'])
    assert args.vault_ids == ['my_vault_id']
    assert args.ask_vault_pass is True
    assert args.vault_password_files == []

    args = parser.parse_args(['--vault-id', 'my_vault_id', '--vault-password-file', 'vault_pass.txt'])
    assert args.vault_ids == ['my_vault_id']
    assert args.ask_vault_pass is False
    assert args.vault_password_files == ['vault_pass.txt']

    # Test the mutually exclusive group
    with pytest.raises(SystemExit):
        parser.parse_args(['--ask-vault-pass', '--vault-password-file', 'vault_pass.txt'])
