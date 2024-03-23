# file lib/ansible/cli/adhoc.py:28-54
# lines [30, 31, 32, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 48, 49, 50, 51, 52, 53, 54]
# branches []

import pytest
from ansible.cli.adhoc import AdHocCLI
from unittest.mock import patch, MagicMock
from ansible.cli import opt_help

# Mock the constants used in the AdHocCLI class
class MockConstants:
    DEFAULT_MODULE_ARGS = ''
    DEFAULT_MODULE_NAME = 'ping'

@pytest.fixture
def adhoc_cli():
    with patch('ansible.cli.adhoc.C', new=MockConstants):
        cli = AdHocCLI(['adhoc'])
        yield cli

def test_init_parser(adhoc_cli, mocker):
    mocker.patch('ansible.cli.opt_help.add_runas_options')
    mocker.patch('ansible.cli.opt_help.add_inventory_options')
    mocker.patch('ansible.cli.opt_help.add_async_options')
    mocker.patch('ansible.cli.opt_help.add_output_options')
    mocker.patch('ansible.cli.opt_help.add_connect_options')
    mocker.patch('ansible.cli.opt_help.add_check_options')
    mocker.patch('ansible.cli.opt_help.add_runtask_options')
    mocker.patch('ansible.cli.opt_help.add_vault_options')
    mocker.patch('ansible.cli.opt_help.add_fork_options')
    mocker.patch('ansible.cli.opt_help.add_module_options')
    mocker.patch('ansible.cli.opt_help.add_basedir_options')
    mocker.patch('ansible.cli.opt_help.add_tasknoplay_options')

    adhoc_cli.init_parser()

    # Assertions to check if the parser is initialized with the correct arguments
    assert adhoc_cli.parser is not None
    assert any(opt.dest == 'module_args' for opt in adhoc_cli.parser._actions), "Parser should have 'module_args' option"
    assert any(opt.dest == 'module_name' for opt in adhoc_cli.parser._actions), "Parser should have 'module_name' option"
    assert any(opt.metavar == 'pattern' for opt in adhoc_cli.parser._actions), "Parser should have 'pattern' argument"

    # Verify that the mocked methods were called
    opt_help.add_runas_options.assert_called_once_with(adhoc_cli.parser)
    opt_help.add_inventory_options.assert_called_once_with(adhoc_cli.parser)
    opt_help.add_async_options.assert_called_once_with(adhoc_cli.parser)
    opt_help.add_output_options.assert_called_once_with(adhoc_cli.parser)
    opt_help.add_connect_options.assert_called_once_with(adhoc_cli.parser)
    opt_help.add_check_options.assert_called_once_with(adhoc_cli.parser)
    opt_help.add_runtask_options.assert_called_once_with(adhoc_cli.parser)
    opt_help.add_vault_options.assert_called_once_with(adhoc_cli.parser)
    opt_help.add_fork_options.assert_called_once_with(adhoc_cli.parser)
    opt_help.add_module_options.assert_called_once_with(adhoc_cli.parser)
    opt_help.add_basedir_options.assert_called_once_with(adhoc_cli.parser)
    opt_help.add_tasknoplay_options.assert_called_once_with(adhoc_cli.parser)
