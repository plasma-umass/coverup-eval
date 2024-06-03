# file pymonet/utils.py:117-137
# lines []
# branches ['133->exit']

import pytest
from pymonet.utils import cond

def test_cond_branch_coverage():
    # Define condition and execute functions
    def condition_true(x):
        return x == 1

    def condition_false(x):
        return x == 2

    def execute_true(x):
        return "True branch executed"

    def execute_false(x):
        return "False branch executed"

    # Create a condition list with both true and false conditions
    condition_list = [
        (condition_false, execute_false),
        (condition_true, execute_true)
    ]

    # Get the result function from cond
    result_function = cond(condition_list)

    # Test with an input that triggers the true condition
    assert result_function(1) == "True branch executed"

    # Test with an input that does not trigger any condition
    assert result_function(3) is None

    # Test with an input that triggers the false condition
    assert result_function(2) == "False branch executed"
