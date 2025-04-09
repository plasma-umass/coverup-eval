# file: lib/ansible/cli/console.py:431-437
# asked: {"lines": [431, 432, 433, 434, 435, 437], "branches": [[432, 0], [432, 433]]}
# gained: {"lines": [431, 432, 433, 434, 435, 437], "branches": [[432, 0], [432, 433]]}

import pytest
from unittest.mock import MagicMock
from ansible.cli.console import ConsoleCLI

class TestConsoleCLI:
    
    @pytest.fixture
    def console_cli(self):
        class TestCLI(ConsoleCLI):
            def __init__(self, args):
                super().__init__(args)
                self.modules = ['test_module']
            
            def module_args(self, module):
                return ['arg1', 'arg2', 'arg3']
        
        return TestCLI(args=['test'])

    def test_completedefault(self, console_cli):
        # Test when the first word in line is in self.modules
        completions = console_cli.completedefault('arg', 'test_module arg', 0, 0)
        assert completions == ['arg1=', 'arg2=', 'arg3=']

        # Test when the first word in line is not in self.modules
        completions = console_cli.completedefault('arg', 'other_module arg', 0, 0)
        assert completions is None
