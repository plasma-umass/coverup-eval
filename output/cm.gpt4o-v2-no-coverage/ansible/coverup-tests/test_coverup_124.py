# file: lib/ansible/cli/vault.py:120-141
# asked: {"lines": [120, 121, 123, 125, 126, 127, 128, 130, 131, 133, 134, 135, 138, 139, 141], "branches": [[125, 126], [125, 130], [126, 127], [126, 130], [127, 126], [127, 128], [130, 131], [130, 133], [133, 134], [133, 141], [134, 135], [134, 138], [138, 139], [138, 141]]}
# gained: {"lines": [120, 121, 123, 125, 126, 127, 128, 130, 131, 133, 134, 135, 138, 139, 141], "branches": [[125, 126], [125, 130], [126, 127], [127, 128], [130, 131], [130, 133], [133, 134], [133, 141], [134, 135], [138, 139], [138, 141]]}

import pytest
from ansible.errors import AnsibleOptionsError
from ansible.cli.vault import VaultCLI
from ansible.utils.display import Display

@pytest.fixture
def mock_display(mocker):
    return mocker.patch('ansible.cli.vault.display', autospec=True)

@pytest.fixture
def vault_cli(mocker):
    cli = VaultCLI(['test'])
    cli.parser = mocker.Mock()
    cli.parser.prog = 'ansible-vault'
    return cli

def test_post_process_args_verbosity(vault_cli, mock_display):
    options = type('obj', (object,), {'verbosity': 3, 'vault_ids': None, 'args': [], 'action': None})
    vault_cli.post_process_args(options)
    assert mock_display.verbosity == 3

def test_post_process_args_invalid_vault_id(vault_cli):
    options = type('obj', (object,), {'verbosity': 0, 'vault_ids': ['invalid;id'], 'args': [], 'action': None})
    with pytest.raises(AnsibleOptionsError, match="'invalid;id' is not a valid vault id. The character ';' is not allowed in vault ids"):
        vault_cli.post_process_args(options)

def test_post_process_args_output_file_with_multiple_args(vault_cli):
    options = type('obj', (object,), {'verbosity': 0, 'vault_ids': None, 'args': ['arg1', 'arg2'], 'output_file': 'output', 'action': None})
    with pytest.raises(AnsibleOptionsError, match="At most one input file may be used with the --output option"):
        vault_cli.post_process_args(options)

def test_post_process_args_encrypt_string_read_stdin(vault_cli):
    options = type('obj', (object,), {'verbosity': 0, 'vault_ids': None, 'args': ['-'], 'action': 'encrypt_string', 'encrypt_string_stdin_name': None, 'encrypt_string_prompt': None})
    result = vault_cli.post_process_args(options)
    assert vault_cli.encrypt_string_read_stdin is True

def test_post_process_args_encrypt_string_prompt_error(vault_cli):
    options = type('obj', (object,), {'verbosity': 0, 'vault_ids': None, 'args': ['-'], 'action': 'encrypt_string', 'encrypt_string_stdin_name': None, 'encrypt_string_prompt': True})
    with pytest.raises(AnsibleOptionsError, match='The --prompt option is not supported if also reading input from stdin'):
        vault_cli.post_process_args(options)
