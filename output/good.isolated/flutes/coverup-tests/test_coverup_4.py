# file flutes/structure.py:16-32
# lines [16, 32]
# branches []

import pytest
from flutes.structure import reverse_map

def test_reverse_map():
    # Setup
    input_dict = {'apple': 2, 'banana': 0, 'cherry': 1}
    expected_output = ['banana', 'cherry', 'apple']

    # Exercise
    result = reverse_map(input_dict)

    # Verify
    assert result == expected_output, "The reverse_map function did not return the expected list."

    # Cleanup - nothing to do since there are no side effects from reverse_map

# This test will be collected and run by pytest, no top-level code is necessary.
