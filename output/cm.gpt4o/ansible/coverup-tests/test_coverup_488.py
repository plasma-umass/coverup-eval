# file lib/ansible/cli/console.py:375-382
# lines [375, 377, 378, 379, 381, 382]
# branches ['377->378', '377->381']

import pytest
from unittest import mock
from ansible.cli.console import ConsoleCLI
from ansible.utils.display import Display

@pytest.fixture
def console_cli():
    args = mock.MagicMock()
    cli = ConsoleCLI(args)
    cli.diff = False
    return cli

def test_do_diff_with_arg(console_cli, mocker):
    mock_display = mocker.patch.object(Display, 'display')
    console_cli.do_diff('yes')
    assert console_cli.diff is True
    mock_display.assert_called_with("diff mode changed to True")

def test_do_diff_without_arg(console_cli, mocker):
    mock_display = mocker.patch.object(Display, 'display')
    mock_v = mocker.patch.object(Display, 'v')
    console_cli.do_diff('')
    mock_display.assert_called_with("Please specify a diff value , e.g. `diff yes`")
    mock_v.assert_called_with("diff mode is currently False")
