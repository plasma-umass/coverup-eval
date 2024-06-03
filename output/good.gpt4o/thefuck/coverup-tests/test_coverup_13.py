# file thefuck/rules/no_such_file.py:21-30
# lines [21, 22, 23, 25, 26, 27, 29, 30]
# branches ['22->exit', '22->23', '25->22', '25->26']

import pytest
import re
from unittest.mock import Mock, patch
from thefuck.rules.no_such_file import get_new_command

@pytest.fixture
def mock_shell_and(mocker):
    return mocker.patch('thefuck.rules.no_such_file.shell.and_', return_value='mkdir -p {} && {}')

def test_get_new_command(mock_shell_and):
    command = Mock()
    command.output = "bash: ./some/nonexistent/file.txt: No such file or directory"
    command.script = "some_command"
    
    patterns = [r'\./([^:]+): No such file or directory']
    
    with patch('thefuck.rules.no_such_file.patterns', patterns):
        new_command = get_new_command(command)
    
    assert new_command == 'mkdir -p some/nonexistent && some_command'
