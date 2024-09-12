# file: lib/ansible/cli/vault.py:281-381
# asked: {"lines": [294, 296, 297, 300, 301, 305, 306, 307, 309, 311, 313, 314, 316, 317, 321, 322, 324, 325, 326, 328, 329, 331, 334, 335, 345, 346, 347, 348, 349, 353, 357, 364, 377, 381], "branches": [[293, 294], [300, 301], [300, 305], [306, 307], [306, 309], [313, 314], [313, 316], [320, 321], [321, 322], [321, 324], [325, 326], [325, 328], [328, 329], [328, 331], [339, 357], [343, 345], [352, 353], [363, 364], [376, 377], [380, 381]]}
# gained: {"lines": [294, 296, 297, 300, 301, 305, 306, 307, 311, 313, 314, 316, 317, 321, 322, 324, 325, 326, 328, 329, 331, 334, 335, 345, 346, 347, 348, 349, 353, 357, 364, 381], "branches": [[293, 294], [300, 301], [306, 307], [313, 314], [313, 316], [320, 321], [321, 322], [325, 326], [325, 328], [328, 329], [339, 357], [343, 345], [352, 353], [363, 364], [380, 381]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.errors import AnsibleOptionsError
from ansible.module_utils._text import to_bytes
from ansible import context
from ansible.cli.vault import VaultCLI

@pytest.fixture
def vault_cli():
    return VaultCLI(['test'])

@pytest.fixture(autouse=True)
def setup_context():
    context.CLIARGS = {
        'args': [],
        'encrypt_string_prompt': False,
        'show_string_input': False,
        'encrypt_string_stdin_name': None,
        'encrypt_string_names': []
    }

def test_encrypt_string_prompt(vault_cli, monkeypatch):
    context.CLIARGS.update({
        'encrypt_string_prompt': True,
        'show_string_input': False
    })
    monkeypatch.setattr('builtins.input', lambda _: 'test_var')
    monkeypatch.setattr('ansible.cli.vault.display.prompt', lambda msg, private=False: 'test_string' if 'String to encrypt' in msg else 'test_var')
    
    with patch.object(vault_cli, '_format_output_vault_strings', return_value=[{'out': 'encrypted_string'}]) as mock_format:
        vault_cli.execute_encrypt_string()
        assert mock_format.call_count == 1

def test_encrypt_string_prompt_empty(vault_cli, monkeypatch):
    context.CLIARGS.update({
        'encrypt_string_prompt': True,
        'show_string_input': False
    })
    monkeypatch.setattr('builtins.input', lambda _: 'test_var')
    monkeypatch.setattr('ansible.cli.vault.display.prompt', lambda msg, private=False: '' if 'String to encrypt' in msg else 'test_var')
    
    with pytest.raises(AnsibleOptionsError, match='The plaintext provided from the prompt was empty, not encrypting'):
        vault_cli.execute_encrypt_string()

def test_encrypt_string_stdin(vault_cli, monkeypatch):
    vault_cli.encrypt_string_read_stdin = True
    context.CLIARGS.update({
        'encrypt_string_stdin_name': 'stdin_var'
    })
    monkeypatch.setattr('sys.stdin.read', lambda: 'stdin_string')
    monkeypatch.setattr('sys.stdout.isatty', lambda: True)
    monkeypatch.setattr('ansible.cli.vault.display.display', lambda msg, stderr=False: None)
    
    with patch.object(vault_cli, '_format_output_vault_strings', return_value=[{'out': 'encrypted_string'}]) as mock_format:
        vault_cli.execute_encrypt_string()
        assert mock_format.call_count == 1

def test_encrypt_string_stdin_empty(vault_cli, monkeypatch):
    vault_cli.encrypt_string_read_stdin = True
    context.CLIARGS.update({
        'encrypt_string_stdin_name': 'stdin_var'
    })
    monkeypatch.setattr('sys.stdin.read', lambda: '')
    monkeypatch.setattr('sys.stdout.isatty', lambda: True)
    monkeypatch.setattr('ansible.cli.vault.display.display', lambda msg, stderr=False: None)
    
    with pytest.raises(AnsibleOptionsError, match='stdin was empty, not encrypting'):
        vault_cli.execute_encrypt_string()

def test_encrypt_string_args(vault_cli, monkeypatch):
    context.CLIARGS.update({
        'args': ['arg1', 'arg2'],
        'encrypt_string_names': ['name1']
    })
    monkeypatch.setattr('ansible.cli.vault.display.display', lambda msg, stderr=False: None)
    
    with patch.object(vault_cli, '_format_output_vault_strings', return_value=[{'out': 'encrypted_string'}]) as mock_format:
        vault_cli.execute_encrypt_string()
        assert mock_format.call_count == 1

def test_encrypt_string_args_empty(vault_cli, monkeypatch):
    context.CLIARGS.update({
        'args': [''],
        'encrypt_string_names': ['name1']
    })
    monkeypatch.setattr('ansible.cli.vault.display.display', lambda msg, stderr=False: None)
    
    with pytest.raises(AnsibleOptionsError, match='The plaintext provided from the command line args was empty, not encrypting'):
        vault_cli.execute_encrypt_string()

def test_encrypt_string_args_mismatch(vault_cli, monkeypatch):
    context.CLIARGS.update({
        'args': ['arg1', 'arg2'],
        'encrypt_string_names': ['name1']
    })
    display_mock = MagicMock()
    monkeypatch.setattr('ansible.cli.vault.display.display', display_mock)
    
    with patch.object(vault_cli, '_format_output_vault_strings', return_value=[{'out': 'encrypted_string'}]) as mock_format:
        vault_cli.execute_encrypt_string()
        display_mock.assert_any_call('The number of --name options do not match the number of args.', stderr=True)
        display_mock.assert_any_call('The last named variable will be "name1". The rest will not have names.', stderr=True)
        assert mock_format.call_count == 1
