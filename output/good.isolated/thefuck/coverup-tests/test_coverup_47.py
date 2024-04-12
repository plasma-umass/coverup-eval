# file thefuck/rules/brew_install.py:37-42
# lines [37, 38, 39, 40, 42]
# branches []

import pytest
from thefuck.types import Command
from thefuck.rules.brew_install import get_new_command
from unittest.mock import Mock

@pytest.fixture
def mock_get_similar_formula(mocker):
    return mocker.patch('thefuck.rules.brew_install._get_similar_formula', return_value='similar_formula')

def test_get_new_command(mock_get_similar_formula):
    command = Command('brew install nonexistformula', 'Error: No available formula for nonexistformula')
    new_command = get_new_command(command)
    assert new_command == 'brew install similar_formula'
    mock_get_similar_formula.assert_called_once_with('nonexistformula')
