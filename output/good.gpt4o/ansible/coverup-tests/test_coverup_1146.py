# file lib/ansible/cli/console.py:322-329
# lines [324, 325, 326, 328, 329]
# branches ['324->325', '324->328', '325->exit', '325->326', '328->exit', '328->329']

import pytest
from unittest import mock
from ansible.cli.console import ConsoleCLI
from ansible.utils.display import Display

@pytest.fixture
def console_cli():
    args = mock.Mock()
    cli = ConsoleCLI(args)
    cli.groups = ['group1', 'group2']
    cli.selected = [mock.Mock(name='host1'), mock.Mock(name='host2')]
    cli.selected[0].name = 'host1'
    cli.selected[1].name = 'host2'
    return cli

def test_do_list_groups(console_cli, mocker):
    display_mock = mocker.patch('ansible.cli.console.display.display')
    console_cli.do_list('groups')
    display_mock.assert_any_call('group1')
    display_mock.assert_any_call('group2')
    assert display_mock.call_count == 2

def test_do_list_hosts(console_cli, mocker):
    display_mock = mocker.patch('ansible.cli.console.display.display')
    console_cli.do_list('')
    display_mock.assert_any_call('host1')
    display_mock.assert_any_call('host2')
    assert display_mock.call_count == 2
