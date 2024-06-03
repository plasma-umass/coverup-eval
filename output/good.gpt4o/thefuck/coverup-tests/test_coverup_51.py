# file thefuck/rules/git_add_force.py:5-8
# lines [5, 6, 7, 8]
# branches []

import pytest
from thefuck.rules.git_add_force import match
from thefuck.types import Command

def test_match():
    command = Command(script='git add somefile', output='Use -f if you really want to add them.')
    assert match(command)

    command = Command(script='git add somefile', output='Some other error message')
    assert not match(command)

    command = Command(script='git commit -m "message"', output='Use -f if you really want to add them.')
    assert not match(command)

@pytest.fixture(autouse=True)
def cleanup(mocker):
    yield
    mocker.stopall()
