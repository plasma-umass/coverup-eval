# file: httpie/output/streams.py:17-18
# asked: {"lines": [17, 18], "branches": []}
# gained: {"lines": [17, 18], "branches": []}

import pytest
from httpie.output.streams import DataSuppressedError

def test_data_suppressed_error_message():
    # Ensure the message attribute is None
    assert DataSuppressedError.message is None

    # Ensure the exception can be raised and caught
    with pytest.raises(DataSuppressedError) as exc_info:
        raise DataSuppressedError("Test message")
    
    # Ensure the exception message is as expected
    assert str(exc_info.value) == "Test message"
