# file typesystem/base.py:190-192
# lines [190, 191, 192]
# branches []

import pytest
from typesystem.base import BaseError

class MockError(BaseError):
    def __init__(self, messages):
        self._messages = messages

def test_base_error_hash():
    error1 = MockError(messages=["Error 1", "Error 2"])
    error2 = MockError(messages=["Error 1", "Error 2"])
    error3 = MockError(messages=["Error 3"])

    # Assert that the hash is consistent for the same content
    assert hash(error1) == hash(error2), "Hashes should be equal for the same error messages"

    # Assert that the hash is different for different content
    assert hash(error1) != hash(error3), "Hashes should be different for different error messages"

    # Clean up if necessary (not needed in this case as no external resources are used)
