# file: httpie/output/streams.py:17-18
# asked: {"lines": [17, 18], "branches": []}
# gained: {"lines": [17, 18], "branches": []}

import pytest

from httpie.output.streams import DataSuppressedError

def test_data_suppressed_error_message():
    # Test that the message attribute is None by default
    error = DataSuppressedError()
    assert error.message is None

    # Test that the exception can be raised and caught
    with pytest.raises(DataSuppressedError):
        raise DataSuppressedError()

    # Test that the message attribute can be set
    error.message = "Test message"
    assert error.message == "Test message"
