# file lib/ansible/cli/console.py:291-300
# lines [291, 293, 294, 296, 297, 298, 299, 300]
# branches ['293->294', '293->296']

import pytest
from unittest import mock
from ansible.cli.console import ConsoleCLI
from ansible.utils.display import Display

@pytest.fixture
def mock_display(mocker):
    display = mocker.patch('ansible.cli.console.display', autospec=True)
    return display

@pytest.fixture
def console_cli(mocker):
    mocker.patch('ansible.cli.console.CLI.__init__', return_value=None)
    return ConsoleCLI(args=[])

def test_do_verbosity_no_arg(console_cli, mock_display):
    console_cli.do_verbosity('')
    mock_display.display.assert_called_once_with('Usage: verbosity <number>')

def test_do_verbosity_valid_arg(console_cli, mock_display):
    console_cli.do_verbosity('3')
    mock_display.verbosity = 3
    mock_display.v.assert_called_once_with('verbosity level set to 3')

def test_do_verbosity_invalid_arg(console_cli, mock_display):
    console_cli.do_verbosity('invalid')
    mock_display.error.assert_called_once()
    assert 'The verbosity must be a valid integer' in mock_display.error.call_args[0][0]
