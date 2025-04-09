# file lib/ansible/cli/console.py:366-373
# lines [366, 368, 369, 370, 372, 373]
# branches ['368->369', '368->372']

import pytest
from unittest import mock
from ansible.cli.console import ConsoleCLI
from ansible.utils.display import Display

@pytest.fixture
def console_cli():
    cli = ConsoleCLI(args=['dummy'])
    cli.check_mode = False
    return cli

def test_do_check_with_arg(console_cli, mocker):
    mock_display = mocker.patch.object(Display, 'display')
    mock_v = mocker.patch.object(Display, 'v')

    console_cli.do_check('yes')
    assert console_cli.check_mode is True
    mock_display.assert_called_once_with("check mode changed to True")
    mock_v.assert_not_called()

def test_do_check_without_arg(console_cli, mocker):
    mock_display = mocker.patch.object(Display, 'display')
    mock_v = mocker.patch.object(Display, 'v')

    console_cli.do_check('')
    mock_display.assert_called_once_with("Please specify check mode value, e.g. `check yes`")
    mock_v.assert_called_once_with("check mode is currently False.")
