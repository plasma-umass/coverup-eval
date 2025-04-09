# file thefuck/types.py:202-204
# lines [202, 203]
# branches []

import pytest
from thefuck.types import CorrectedCommand

def test_corrected_command_initialization(mocker):
    # Mock the required arguments for CorrectedCommand
    script = mocker.Mock()
    side_effect = mocker.Mock()
    priority = mocker.Mock()

    # Test the initialization of CorrectedCommand
    cmd = CorrectedCommand(script, side_effect, priority)
    assert isinstance(cmd, CorrectedCommand)

# Ensure the test is cleaned up properly
@pytest.fixture(autouse=True)
def cleanup(mocker):
    yield
    mocker.stopall()
