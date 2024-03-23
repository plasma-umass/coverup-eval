# file thefuck/rules/vagrant_up.py:5-7
# lines [5, 6, 7]
# branches []

import pytest
from thefuck.types import Command
from thefuck.rules.vagrant_up import match

@pytest.fixture
def vagrant_not_up_output():
    return "A Vagrant environment or target machine is required to run this command. Run `vagrant up` to create one."

def test_vagrant_up_match(mocker, vagrant_not_up_output):
    command = Command('vagrant provision', vagrant_not_up_output)
    assert match(command)

def test_vagrant_up_not_match(mocker):
    command = Command('vagrant provision', 'All good!')
    assert not match(command)
