# file thefuck/types.py:228-230
# lines [228, 229, 230]
# branches []

import pytest

# Assuming CorrectedCommand is imported from thefuck.types
from thefuck.types import CorrectedCommand

@pytest.fixture
def corrected_command():
    cmd = CorrectedCommand("echo 'Hello, World!'", None, 100)
    return cmd

def test_corrected_command_repr(corrected_command):
    expected_repr = "CorrectedCommand(script=echo 'Hello, World!', side_effect=None, priority=100)"
    assert repr(corrected_command) == expected_repr

# Clean up fixture if necessary
@pytest.fixture(autouse=True)
def cleanup():
    yield
    # Add any necessary cleanup code here
