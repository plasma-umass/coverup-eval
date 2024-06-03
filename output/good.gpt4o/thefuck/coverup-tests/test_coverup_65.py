# file thefuck/rules/vagrant_up.py:5-7
# lines [5, 6, 7]
# branches []

import pytest
from thefuck.rules.vagrant_up import match
from thefuck.types import Command

@pytest.mark.parametrize('output', [
    'You should run `vagrant up` to start the machine',
    'Please run `vagrant up` to continue',
    'run `vagrant up` to fix the issue'
])
def test_match_vagrant_up(output):
    command = Command('vagrant', output)
    assert match(command)

@pytest.mark.parametrize('output', [
    'You should run vagrant up to start the machine',
    'Please run vagrant up to continue',
    'run vagrant up to fix the issue'
])
def test_no_match_vagrant_up(output):
    command = Command('vagrant', output)
    assert not match(command)
