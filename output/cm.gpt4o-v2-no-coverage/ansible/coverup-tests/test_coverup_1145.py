# file: lib/ansible/cli/vault.py:281-381
# asked: {"lines": [309, 322, 329, 377, 381], "branches": [[306, 309], [321, 322], [328, 329], [343, 352], [376, 377], [380, 381]]}
# gained: {"lines": [322, 329, 381], "branches": [[321, 322], [328, 329], [380, 381]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.errors import AnsibleOptionsError
from ansible.module_utils._text import to_bytes
from ansible import context
from ansible.cli.vault import VaultCLI

@pytest.fixture
def vault_cli():
    return VaultCLI(['test'])

def test_execute_encrypt_string_prompt(monkeypatch, vault_cli):
    context.CLIARGS = {
        'args': [],
        'encrypt_string_prompt': True,
        'show_string_input': False
    }

    def mock_prompt(msg, private=False):
        if 'Variable name' in msg:
            return 'test_var'
        return 'test_string'

    monkeypatch.setattr('ansible.cli.vault.display.prompt', mock_prompt)
    monkeypatch.setattr('ansible.cli.vault.display.display', MagicMock())
    monkeypatch.setattr('ansible.cli.vault.VaultCLI._format_output_vault_strings', lambda self, b_plaintext_list, vault_id=None: [{'out': 'encrypted_string'}])

    with patch('sys.stdout.isatty', return_value=True):
        vault_cli.execute_encrypt_string()

    assert context.CLIARGS['encrypt_string_prompt'] == True

def test_execute_encrypt_string_stdin(monkeypatch, vault_cli):
    context.CLIARGS = {
        'args': [],
        'encrypt_string_prompt': False,
        'show_string_input': False,
        'encrypt_string_stdin_name': 'stdin_var'
    }

    vault_cli.encrypt_string_read_stdin = True

    monkeypatch.setattr('sys.stdin.read', lambda: 'stdin_string')
    monkeypatch.setattr('ansible.cli.vault.display.display', MagicMock())
    monkeypatch.setattr('ansible.cli.vault.VaultCLI._format_output_vault_strings', lambda self, b_plaintext_list, vault_id=None: [{'out': 'encrypted_string'}])

    with patch('sys.stdout.isatty', return_value=True):
        vault_cli.execute_encrypt_string()

    assert vault_cli.encrypt_string_read_stdin == True

def test_execute_encrypt_string_args(monkeypatch, vault_cli):
    context.CLIARGS = {
        'args': ['arg1', 'arg2'],
        'encrypt_string_prompt': False,
        'show_string_input': False,
        'encrypt_string_names': ['name1']
    }

    monkeypatch.setattr('ansible.cli.vault.display.display', MagicMock())
    monkeypatch.setattr('ansible.cli.vault.VaultCLI._format_output_vault_strings', lambda self, b_plaintext_list, vault_id=None: [{'out': 'encrypted_string'}])

    with patch('sys.stdout.isatty', return_value=True):
        vault_cli.execute_encrypt_string()

    assert context.CLIARGS['args'] == ['arg1', 'arg2']

def test_execute_encrypt_string_empty_prompt(monkeypatch, vault_cli):
    context.CLIARGS = {
        'args': [],
        'encrypt_string_prompt': True,
        'show_string_input': False
    }

    def mock_prompt(msg, private=False):
        return ''

    monkeypatch.setattr('ansible.cli.vault.display.prompt', mock_prompt)

    with pytest.raises(AnsibleOptionsError, match='The plaintext provided from the prompt was empty, not encrypting'):
        vault_cli.execute_encrypt_string()

def test_execute_encrypt_string_empty_stdin(monkeypatch, vault_cli):
    context.CLIARGS = {
        'args': [],
        'encrypt_string_prompt': False,
        'show_string_input': False
    }

    vault_cli.encrypt_string_read_stdin = True

    monkeypatch.setattr('sys.stdin.read', lambda: '')

    with pytest.raises(AnsibleOptionsError, match='stdin was empty, not encrypting'):
        vault_cli.execute_encrypt_string()

def test_execute_encrypt_string_empty_args(monkeypatch, vault_cli):
    context.CLIARGS = {
        'args': [''],
        'encrypt_string_prompt': False,
        'show_string_input': False
    }

    with pytest.raises(AnsibleOptionsError, match='The plaintext provided from the command line args was empty, not encrypting'):
        vault_cli.execute_encrypt_string()
