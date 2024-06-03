# file thefuck/types.py:225-226
# lines [225, 226]
# branches []

import pytest
from unittest.mock import Mock

# Assuming the CorrectedCommand class is imported from thefuck.types
from thefuck.types import CorrectedCommand

@pytest.fixture
def corrected_command():
    script = "echo 'Hello, World!'"
    side_effect = None
    priority = 1
    return CorrectedCommand(script, side_effect, priority)

def test_corrected_command_hash(corrected_command):
    # Create a mock object to simulate the side effect
    mock_side_effect = Mock()
    corrected_command.side_effect = mock_side_effect

    # Calculate the hash
    cmd_hash = hash(corrected_command)

    # Verify the hash is calculated correctly
    expected_hash = hash((corrected_command.script, corrected_command.side_effect))
    assert cmd_hash == expected_hash

    # Clean up the mock
    mock_side_effect.reset_mock()
