# file: lib/ansible/cli/vault.py:120-141
# asked: {"lines": [], "branches": [[126, 130], [127, 126], [134, 138]]}
# gained: {"lines": [], "branches": [[127, 126]]}

import pytest
from ansible.errors import AnsibleOptionsError
from ansible.cli.vault import VaultCLI
from unittest.mock import MagicMock

class MockOptions:
    def __init__(self, verbosity=0, vault_ids=None, output_file=None, args=None, action=None, encrypt_string_stdin_name=None, encrypt_string_prompt=None):
        self.verbosity = verbosity
        self.vault_ids = vault_ids or []
        self.output_file = output_file
        self.args = args or []
        self.action = action
        self.encrypt_string_stdin_name = encrypt_string_stdin_name
        self.encrypt_string_prompt = encrypt_string_prompt

@pytest.fixture
def vault_cli(monkeypatch):
    cli = VaultCLI(['dummy_arg'])
    cli.parser = MagicMock()
    cli.parser.prog = 'ansible-vault'
    return cli

def test_post_process_args_sets_verbosity(vault_cli):
    options = MockOptions(verbosity=3)
    processed_options = vault_cli.post_process_args(options)
    assert processed_options.verbosity == 3

def test_post_process_args_invalid_vault_id(vault_cli):
    options = MockOptions(vault_ids=['valid_id', 'invalid;id'])
    with pytest.raises(AnsibleOptionsError, match="is not a valid vault id"):
        vault_cli.post_process_args(options)

def test_post_process_args_output_file_with_multiple_args(vault_cli):
    options = MockOptions(output_file='output.txt', args=['input1.txt', 'input2.txt'])
    with pytest.raises(AnsibleOptionsError, match="At most one input file may be used with the --output option"):
        vault_cli.post_process_args(options)

def test_post_process_args_encrypt_string_read_stdin(vault_cli):
    options = MockOptions(action='encrypt_string', args=['-'])
    processed_options = vault_cli.post_process_args(options)
    assert vault_cli.encrypt_string_read_stdin

def test_post_process_args_encrypt_string_prompt_and_stdin(vault_cli):
    options = MockOptions(action='encrypt_string', args=['-'], encrypt_string_prompt=True)
    with pytest.raises(AnsibleOptionsError, match="The --prompt option is not supported if also reading input from stdin"):
        vault_cli.post_process_args(options)
