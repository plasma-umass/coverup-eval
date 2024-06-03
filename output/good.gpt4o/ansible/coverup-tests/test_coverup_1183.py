# file lib/ansible/cli/arguments/option_helpers.py:381-389
# lines [383, 384, 385, 386, 387, 388, 389]
# branches []

import pytest
from argparse import ArgumentParser
from unittest.mock import patch
from ansible.cli.arguments.option_helpers import add_vault_options

def test_add_vault_options(mocker):
    parser = ArgumentParser()
    mock_unfrack_path = mocker.patch('ansible.cli.arguments.option_helpers.unfrack_path', return_value=str)

    add_vault_options(parser)
    args = parser.parse_args([
        '--vault-id', 'test_vault_id',
        '--vault-password-file', 'test_vault_password_file'
    ])

    assert 'test_vault_id' in args.vault_ids
    assert args.ask_vault_pass is False
    assert 'test_vault_password_file' in args.vault_password_files

    mock_unfrack_path.assert_called_once()

@pytest.fixture(autouse=True)
def cleanup():
    yield
    # Add any necessary cleanup code here
