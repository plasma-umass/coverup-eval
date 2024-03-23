# file mimesis/providers/numbers.py:73-93
# lines [73, 74, 75, 76, 77, 78, 91, 92, 93]
# branches []

import pytest
from mimesis.providers.numbers import Numbers
from mimesis.random import Random

# Mocking the Random.uniform method
def test_complex_number_full_coverage(mocker):
    # Create an instance of Numbers
    numbers = Numbers()

    # Create a mock for the Random.uniform method
    mock_uniform = mocker.patch.object(Random, 'uniform', side_effect=[0.5, 0.7])

    # Call the method under test
    result = numbers.complex_number(0.0, 1.0, 0.0, 1.0, 15, 15)

    # Assert that the mock was called with the correct parameters
    mock_uniform.assert_any_call(0.0, 1.0, 15)
    mock_uniform.assert_any_call(0.0, 1.0, 15)

    # Assert that the result is a complex number with the expected real and imaginary parts
    assert result == complex(0.5, 0.7), "The complex number does not have the expected real and imaginary parts"

    # Clean up by stopping the patcher
    mocker.stopall()
