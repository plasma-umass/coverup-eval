# file: lib/ansible/cli/playbook.py:32-59
# asked: {"lines": [35, 36, 37, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 51, 52, 53, 54, 55, 56, 57, 58, 59], "branches": []}
# gained: {"lines": [35, 36, 37, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 51, 52, 53, 54, 55, 56, 57, 58, 59], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.cli.playbook import PlaybookCLI
from ansible.cli.arguments import option_helpers as opt_help
from argparse import ArgumentParser

@pytest.fixture
def cli(mocker):
    mocker.patch('ansible.cli.CLI.__init__', return_value=None)
    cli_instance = PlaybookCLI(args=['test'])
    cli_instance.parser = ArgumentParser()
    return cli_instance

def test_init_parser(cli, mocker):
    mock_super = mocker.patch('ansible.cli.CLI.init_parser', return_value=None)
    mock_add_argument = mocker.patch.object(cli.parser, 'add_argument', return_value=None)

    mocker.patch.object(opt_help, 'add_connect_options', return_value=None)
    mocker.patch.object(opt_help, 'add_meta_options', return_value=None)
    mocker.patch.object(opt_help, 'add_runas_options', return_value=None)
    mocker.patch.object(opt_help, 'add_subset_options', return_value=None)
    mocker.patch.object(opt_help, 'add_check_options', return_value=None)
    mocker.patch.object(opt_help, 'add_inventory_options', return_value=None)
    mocker.patch.object(opt_help, 'add_runtask_options', return_value=None)
    mocker.patch.object(opt_help, 'add_vault_options', return_value=None)
    mocker.patch.object(opt_help, 'add_fork_options', return_value=None)
    mocker.patch.object(opt_help, 'add_module_options', return_value=None)

    cli.init_parser()

    mock_super.assert_called_once_with(
        usage="%prog [options] playbook.yml [playbook2 ...]",
        desc="Runs Ansible playbooks, executing the defined tasks on the targeted hosts."
    )
    opt_help.add_connect_options.assert_called_once_with(cli.parser)
    opt_help.add_meta_options.assert_called_once_with(cli.parser)
    opt_help.add_runas_options.assert_called_once_with(cli.parser)
    opt_help.add_subset_options.assert_called_once_with(cli.parser)
    opt_help.add_check_options.assert_called_once_with(cli.parser)
    opt_help.add_inventory_options.assert_called_once_with(cli.parser)
    opt_help.add_runtask_options.assert_called_once_with(cli.parser)
    opt_help.add_vault_options.assert_called_once_with(cli.parser)
    opt_help.add_fork_options.assert_called_once_with(cli.parser)
    opt_help.add_module_options.assert_called_once_with(cli.parser)

    mock_add_argument.assert_any_call('--list-tasks', dest='listtasks', action='store_true', help="list all tasks that would be executed")
    mock_add_argument.assert_any_call('--list-tags', dest='listtags', action='store_true', help="list all available tags")
    mock_add_argument.assert_any_call('--step', dest='step', action='store_true', help="one-step-at-a-time: confirm each task before running")
    mock_add_argument.assert_any_call('--start-at-task', dest='start_at_task', help="start the playbook at the task matching this name")
    mock_add_argument.assert_any_call('args', help='Playbook(s)', metavar='playbook', nargs='+')
