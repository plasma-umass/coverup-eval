# file: lib/ansible/cli/console.py:357-364
# asked: {"lines": [357, 359, 360, 361, 363, 364], "branches": [[359, 360], [359, 363]]}
# gained: {"lines": [357, 359, 360, 361, 363, 364], "branches": [[359, 360], [359, 363]]}

import pytest
from ansible.cli.console import ConsoleCLI
from unittest.mock import patch, MagicMock

@pytest.fixture
def console_cli():
    return ConsoleCLI(args=['test'])

def test_do_become_method_with_arg(console_cli):
    with patch('ansible.cli.console.display') as mock_display:
        console_cli.do_become_method('sudo')
        assert console_cli.become_method == 'sudo'
        mock_display.v.assert_called_once_with('become_method changed to sudo')

def test_do_become_method_without_arg(console_cli):
    with patch('ansible.cli.console.display') as mock_display:
        console_cli.do_become_method('')
        mock_display.display.assert_called_once_with('Please specify a become_method, e.g. `become_method su`')
        mock_display.v.assert_called_once_with('Current become_method is None')
