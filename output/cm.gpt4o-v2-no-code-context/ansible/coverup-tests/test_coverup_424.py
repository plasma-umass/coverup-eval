# file: lib/ansible/cli/console.py:431-437
# asked: {"lines": [431, 432, 433, 434, 435, 437], "branches": [[432, 0], [432, 433]]}
# gained: {"lines": [431, 432, 433, 434, 435, 437], "branches": [[432, 0], [432, 433]]}

import pytest
from ansible.cli.console import ConsoleCLI

class MockCLI(ConsoleCLI):
    def __init__(self, modules, module_args):
        self.modules = modules
        self._module_args = module_args

    def module_args(self, module):
        return self._module_args

@pytest.fixture
def mock_cli():
    modules = ['test_module']
    module_args = ['arg1', 'arg2', 'arg3']
    return MockCLI(modules, module_args)

def test_completedefault_with_matching_module(mock_cli):
    text = 'arg'
    line = 'test_module arg'
    begidx = 12
    endidx = 15

    completions = mock_cli.completedefault(text, line, begidx, endidx)
    assert completions == ['arg1=', 'arg2=', 'arg3=']

def test_completedefault_with_non_matching_module(mock_cli):
    text = 'arg'
    line = 'nonexistent_module arg'
    begidx = 18
    endidx = 21

    completions = mock_cli.completedefault(text, line, begidx, endidx)
    assert completions is None
