# file: httpie/output/streams.py:17-18
# asked: {"lines": [17, 18], "branches": []}
# gained: {"lines": [17, 18], "branches": []}

import pytest

from httpie.output.streams import DataSuppressedError

def test_data_suppressed_error_message():
    error = DataSuppressedError()
    assert error.message is None
