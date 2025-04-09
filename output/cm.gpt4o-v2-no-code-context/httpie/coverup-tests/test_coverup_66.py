# file: httpie/output/streams.py:17-18
# asked: {"lines": [17, 18], "branches": []}
# gained: {"lines": [17, 18], "branches": []}

import pytest

from httpie.output.streams import DataSuppressedError

def test_data_suppressed_error():
    # Create an instance of the exception
    exc = DataSuppressedError()

    # Assert that the message attribute is None
    assert exc.message is None

    # Assert that the exception is an instance of DataSuppressedError
    assert isinstance(exc, DataSuppressedError)
