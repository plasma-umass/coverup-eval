# file lib/ansible/cli/console.py:357-364
# lines [357, 359, 360, 361, 363, 364]
# branches ['359->360', '359->363']

import pytest
from unittest import mock
from ansible.cli.console import ConsoleCLI
from ansible.utils.display import Display

@pytest.fixture
def console_cli(mocker):
    mock_args = mocker.Mock()
    cli = ConsoleCLI(mock_args)
    cli.become_method = 'sudo'
    return cli

def test_do_become_method_with_arg(console_cli, mocker):
    mock_display_v = mocker.patch.object(Display, 'v')
    console_cli.do_become_method('su')
    assert console_cli.become_method == 'su'
    mock_display_v.assert_called_once_with("become_method changed to su")

def test_do_become_method_without_arg(console_cli, mocker):
    mock_display_display = mocker.patch.object(Display, 'display')
    mock_display_v = mocker.patch.object(Display, 'v')
    console_cli.do_become_method('')
    mock_display_display.assert_called_once_with("Please specify a become_method, e.g. `become_method su`")
    mock_display_v.assert_called_once_with("Current become_method is sudo")
