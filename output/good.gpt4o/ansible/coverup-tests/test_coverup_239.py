# file lib/ansible/cli/console.py:94-113
# lines [94, 95, 96, 97, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 111, 112, 113]
# branches []

import pytest
from unittest import mock
from ansible.cli.console import ConsoleCLI
from argparse import ArgumentParser

@pytest.fixture
def mock_opt_help(mocker):
    opt_help = mocker.Mock()
    mocker.patch('ansible.cli.console.opt_help', opt_help)
    return opt_help

@pytest.fixture
def mock_cli_args():
    return ['ansible-console']

def test_consolecli_init_parser(mock_opt_help, mock_cli_args):
    cli = ConsoleCLI(mock_cli_args)
    cli.parser = ArgumentParser()
    
    cli.init_parser()
    
    mock_opt_help.add_runas_options.assert_called_once_with(cli.parser)
    mock_opt_help.add_inventory_options.assert_called_once_with(cli.parser)
    mock_opt_help.add_connect_options.assert_called_once_with(cli.parser)
    mock_opt_help.add_check_options.assert_called_once_with(cli.parser)
    mock_opt_help.add_vault_options.assert_called_once_with(cli.parser)
    mock_opt_help.add_fork_options.assert_called_once_with(cli.parser)
    mock_opt_help.add_module_options.assert_called_once_with(cli.parser)
    mock_opt_help.add_basedir_options.assert_called_once_with(cli.parser)
    mock_opt_help.add_runtask_options.assert_called_once_with(cli.parser)
    mock_opt_help.add_tasknoplay_options.assert_called_once_with(cli.parser)
    
    args = cli.parser.parse_args(['--step'])
    assert args.step is True
    assert args.pattern == 'all'
    
    args = cli.parser.parse_args(['some_pattern'])
    assert args.step is False
    assert args.pattern == 'some_pattern'
