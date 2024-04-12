# file thefuck/types.py:205-215
# lines [205, 213, 214, 215]
# branches []

import pytest
from thefuck.types import CorrectedCommand

def test_corrected_command_initialization():
    # Setup: Define a side_effect function and priority
    def side_effect(command, basestring):
        pass
    priority = 10

    # Exercise: Create an instance of CorrectedCommand
    corrected_command = CorrectedCommand('ls -la', side_effect, priority)

    # Verify: Check if the instance has the correct attributes
    assert corrected_command.script == 'ls -la'
    assert corrected_command.side_effect == side_effect
    assert corrected_command.priority == priority

    # Cleanup: No cleanup required as no external resources are modified
