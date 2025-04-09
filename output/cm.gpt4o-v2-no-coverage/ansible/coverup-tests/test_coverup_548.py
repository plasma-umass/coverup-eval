# file: lib/ansible/cli/console.py:375-382
# asked: {"lines": [375, 377, 378, 379, 381, 382], "branches": [[377, 378], [377, 381]]}
# gained: {"lines": [375, 377, 378, 379, 381, 382], "branches": [[377, 378], [377, 381]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.cli.console import ConsoleCLI
from ansible.module_utils.parsing.convert_bool import boolean

class TestConsoleCLI:
    
    @pytest.fixture
    def console_cli(self):
        return ConsoleCLI(args=['test'])

    @patch('ansible.cli.console.display.display')
    def test_do_diff_with_arg(self, mock_display, console_cli):
        console_cli.diff = False
        console_cli.do_diff('yes')
        assert console_cli.diff is True
        mock_display.assert_called_with("diff mode changed to True")

    @patch('ansible.cli.console.display.display')
    @patch('ansible.cli.console.display.v')
    def test_do_diff_without_arg(self, mock_v, mock_display, console_cli):
        console_cli.diff = False
        console_cli.do_diff('')
        mock_display.assert_called_with("Please specify a diff value , e.g. `diff yes`")
        mock_v.assert_called_with("diff mode is currently False")
