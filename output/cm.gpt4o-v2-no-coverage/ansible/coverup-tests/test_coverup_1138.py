# file: lib/ansible/cli/console.py:94-113
# asked: {"lines": [95, 96, 97, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 111, 112, 113], "branches": []}
# gained: {"lines": [95, 96, 97, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 111, 112, 113], "branches": []}

import pytest
from unittest.mock import MagicMock, patch
from ansible.cli.console import ConsoleCLI

@pytest.fixture
def mock_parser(mocker):
    parser = MagicMock()
    mocker.patch('argparse.ArgumentParser', return_value=parser)
    return parser

@patch('ansible.cli.arguments.option_helpers.add_runas_options')
@patch('ansible.cli.arguments.option_helpers.add_inventory_options')
@patch('ansible.cli.arguments.option_helpers.add_connect_options')
@patch('ansible.cli.arguments.option_helpers.add_check_options')
@patch('ansible.cli.arguments.option_helpers.add_vault_options')
@patch('ansible.cli.arguments.option_helpers.add_fork_options')
@patch('ansible.cli.arguments.option_helpers.add_module_options')
@patch('ansible.cli.arguments.option_helpers.add_basedir_options')
@patch('ansible.cli.arguments.option_helpers.add_runtask_options')
@patch('ansible.cli.arguments.option_helpers.add_tasknoplay_options')
def test_init_parser(mock_tasknoplay, mock_runtask, mock_basedir, mock_module, mock_fork, mock_vault, mock_check, mock_connect, mock_inventory, mock_runas, mock_parser):
    cli = ConsoleCLI(args=['test'])
    cli.parser = mock_parser

    cli.init_parser()

    mock_parser.add_argument.assert_any_call('pattern', help='host pattern', metavar='pattern', default='all', nargs='?')
    mock_parser.add_argument.assert_any_call('--step', dest='step', action='store_true', help='one-step-at-a-time: confirm each task before running')

    mock_runas.assert_called_once_with(mock_parser)
    mock_inventory.assert_called_once_with(mock_parser)
    mock_connect.assert_called_once_with(mock_parser)
    mock_check.assert_called_once_with(mock_parser)
    mock_vault.assert_called_once_with(mock_parser)
    mock_fork.assert_called_once_with(mock_parser)
    mock_module.assert_called_once_with(mock_parser)
    mock_basedir.assert_called_once_with(mock_parser)
    mock_runtask.assert_called_once_with(mock_parser)
    mock_tasknoplay.assert_called_once_with(mock_parser)
