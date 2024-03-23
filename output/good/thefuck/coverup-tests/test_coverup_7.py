# file thefuck/rules/brew_install.py:26-34
# lines [26, 27, 28, 30, 31, 32, 33, 34]
# branches ['30->31', '30->34']

import pytest
from thefuck.types import Command
from thefuck.rules.brew_install import match
from unittest.mock import Mock

@pytest.fixture
def brew_install_no_formula(mocker):
    mocker.patch('thefuck.rules.brew_install._get_similar_formula', return_value=['similar_formula'])

def test_match_with_no_available_formula_and_similar(brew_install_no_formula):
    command = Command('brew install nonexistentformula', 'Error: No available formula for nonexistentformula')
    assert match(command)

def test_match_with_no_available_formula_and_no_similar(mocker, brew_install_no_formula):
    mocker.patch('thefuck.rules.brew_install._get_similar_formula', return_value=[])
    command = Command('brew install nonexistentformula', 'Error: No available formula for nonexistentformula')
    assert not match(command)

def test_match_with_no_error_in_output():
    command = Command('brew install validformula', 'Some other output without the error')
    assert not match(command)

def test_match_with_no_brew_install_in_script():
    command = Command('brew search validformula', 'Error: No available formula for validformula')
    assert not match(command)
