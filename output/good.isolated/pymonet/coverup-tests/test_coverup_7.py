# file pymonet/semigroups.py:160-177
# lines [160, 161, 165, 167, 168, 170, 177]
# branches []

import pytest
from pymonet.semigroups import Min

def test_min_concat_and_str(mocker):
    # Setup: create two Min instances
    min1 = Min(10)
    min2 = Min(20)

    # Exercise: Concatenate min1 and min2
    result = min1.concat(min2)

    # Verify: Check if the result is the smallest of the two
    assert result.value == 10
    assert str(result) == 'Min[value=10]'

    # Cleanup: No cleanup required for this test
