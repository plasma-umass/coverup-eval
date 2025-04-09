# file thefuck/types.py:228-230
# lines [228, 229, 230]
# branches []

import pytest
from thefuck.types import CorrectedCommand

def test_corrected_command_repr():
    # Create an instance of CorrectedCommand with test values
    corrected_command = CorrectedCommand(script='test_script', side_effect='test_side_effect', priority=10)

    # Call __repr__ and capture the result
    repr_result = repr(corrected_command)

    # Assert that the __repr__ method returns the expected string
    expected_repr = "CorrectedCommand(script=test_script, side_effect=test_side_effect, priority=10)"
    assert repr_result == expected_repr
