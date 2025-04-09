# file thefuck/rules/brew_install.py:37-42
# lines [37, 38, 39, 40, 42]
# branches []

import pytest
from unittest.mock import patch
from thefuck.rules.brew_install import get_new_command

def test_get_new_command(mocker):
    command = mocker.Mock()
    command.output = "Error: No available formula for nonexistentformula"
    command.script = "brew install nonexistentformula"
    
    mock_get_similar_formula = mocker.patch('thefuck.rules.brew_install._get_similar_formula', return_value='existingformula')
    mock_replace_argument = mocker.patch('thefuck.rules.brew_install.replace_argument', return_value='brew install existingformula')
    
    new_command = get_new_command(command)
    
    assert new_command == 'brew install existingformula'
    mock_get_similar_formula.assert_called_once_with('nonexistentformula')
    mock_replace_argument.assert_called_once_with('brew install nonexistentformula', 'nonexistentformula', 'existingformula')
