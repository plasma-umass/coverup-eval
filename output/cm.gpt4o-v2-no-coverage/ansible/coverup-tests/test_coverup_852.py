# file: lib/ansible/cli/console.py:261-273
# asked: {"lines": [261, 273], "branches": []}
# gained: {"lines": [261, 273], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.cli.console import ConsoleCLI

class TestConsoleCLI:
    
    @pytest.fixture
    def console_cli(self):
        return ConsoleCLI(args=['test'])

    def test_do_shell(self, console_cli, mocker):
        mock_default = mocker.patch.object(console_cli, 'default')
        console_cli.do_shell('ps aux | grep java | wc -l')
        mock_default.assert_called_once_with('ps aux | grep java | wc -l', True)
