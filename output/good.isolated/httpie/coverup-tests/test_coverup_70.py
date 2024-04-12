# file httpie/output/streams.py:17-18
# lines [17, 18]
# branches []

import pytest
from httpie.output.streams import DataSuppressedError

def test_data_suppressed_error_message():
    error_message = "Test error message"
    DataSuppressedError.message = error_message
    try:
        raise DataSuppressedError()
    except DataSuppressedError as e:
        assert e.message == error_message
