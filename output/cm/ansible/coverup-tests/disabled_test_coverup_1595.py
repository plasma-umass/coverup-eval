# file lib/ansible/cli/console.py:322-329
# lines [324, 325, 326, 328, 329]
# branches ['324->325', '324->328', '325->exit', '325->326', '328->exit', '328->329']

import pytest
from ansible.cli.console import ConsoleCLI
from ansible.utils.display import Display

# Mock the display object to prevent actual output during tests
@pytest.fixture
def mock_display(mocker):
    return mocker.patch.object(Display, 'display')

# Fixture to create a ConsoleCLI instance with necessary setup
@pytest.fixture
def console_cli(mocker):
    mocker.patch('ansible.cli.console.CLI.__init__', return_value=None)
    cli = ConsoleCLI([])
    cli.groups = ['group1', 'group2']
    cli.selected = [type('Host', (object,), {'name': 'host1'}),
                    type('Host', (object,), {'name': 'host2'})]
    return cli

# Test function to cover lines 324-326
def test_do_list_groups(console_cli, mock_display):
    console_cli.do_list('groups')
    assert mock_display.call_count == len(console_cli.groups)
    mock_display.assert_any_call('group1')
    mock_display.assert_any_call('group2')

# Test function to cover lines 328-329
def test_do_list_hosts(console_cli, mock_display):
    console_cli.do_list('')
    assert mock_display.call_count == len(console_cli.selected)
    mock_display.assert_any_call('host1')
    mock_display.assert_any_call('host2')
