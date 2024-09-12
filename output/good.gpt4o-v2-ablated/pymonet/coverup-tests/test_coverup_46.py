# file: pymonet/either.py:138-147
# asked: {"lines": [138, 145, 147], "branches": []}
# gained: {"lines": [138, 145, 147], "branches": []}

import pytest
from pymonet.either import Either

class TestLeft:
    def test_to_validation(self, mocker):
        from pymonet.validation import Validation
        from pymonet.either import Left

        # Mock the Validation.fail method
        mock_fail = mocker.patch.object(Validation, 'fail', return_value='mocked_fail')

        # Create a Left instance
        left_instance = Left('error_value')

        # Call the to_validation method
        result = left_instance.to_validation()

        # Assert that Validation.fail was called with the correct argument
        mock_fail.assert_called_once_with(['error_value'])

        # Assert that the result is the mocked return value
        assert result == 'mocked_fail'
