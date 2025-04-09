# file pymonet/utils.py:117-137
# lines [117, 132, 133, 134, 135, 137]
# branches ['133->exit', '133->134', '134->133', '134->135']

import pytest
from pymonet.utils import cond

def test_cond(mocker):
    # Mock condition and execute functions
    condition_true = mocker.Mock(return_value=True)
    condition_false = mocker.Mock(return_value=False)
    execute_function = mocker.Mock(return_value="executed")

    # Create a condition list with both true and false conditions
    condition_list = [
        (condition_false, execute_function),  # This should be skipped
        (condition_true, execute_function)    # This should be executed
    ]

    # Create the conditional function
    conditional_function = cond(condition_list)

    # Call the conditional function and assert the result
    result = conditional_function()
    assert result == "executed"

    # Verify that the correct functions were called
    condition_false.assert_called_once()
    condition_true.assert_called_once()
    execute_function.assert_called_once()

    # Clean up mocks
    mocker.stopall()
