# file thefuck/rules/no_such_file.py:13-18
# lines [13, 14, 15, 16, 18]
# branches ['14->15', '14->18', '15->14', '15->16']

import pytest
from thefuck.rules.no_such_file import match
from thefuck.types import Command

@pytest.fixture
def no_such_file_output():
    return "bash: line 1: no_such_command: No such file or directory"

@pytest.fixture
def file_exists_output():
    return "bash: line 1: existing_command: command found"

def test_match_when_file_does_not_exist(mocker, no_such_file_output):
    mocker.patch('thefuck.rules.no_such_file.patterns', [r'No such file or directory'])
    command = Command('no_such_command', no_such_file_output)
    assert match(command) == True

def test_match_when_file_exists(mocker, file_exists_output):
    mocker.patch('thefuck.rules.no_such_file.patterns', [r'No such file or directory'])
    command = Command('existing_command', file_exists_output)
    assert match(command) == False
