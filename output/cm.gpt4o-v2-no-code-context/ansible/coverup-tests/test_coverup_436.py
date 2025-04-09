# file: lib/ansible/cli/console.py:357-364
# asked: {"lines": [357, 359, 360, 361, 363, 364], "branches": [[359, 360], [359, 363]]}
# gained: {"lines": [357, 359, 360, 361, 363, 364], "branches": [[359, 360], [359, 363]]}

import pytest
from ansible.cli.console import ConsoleCLI
from unittest.mock import patch, MagicMock

@pytest.fixture
def console_cli(mocker):
    mock_args = mocker.MagicMock()
    return ConsoleCLI(mock_args)

def test_do_become_method_with_arg(console_cli, mocker):
    mock_display_v = mocker.patch('ansible.cli.console.display.v')
    console_cli.become_method = None

    console_cli.do_become_method('sudo')

    assert console_cli.become_method == 'sudo'
    mock_display_v.assert_called_once_with("become_method changed to sudo")

def test_do_become_method_without_arg(console_cli, mocker):
    mock_display_display = mocker.patch('ansible.cli.console.display.display')
    mock_display_v = mocker.patch('ansible.cli.console.display.v')
    console_cli.become_method = 'sudo'

    console_cli.do_become_method('')

    mock_display_display.assert_called_once_with("Please specify a become_method, e.g. `become_method su`")
    mock_display_v.assert_called_once_with("Current become_method is sudo")
