# file thefuck/rules/lein_not_task.py:6-11
# lines [6, 7, 8, 9, 10, 11]
# branches []

import pytest
from thefuck.types import Command
from thefuck.rules.lein_not_task import match

@pytest.fixture
def lein_not_task_error():
    return '''lein foo
'foo' is not a task. See 'lein help'.
Did you mean this?
     doo'''

@pytest.fixture
def lein_not_task_command(lein_not_task_error):
    return Command('lein foo', lein_not_task_error)

@pytest.fixture
def lein_other_error():
    return '''lein bar
Some other error message that doesn't match the pattern.'''

@pytest.fixture
def lein_other_command(lein_other_error):
    return Command('lein bar', lein_other_error)

def test_match_with_lein_not_task_error(lein_not_task_command):
    assert match(lein_not_task_command)

def test_not_match_with_other_error(lein_other_command):
    assert not match(lein_other_command)
