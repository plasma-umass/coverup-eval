# file thefuck/corrector.py:81-92
# lines [81, 88, 89, 90, 91, 92]
# branches []

import pytest
from unittest.mock import Mock, patch
from thefuck.types import Command, CorrectedCommand
from thefuck.corrector import get_corrected_commands

@pytest.fixture
def mock_get_rules(mocker):
    return mocker.patch('thefuck.corrector.get_rules')

@pytest.fixture
def mock_organize_commands(mocker):
    return mocker.patch('thefuck.corrector.organize_commands')

def test_get_corrected_commands(mock_get_rules, mock_organize_commands):
    # Mocking the command
    command = Mock(spec=Command)
    
    # Mocking rules
    rule1 = Mock()
    rule1.is_match.return_value = True
    rule1.get_corrected_commands.return_value = [CorrectedCommand('echo test', 1, 1)]
    
    rule2 = Mock()
    rule2.is_match.return_value = False
    
    rule3 = Mock()
    rule3.is_match.return_value = True
    rule3.get_corrected_commands.return_value = [CorrectedCommand('echo test2', 2, 2)]
    
    mock_get_rules.return_value = [rule1, rule2, rule3]
    
    # Mocking organize_commands
    mock_organize_commands.side_effect = lambda cmds: list(cmds)
    
    # Call the function
    result = get_corrected_commands(command)
    
    # Assertions
    assert mock_get_rules.called
    assert rule1.is_match.called_with(command)
    assert rule1.get_corrected_commands.called_with(command)
    assert rule2.is_match.called_with(command)
    assert not rule2.get_corrected_commands.called
    assert rule3.is_match.called_with(command)
    assert rule3.get_corrected_commands.called_with(command)
    assert mock_organize_commands.called
    
    # Check the result
    assert result == [CorrectedCommand('echo test', 1, 1), CorrectedCommand('echo test2', 2, 2)]
