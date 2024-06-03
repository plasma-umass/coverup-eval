# file thefuck/types.py:205-215
# lines [205, 213, 214, 215]
# branches []

import pytest
from unittest.mock import Mock
from thefuck.types import CorrectedCommand

def test_corrected_command_initialization():
    script = "echo 'Hello, World!'"
    side_effect = Mock()
    priority = 10

    corrected_command = CorrectedCommand(script, side_effect, priority)

    assert corrected_command.script == script
    assert corrected_command.side_effect == side_effect
    assert corrected_command.priority == priority

    # Clean up
    side_effect.reset_mock()
