# file: httpie/output/streams.py:17-18
# asked: {"lines": [17, 18], "branches": []}
# gained: {"lines": [17, 18], "branches": []}

import pytest
from httpie.output.streams import DataSuppressedError

def test_data_suppressed_error():
    with pytest.raises(DataSuppressedError) as exc_info:
        raise DataSuppressedError("Test message")
    assert exc_info.value.message is None
    assert str(exc_info.value) == "Test message"
