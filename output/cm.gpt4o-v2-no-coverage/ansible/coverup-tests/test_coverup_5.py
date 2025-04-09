# file: lib/ansible/cli/vault.py:281-381
# asked: {"lines": [281, 283, 286, 290, 293, 294, 296, 297, 300, 301, 305, 306, 307, 309, 311, 313, 314, 316, 317, 320, 321, 322, 324, 325, 326, 328, 329, 331, 334, 335, 339, 340, 343, 345, 346, 347, 348, 349, 352, 353, 357, 360, 361, 363, 364, 366, 367, 371, 373, 374, 375, 376, 377, 378, 380, 381], "branches": [[293, 294], [293, 320], [300, 301], [300, 305], [306, 307], [306, 309], [313, 314], [313, 316], [320, 321], [320, 339], [321, 322], [321, 324], [325, 326], [325, 328], [328, 329], [328, 331], [339, 340], [339, 357], [343, 345], [343, 352], [352, 353], [352, 360], [360, 361], [360, 371], [363, 364], [363, 366], [373, 374], [373, 380], [376, 377], [376, 378], [380, 0], [380, 381]]}
# gained: {"lines": [281, 283, 286, 290, 293, 294, 296, 297, 300, 301, 305, 306, 307, 311, 313, 314, 316, 317, 320, 321, 324, 325, 326, 328, 331, 334, 335, 339, 340, 343, 345, 346, 347, 348, 349, 352, 353, 357, 360, 361, 363, 364, 366, 367, 371, 373, 374, 375, 376, 378, 380], "branches": [[293, 294], [293, 320], [300, 301], [300, 305], [306, 307], [313, 314], [313, 316], [320, 321], [320, 339], [321, 324], [325, 326], [325, 328], [328, 331], [339, 340], [339, 357], [343, 345], [352, 353], [352, 360], [360, 361], [360, 371], [363, 364], [363, 366], [373, 374], [373, 380], [376, 378], [380, 0]]}

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
    monkeypatch.setattr('ansible.cli.vault.VaultCLI._format_output_vault_strings', MagicMock(return_value=[{'out': 'encrypted_string'}]))

    vault_cli.execute_encrypt_string()

    assert vault_cli._format_output_vault_strings.called
    assert vault_cli._format_output_vault_strings.call_args[0][0][0][0] == to_bytes('test_string')
    assert vault_cli._format_output_vault_strings.call_args[0][0][0][2] == 'test_var'

def test_execute_encrypt_string_stdin(monkeypatch, vault_cli):
    context.CLIARGS = {
        'args': [],
        'encrypt_string_prompt': False,
        'show_string_input': False,
        'encrypt_string_stdin_name': 'stdin_var'
    }

    vault_cli.encrypt_string_read_stdin = True

    monkeypatch.setattr('sys.stdin.read', lambda: 'stdin_string')
    monkeypatch.setattr('sys.stdout.isatty', lambda: False)
    monkeypatch.setattr('ansible.cli.vault.display.display', MagicMock())
    monkeypatch.setattr('ansible.cli.vault.VaultCLI._format_output_vault_strings', MagicMock(return_value=[{'out': 'encrypted_string'}]))

    vault_cli.execute_encrypt_string()

    assert vault_cli._format_output_vault_strings.called
    assert vault_cli._format_output_vault_strings.call_args[0][0][0][0] == to_bytes('stdin_string')
    assert vault_cli._format_output_vault_strings.call_args[0][0][0][2] == 'stdin_var'

def test_execute_encrypt_string_args(monkeypatch, vault_cli):
    context.CLIARGS = {
        'args': ['arg1', 'arg2'],
        'encrypt_string_prompt': False,
        'show_string_input': False,
        'encrypt_string_names': ['name1']
    }

    monkeypatch.setattr('ansible.cli.vault.display.display', MagicMock())
    monkeypatch.setattr('ansible.cli.vault.VaultCLI._format_output_vault_strings', MagicMock(return_value=[{'out': 'encrypted_string'}]))

    vault_cli.execute_encrypt_string()

    assert vault_cli._format_output_vault_strings.called
    assert vault_cli._format_output_vault_strings.call_args[0][0][0][0] == to_bytes('arg1')
    assert vault_cli._format_output_vault_strings.call_args[0][0][0][2] == 'name1'
    assert vault_cli._format_output_vault_strings.call_args[0][0][1][0] == to_bytes('arg2')
    assert vault_cli._format_output_vault_strings.call_args[0][0][1][2] is None

def test_execute_encrypt_string_empty_prompt(monkeypatch, vault_cli):
    context.CLIARGS = {
        'args': [],
        'encrypt_string_prompt': True,
        'show_string_input': False
    }

    def mock_prompt(msg, private=False):
        return ''

    monkeypatch.setattr('ansible.cli.vault.display.prompt', mock_prompt)
    monkeypatch.setattr('ansible.cli.vault.display.display', MagicMock())

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
    monkeypatch.setattr('sys.stdout.isatty', lambda: False)
    monkeypatch.setattr('ansible.cli.vault.display.display', MagicMock())

    with pytest.raises(AnsibleOptionsError, match='stdin was empty, not encrypting'):
        vault_cli.execute_encrypt_string()

def test_execute_encrypt_string_empty_args(monkeypatch, vault_cli):
    context.CLIARGS = {
        'args': [''],
        'encrypt_string_prompt': False,
        'show_string_input': False
    }

    monkeypatch.setattr('ansible.cli.vault.display.display', MagicMock())

    with pytest.raises(AnsibleOptionsError, match='The plaintext provided from the command line args was empty, not encrypting'):
        vault_cli.execute_encrypt_string()
