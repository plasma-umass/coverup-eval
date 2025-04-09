# file lib/ansible/cli/console.py:322-329
# lines [322, 324, 325, 326, 328, 329]
# branches ['324->325', '324->328', '325->exit', '325->326', '328->exit', '328->329']

import pytest
from unittest.mock import MagicMock, call
from ansible.cli.console import ConsoleCLI
from ansible.utils.display import Display

# Mock the display object to capture the output
@pytest.fixture
def mock_display(mocker):
    return mocker.patch('ansible.utils.display.Display.display')

# Create a test ConsoleCLI instance with necessary attributes
@pytest.fixture
def console_cli(mocker):
    mocker.patch('ansible.cli.console.CLI.__init__', return_value=None)
    cli = ConsoleCLI(args=[])
    cli.groups = ['group1', 'group2']
    cli.selected = [type('Host', (object,), {'name': 'host1'}),
                    type('Host', (object,), {'name': 'host2'})]
    return cli

# Test the 'do_list' method with 'groups' argument
def test_do_list_groups(console_cli, mock_display):
    console_cli.do_list('groups')
    mock_display.assert_has_calls([call('group1'), call('group2')])

# Test the 'do_list' method with no argument
def test_do_list_hosts(console_cli, mock_display):
    console_cli.do_list('')
    mock_display.assert_has_calls([call('host1'), call('host2')])
