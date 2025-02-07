# file: lib/ansible/cli/console.py:322-329
# asked: {"lines": [322, 324, 325, 326, 328, 329], "branches": [[324, 325], [324, 328], [325, 0], [325, 326], [328, 0], [328, 329]]}
# gained: {"lines": [322, 324, 325, 326, 328, 329], "branches": [[324, 325], [324, 328], [325, 0], [325, 326], [328, 0], [328, 329]]}

import pytest
from unittest.mock import MagicMock
from ansible.cli.console import ConsoleCLI

@pytest.fixture
def console_cli():
    cli = ConsoleCLI(args=['test'])
    cli.groups = ['group1', 'group2']
    host1 = MagicMock()
    host1.name = 'host1'
    host2 = MagicMock()
    host2.name = 'host2'
    cli.selected = [host1, host2]
    return cli

def test_do_list_groups(console_cli, mocker):
    mock_display = mocker.patch('ansible.cli.console.display.display')
    console_cli.do_list('groups')
    mock_display.assert_any_call('group1')
    mock_display.assert_any_call('group2')
    assert mock_display.call_count == 2

def test_do_list_hosts(console_cli, mocker):
    mock_display = mocker.patch('ansible.cli.console.display.display')
    console_cli.do_list('')
    mock_display.assert_any_call('host1')
    mock_display.assert_any_call('host2')
    assert mock_display.call_count == 2
