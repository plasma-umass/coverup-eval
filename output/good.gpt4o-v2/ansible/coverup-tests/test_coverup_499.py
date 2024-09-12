# file: lib/ansible/cli/console.py:375-382
# asked: {"lines": [375, 377, 378, 379, 381, 382], "branches": [[377, 378], [377, 381]]}
# gained: {"lines": [375, 377, 378, 379, 381, 382], "branches": [[377, 378], [377, 381]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.cli.console import ConsoleCLI
from ansible.module_utils.parsing.convert_bool import boolean

@pytest.fixture
def console_cli():
    args = MagicMock()
    cli = ConsoleCLI(args)
    cli.diff = False
    return cli

def test_do_diff_with_arg_true(console_cli, mocker):
    mock_display = mocker.patch('ansible.cli.console.display.display')
    console_cli.do_diff('yes')
    assert console_cli.diff is True
    mock_display.assert_called_once_with('diff mode changed to True')

def test_do_diff_with_arg_false(console_cli, mocker):
    mock_display = mocker.patch('ansible.cli.console.display.display')
    console_cli.do_diff('no')
    assert console_cli.diff is False
    mock_display.assert_called_once_with('diff mode changed to False')

def test_do_diff_without_arg(console_cli, mocker):
    mock_display = mocker.patch('ansible.cli.console.display.display')
    mock_v = mocker.patch('ansible.cli.console.display.v')
    console_cli.do_diff('')
    mock_display.assert_called_once_with('Please specify a diff value , e.g. `diff yes`')
    mock_v.assert_called_once_with('diff mode is currently False')
