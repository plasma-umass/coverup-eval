# file flutes/iterator.py:160-161
# lines [160, 161]
# branches []

import pytest
from flutes.iterator import scanl
from typing import List

def test_scanl():
    # Define a simple addition function for testing
    def add(x, y):
        return x + y

    # Create a list to be used with scanl
    input_list = [1, 2, 3, 4]

    # Expected result after scanl with add function
    expected_result = [1, 3, 6, 10]

    # Call scanl with the add function and the input list
    result_iterator = scanl(add, input_list)

    # Convert the result iterator to a list for comparison
    result_list = list(result_iterator)

    # Assert that the result matches the expected result
    assert result_list == expected_result, "scanl did not produce the expected result"

# Note: The actual implementation of scanl is not provided, so this test assumes that
# scanl is implemented correctly and will produce the expected result when given the add
# function and the input list. If the implementation of scanl is incorrect, this test may fail.
