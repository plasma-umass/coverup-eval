# file lib/ansible/cli/console.py:302-320
# lines [302, 311, 312, 313, 314, 315, 316, 318, 320]
# branches ['311->312', '311->313', '313->314', '313->315', '315->316', '315->318']

import pytest
from unittest import mock
from ansible.cli.console import ConsoleCLI
from ansible.utils.display import Display

@pytest.fixture
def console_cli():
    cli = ConsoleCLI(args=['test'])
    cli.inventory = mock.Mock()
    cli.set_prompt = mock.Mock()
    return cli

def test_do_cd_no_arg(console_cli):
    console_cli.do_cd('')
    assert console_cli.cwd == '*'
    console_cli.set_prompt.assert_called_once()

def test_do_cd_root(console_cli):
    console_cli.do_cd('/')
    assert console_cli.cwd == 'all'
    console_cli.set_prompt.assert_called_once()

def test_do_cd_star(console_cli):
    console_cli.do_cd('*')
    assert console_cli.cwd == 'all'
    console_cli.set_prompt.assert_called_once()

def test_do_cd_valid_host(console_cli):
    console_cli.inventory.get_hosts.return_value = ['host1']
    console_cli.do_cd('webservers')
    assert console_cli.cwd == 'webservers'
    console_cli.set_prompt.assert_called_once()

def test_do_cd_no_host_matched(console_cli, mocker):
    mock_display = mocker.patch('ansible.cli.console.display.display')
    console_cli.inventory.get_hosts.return_value = []
    console_cli.do_cd('invalidhost')
    assert console_cli.cwd != 'invalidhost'
    mock_display.assert_called_once_with("no host matched")
    console_cli.set_prompt.assert_called_once()
