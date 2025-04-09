# file: lib/ansible/cli/console.py:375-382
# asked: {"lines": [375, 377, 378, 379, 381, 382], "branches": [[377, 378], [377, 381]]}
# gained: {"lines": [375, 377, 378, 379, 381, 382], "branches": [[377, 378], [377, 381]]}

import pytest
from unittest import mock
from ansible.cli.console import ConsoleCLI
from ansible.utils.display import Display

@pytest.fixture
def console_cli(mocker):
    mocker.patch('ansible.cli.console.CLI.__init__', return_value=None)
    cli = ConsoleCLI(args=[])
    cli.diff = False
    return cli

def test_do_diff_with_argument(console_cli, mocker):
    mock_display = mocker.patch('ansible.utils.display.Display.display')
    mock_v = mocker.patch('ansible.utils.display.Display.v')
    
    console_cli.do_diff('yes')
    
    assert console_cli.diff is True
    mock_display.assert_called_once_with("diff mode changed to True")
    mock_v.assert_not_called()

def test_do_diff_without_argument(console_cli, mocker):
    mock_display = mocker.patch('ansible.utils.display.Display.display')
    mock_v = mocker.patch('ansible.utils.display.Display.v')
    
    console_cli.do_diff('')
    
    mock_display.assert_called_once_with("Please specify a diff value , e.g. `diff yes`")
    mock_v.assert_called_once_with("diff mode is currently False")
