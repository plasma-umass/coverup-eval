# file pymonet/utils.py:117-137
# lines [117, 132, 133, 134, 135, 137]
# branches ['133->exit', '133->134', '134->133', '134->135']

import pytest
from pymonet.utils import cond

def test_cond_executes_missing_branches():
    # Setup conditions and execution functions
    condition_true = lambda x: True
    condition_false = lambda x: False
    execution_a = lambda x: 'A'
    execution_b = lambda x: 'B'

    # Create a condition list with a false condition followed by a true condition
    condition_list = [
        (condition_false, execution_a),
        (condition_true, execution_b),
    ]

    # Create the conditional function
    conditional_function = cond(condition_list)

    # Test that the second branch is executed when the first condition is False
    result = conditional_function(None)
    assert result == 'B', "The second branch should be executed and return 'B'"

    # Clean up is not necessary as no external state is modified
