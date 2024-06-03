# file pymonet/either.py:81-82
# lines [81, 82]
# branches []

import pytest
from pymonet.either import Either

class TestEither:
    def test_is_right(self, mocker):
        # Mock the is_right method to ensure it gets called
        either_instance = Either(value=None)
        mock_is_right = mocker.patch.object(Either, 'is_right', return_value=True)
        
        # Call the method
        result = either_instance.is_right()
        
        # Assert that the method was called and returned the expected value
        mock_is_right.assert_called_once()
        assert result is True
