# file lib/ansible/cli/vault.py:281-381
# lines [283, 286, 290, 293, 294, 296, 297, 300, 301, 305, 306, 307, 309, 311, 313, 314, 316, 317, 320, 321, 322, 324, 325, 326, 328, 329, 331, 334, 335, 339, 340, 343, 345, 346, 347, 348, 349, 352, 353, 357, 360, 361, 363, 364, 366, 367, 371, 373, 374, 375, 376, 377, 378, 380, 381]
# branches ['293->294', '293->320', '300->301', '300->305', '306->307', '306->309', '313->314', '313->316', '320->321', '320->339', '321->322', '321->324', '325->326', '325->328', '328->329', '328->331', '339->340', '339->357', '343->345', '343->352', '352->353', '352->360', '360->361', '360->371', '363->364', '363->366', '373->374', '373->380', '376->377', '376->378', '380->exit', '380->381']

import pytest
from unittest.mock import patch, MagicMock
from ansible.cli.vault import VaultCLI
from ansible.errors import AnsibleOptionsError
from ansible.utils.display import Display
from ansible.module_utils._text import to_bytes

@pytest.fixture
def mock_context(mocker):
    context = mocker.patch('ansible.cli.vault.context')
    context.CLIARGS = {
        'args': ['test_string'],
        'encrypt_string_prompt': False,
        'show_string_input': False,
        'encrypt_string_stdin_name': None,
        'encrypt_string_names': [],
    }
    return context

@pytest.fixture
def mock_display(mocker):
    display = mocker.patch('ansible.cli.vault.display', autospec=True)
    display.prompt = MagicMock(side_effect=['test_var', 'test_string'])
    return display

@pytest.fixture
def mock_sys(mocker):
    sys = mocker.patch('ansible.cli.vault.sys', autospec=True)
    sys.stdout.isatty.return_value = True
    sys.stdin.read.return_value = 'test_stdin_string'
    return sys

@pytest.fixture
def mock_editor(mocker):
    editor = mocker.patch('ansible.cli.vault.VaultEditor', autospec=True)
    editor.encrypt_bytes.return_value = b'encrypted_string'
    return editor

@pytest.fixture
def vault_cli(mock_context, mock_editor):
    cli = VaultCLI(['ansible-vault'])
    cli.editor = mock_editor
    cli.encrypt_secret = b'secret'
    cli.encrypt_vault_id = None
    return cli

def test_execute_encrypt_string_prompt(mock_context, mock_display, vault_cli):
    mock_context.CLIARGS['encrypt_string_prompt'] = True
    vault_cli.execute_encrypt_string()
    mock_display.prompt.assert_any_call('Variable name (enter for no name): ')
    mock_display.prompt.assert_any_call('String to encrypt (hidden): ', private=True)

def test_execute_encrypt_string_stdin(mock_context, mock_sys, vault_cli):
    vault_cli.encrypt_string_read_stdin = True
    vault_cli.execute_encrypt_string()
    mock_sys.stdin.read.assert_called_once()
    assert mock_sys.stdin.read() == 'test_stdin_string'

def test_execute_encrypt_string_args(mock_context, vault_cli):
    mock_context.CLIARGS['encrypt_string_names'] = ['var1']
    mock_context.CLIARGS['args'] = ['test_string1', 'test_string2']
    vault_cli.execute_encrypt_string()
    assert len(mock_context.CLIARGS['args']) == 2

def test_execute_encrypt_string_empty_prompt(mock_context, mock_display, vault_cli):
    mock_context.CLIARGS['encrypt_string_prompt'] = True
    mock_display.prompt.side_effect = ['', '']
    with pytest.raises(AnsibleOptionsError, match='The plaintext provided from the prompt was empty, not encrypting'):
        vault_cli.execute_encrypt_string()

def test_execute_encrypt_string_empty_stdin(mock_context, mock_sys, vault_cli):
    vault_cli.encrypt_string_read_stdin = True
    mock_sys.stdin.read.return_value = ''
    with pytest.raises(AnsibleOptionsError, match='stdin was empty, not encrypting'):
        vault_cli.execute_encrypt_string()

def test_execute_encrypt_string_empty_args(mock_context, vault_cli):
    mock_context.CLIARGS['args'] = ['']
    with pytest.raises(AnsibleOptionsError, match='The plaintext provided from the command line args was empty, not encrypting'):
        vault_cli.execute_encrypt_string()
