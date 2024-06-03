# file httpie/output/streams.py:21-24
# lines [21, 22, 24]
# branches []

import pytest
from httpie.output.streams import DataSuppressedError, BINARY_SUPPRESSED_NOTICE

def test_binary_suppressed_error():
    class BinarySuppressedError(DataSuppressedError):
        """An error indicating that the body is binary and won't be written,
         e.g., for terminal output)."""
        message = BINARY_SUPPRESSED_NOTICE

    # Instantiate the error and check its message
    error_instance = BinarySuppressedError()
    assert error_instance.message == BINARY_SUPPRESSED_NOTICE
