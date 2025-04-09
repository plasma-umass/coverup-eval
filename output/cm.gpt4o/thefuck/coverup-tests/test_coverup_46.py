# file thefuck/rules/lein_not_task.py:6-11
# lines [6, 7, 8, 9, 10, 11]
# branches []

import pytest
from thefuck.rules.lein_not_task import match
from thefuck.types import Command

@pytest.fixture
def mock_command():
    return Command(script='lein some_task', output="some_task is not a task. See 'lein help'. Did you mean this?")

def test_match(mock_command):
    assert match(mock_command)

def test_no_match_wrong_script(mock_command):
    mock_command.script = 'not_lein some_task'
    assert not match(mock_command)

def test_no_match_missing_help(mock_command):
    mock_command.output = "some_task is not a task."
    assert not match(mock_command)

def test_no_match_missing_suggestion(mock_command):
    mock_command.output = "some_task is not a task. See 'lein help'"
    assert not match(mock_command)
