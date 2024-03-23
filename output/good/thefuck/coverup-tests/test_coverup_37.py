# file thefuck/rules/cp_create_destination.py:5-11
# lines [5, 6, 7, 8, 9, 10]
# branches []

import pytest
from thefuck.types import Command
from thefuck.rules.cp_create_destination import match
from thefuck.system import Path

@pytest.fixture
def no_such_file_error():
    return Command('cp foo bar', 'cp: cannot stat \'foo\': No such file or directory')

@pytest.fixture
def directory_does_not_exist_error():
    return Command('cp foo bar/', 'cp: directory bar does not exist')

@pytest.fixture
def other_error():
    return Command('cp foo bar', 'cp: some other error')

def test_match_no_such_file_error(no_such_file_error):
    assert match(no_such_file_error)

def test_match_directory_does_not_exist_error(directory_does_not_exist_error):
    assert match(directory_does_not_exist_error)

def test_match_other_error_should_not_match(other_error):
    assert not match(other_error)
