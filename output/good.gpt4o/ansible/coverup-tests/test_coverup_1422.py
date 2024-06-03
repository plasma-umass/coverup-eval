# file lib/ansible/cli/console.py:431-437
# lines [432, 433, 434, 435, 437]
# branches ['432->exit', '432->433']

import pytest
from ansible.cli.console import ConsoleCLI

class MockCLI(ConsoleCLI):
    def __init__(self):
        self.modules = ['test_module']
    
    def module_args(self, module_name):
        return ['arg1', 'arg2', 'arg3']

@pytest.fixture
def mock_cli():
    return MockCLI()

def test_completedefault(mock_cli):
    line = 'test_module arg'
    text = 'arg'
    begidx = 12
    endidx = 15

    result = mock_cli.completedefault(text, line, begidx, endidx)
    
    assert result == ['arg1=', 'arg2=', 'arg3=']
