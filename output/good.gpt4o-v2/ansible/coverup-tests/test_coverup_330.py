# file: lib/ansible/cli/arguments/option_helpers.py:340-358
# asked: {"lines": [340, 347, 348, 350, 352, 353, 354, 355, 356, 358], "branches": [[347, 348], [347, 350]]}
# gained: {"lines": [340, 347, 348, 350, 352, 353, 354, 355, 356, 358], "branches": [[347, 348], [347, 350]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.cli.arguments.option_helpers import add_runas_prompt_options

@pytest.fixture
def mock_parser():
    return MagicMock()

def test_add_runas_prompt_options_with_runas_group(mock_parser):
    runas_group = "runas_group"
    add_runas_prompt_options(mock_parser, runas_group)
    mock_parser.add_argument_group.assert_any_call(runas_group)

def test_add_runas_prompt_options_without_runas_group(mock_parser):
    add_runas_prompt_options(mock_parser)
    mock_parser.add_argument_group.assert_called()

@patch('ansible.cli.arguments.option_helpers.C.DEFAULT_BECOME_ASK_PASS', True)
@patch('ansible.cli.arguments.option_helpers.C.BECOME_PASSWORD_FILE', '/path/to/password/file')
@patch('ansible.cli.arguments.option_helpers.unfrack_path', lambda: str)
def test_add_runas_prompt_options_arguments(mock_parser):
    add_runas_prompt_options(mock_parser)
    mock_parser.add_mutually_exclusive_group().add_argument.assert_any_call(
        '-K', '--ask-become-pass', dest='become_ask_pass', action='store_true',
        default=True, help='ask for privilege escalation password'
    )
    mock_parser.add_mutually_exclusive_group().add_argument.assert_any_call(
        '--become-password-file', '--become-pass-file', default='/path/to/password/file',
        dest='become_password_file', help='Become password file', type=str, action='store'
    )
