# file pymonet/either.py:22-35
# lines [22, 33, 34, 35]
# branches ['33->34', '33->35']

import pytest
from unittest.mock import Mock

# Assuming the Either class is defined in pymonet.either
from pymonet.either import Either

class TestEither:
    def test_case_method(self):
        # Mock the Either class to create instances of Left and Right
        left_instance = Mock(spec=Either)
        right_instance = Mock(spec=Either)

        # Set up the mock to return specific values for is_right and value
        left_instance.is_right.return_value = False
        left_instance.value = 'left_value'
        right_instance.is_right.return_value = True
        right_instance.value = 'right_value'

        # Define the error and success functions
        def error_fn(value):
            return f"Error: {value}"

        def success_fn(value):
            return f"Success: {value}"

        # Test the case method for the Left instance
        result_left = Either.case(left_instance, error_fn, success_fn)
        assert result_left == "Error: left_value"

        # Test the case method for the Right instance
        result_right = Either.case(right_instance, error_fn, success_fn)
        assert result_right == "Success: right_value"
