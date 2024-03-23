# file typesystem/base.py:190-192
# lines [190, 191, 192]
# branches []

import pytest
from typesystem.base import BaseError

class TestBaseError:
    def test_base_error_hash(self):
        # Create a subclass of BaseError to test the __hash__ method
        class MyError(BaseError):
            def __init__(self, messages):
                self._messages = messages

        # Instantiate the subclass with a list of messages
        error_instance = MyError(messages=["Error 1", "Error 2"])

        # Calculate the hash of the error instance
        error_hash = hash(error_instance)

        # Assert that the hash is an integer (as __hash__ should return an int)
        assert isinstance(error_hash, int)

        # Assert that the hash is consistent for the same object
        assert hash(error_instance) == error_hash

        # Create another instance with the same messages to test that they hash the same
        same_error_instance = MyError(messages=["Error 1", "Error 2"])
        assert hash(same_error_instance) == error_hash

        # Create another instance with different messages to test that they hash differently
        different_error_instance = MyError(messages=["Error 3"])
        assert hash(different_error_instance) != error_hash
