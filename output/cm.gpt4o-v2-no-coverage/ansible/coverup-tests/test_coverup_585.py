# file: lib/ansible/cli/console.py:340-346
# asked: {"lines": [340, 342, 343, 344, 346], "branches": [[342, 343], [342, 346]]}
# gained: {"lines": [340, 342, 343, 344, 346], "branches": [[342, 343], [342, 346]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.cli.console import ConsoleCLI

class TestConsoleCLI:
    
    @pytest.fixture
    def console_cli(self):
        return ConsoleCLI(args=['test'])

    @patch('ansible.cli.console.display.display')
    def test_do_remote_user_with_arg(self, mock_display, console_cli):
        console_cli.set_prompt = MagicMock()
        console_cli.do_remote_user('test_user')
        assert console_cli.remote_user == 'test_user'
        console_cli.set_prompt.assert_called_once()
        mock_display.assert_not_called()

    @patch('ansible.cli.console.display.display')
    def test_do_remote_user_without_arg(self, mock_display, console_cli):
        console_cli.do_remote_user('')
        mock_display.assert_called_once_with("Please specify a remote user, e.g. `remote_user root`")
