# file thefuck/corrector.py:81-92
# lines [88, 89, 90, 91, 92]
# branches []

import pytest
from thefuck.types import Command, CorrectedCommand
from thefuck.corrector import get_corrected_commands

# Mock rule that always matches and returns a fixed corrected command
class AlwaysMatchRule:
    @staticmethod
    def is_match(command):
        return True

    @staticmethod
    def get_corrected_commands(command):
        yield CorrectedCommand(script='corrected_command', side_effect=None, priority=900)

# Test function to cover lines 88-92
def test_get_corrected_commands(mocker):
    # Mock the get_rules function to return a list with our AlwaysMatchRule
    mocker.patch('thefuck.corrector.get_rules', return_value=[AlwaysMatchRule()])
    
    # Create a fake command
    fake_command = Command('fake_command', 'fake_output')

    # Call the function to test
    corrected_commands = list(get_corrected_commands(fake_command))

    # Assert that the corrected command is returned
    assert corrected_commands == [CorrectedCommand(script='corrected_command', side_effect=None, priority=900)]

    # Cleanup is handled by pytest-mock through its mocker fixture
