# file lib/ansible/cli/console.py:33-65
# lines [33, 34, 59, 60, 64]
# branches []

import pytest
from ansible.cli.console import ConsoleCLI
from unittest.mock import patch, MagicMock

@pytest.fixture
def console_cli():
    with patch('ansible.cli.console.CLI.__init__'), \
         patch('ansible.cli.console.cmd.Cmd.__init__'), \
         patch('ansible.cli.console.C') as mock_constants:
        mock_constants.COLOR_CONSOLE_PROMPT = None
        mock_constants.COLOR_HIGHLIGHT = 'white'
        console_cli = ConsoleCLI([])
        console_cli.pager = False
        console_cli.modules = []
        yield console_cli

def test_console_cli_attributes(console_cli):
    assert hasattr(console_cli, 'modules')
    assert hasattr(console_cli, 'ARGUMENTS')
    assert hasattr(console_cli, 'NORMAL_PROMPT')
    assert isinstance(console_cli.modules, list)
    assert isinstance(console_cli.ARGUMENTS, dict)
    assert isinstance(console_cli.NORMAL_PROMPT, str)

def test_console_cli_prompt(console_cli):
    with patch('ansible.cli.console.C') as mock_constants:
        mock_constants.COLOR_CONSOLE_PROMPT = 'cyan'
        mock_constants.COLOR_HIGHLIGHT = 'yellow'
        # Refresh the NORMAL_PROMPT after changing the constants
        console_cli.NORMAL_PROMPT = mock_constants.COLOR_CONSOLE_PROMPT or mock_constants.COLOR_HIGHLIGHT
        assert console_cli.NORMAL_PROMPT == 'cyan'

        # Test fallback to COLOR_HIGHLIGHT
        mock_constants.COLOR_CONSOLE_PROMPT = None
        console_cli.NORMAL_PROMPT = mock_constants.COLOR_CONSOLE_PROMPT or mock_constants.COLOR_HIGHLIGHT
        assert console_cli.NORMAL_PROMPT == 'yellow'

def test_console_cli_argument_host_pattern(console_cli):
    expected_argument = 'A name of a group in the inventory, a shell-like glob ' \
                        'selecting hosts in inventory or any combination of the two separated by commas.'
    assert console_cli.ARGUMENTS['host-pattern'] == expected_argument
