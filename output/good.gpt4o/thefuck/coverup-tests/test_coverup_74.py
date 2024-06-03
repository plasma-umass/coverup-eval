# file thefuck/rules/choco_install.py:4-7
# lines [4, 5, 6, 7]
# branches []

import pytest
from thefuck.rules.choco_install import match
from thefuck.types import Command

@pytest.fixture
def mock_command():
    return Command('choco install somepackage', 'Installing the following packages')

def test_match_choco_install(mock_command):
    assert match(mock_command)

def test_match_cinst_install():
    command = Command('cinst somepackage', 'Installing the following packages')
    assert match(command)

def test_no_match():
    command = Command('choco install somepackage', 'Some other output')
    assert not match(command)
