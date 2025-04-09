# file lib/ansible/cli/console.py:322-329
# lines [324, 325, 326, 328, 329]
# branches ['324->325', '324->328', '325->exit', '325->326', '328->exit', '328->329']

import pytest
from ansible.cli.console import ConsoleCLI
from ansible.utils.display import Display

# Mock the display module to prevent actual printing
@pytest.fixture
def mock_display(mocker):
    return mocker.patch.object(Display, 'display')

# Fixture to create a ConsoleCLI instance with necessary setup
@pytest.fixture
def console_cli(mocker):
    mocker.patch('ansible.cli.console.CLI.__init__', return_value=None)
    cli = ConsoleCLI(['console'])
    cli.groups = ['group1', 'group2']
    cli.selected = []
    return cli

# Test function to cover lines 324-326
def test_do_list_groups(console_cli, mock_display):
    console_cli.do_list('groups')
    assert mock_display.call_count == len(console_cli.groups)
    mock_display.assert_any_call('group1')
    mock_display.assert_any_call('group2')

# Test function to cover lines 328-329
def test_do_list_hosts(console_cli, mock_display):
    # Mocking a host object with a 'name' attribute
    mock_host = type('Host', (object,), {'name': 'host1'})
    console_cli.selected.append(mock_host)

    console_cli.do_list('hosts')
    assert mock_display.call_count == len(console_cli.selected)
    mock_display.assert_called_once_with('host1')
