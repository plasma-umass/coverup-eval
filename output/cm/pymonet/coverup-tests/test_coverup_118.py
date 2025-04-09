# file pymonet/utils.py:117-137
# lines []
# branches ['133->exit']

import pytest
from pymonet.utils import cond

def test_cond_branch_exit_not_taken():
    # Setup
    def false_condition(x):
        return False

    def action(x):
        return x * 2

    condition_list = [
        (false_condition, action)
    ]

    # Execute
    conditional_action = cond(condition_list)

    # Verify
    assert conditional_action(3) is None

    # Cleanup - nothing to clean up as the test does not have side effects
