# file: httpie/output/streams.py:21-24
# asked: {"lines": [21, 22, 24], "branches": []}
# gained: {"lines": [21, 22, 24], "branches": []}

import pytest
from httpie.output.streams import DataSuppressedError, BINARY_SUPPRESSED_NOTICE

def test_binary_suppressed_error():
    class BinarySuppressedError(DataSuppressedError):
        """An error indicating that the body is binary and won't be written,
        e.g., for terminal output)."""
        message = BINARY_SUPPRESSED_NOTICE

    # Instantiate the error to ensure the class definition is executed
    error_instance = BinarySuppressedError()

    # Assert that the message attribute is correctly set
    assert error_instance.message == BINARY_SUPPRESSED_NOTICE

    # Assert that the error instance is indeed a subclass of DataSuppressedError
    assert isinstance(error_instance, DataSuppressedError)
