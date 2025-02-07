# file: lib/ansible/cli/console.py:291-300
# asked: {"lines": [291, 293, 294, 296, 297, 298, 299, 300], "branches": [[293, 294], [293, 296]]}
# gained: {"lines": [291, 293, 294, 296, 297, 298, 299, 300], "branches": [[293, 294], [293, 296]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.cli.console import ConsoleCLI

@pytest.fixture
def console_cli():
    args = MagicMock()
    return ConsoleCLI(args)

def test_do_verbosity_no_arg(console_cli):
    with patch('ansible.cli.console.display') as mock_display:
        console_cli.do_verbosity('')
        mock_display.display.assert_called_once_with('Usage: verbosity <number>')

def test_do_verbosity_valid_arg(console_cli):
    with patch('ansible.cli.console.display') as mock_display:
        console_cli.do_verbosity('2')
        assert mock_display.verbosity == 2
        mock_display.v.assert_called_once_with('verbosity level set to 2')

def test_do_verbosity_invalid_arg(console_cli):
    with patch('ansible.cli.console.display') as mock_display:
        console_cli.do_verbosity('invalid')
        mock_display.error.assert_called_once()
        args, _ = mock_display.error.call_args
        assert 'The verbosity must be a valid integer' in args[0]
