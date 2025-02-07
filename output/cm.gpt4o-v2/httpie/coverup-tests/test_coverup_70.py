# file: httpie/output/streams.py:21-24
# asked: {"lines": [21, 22, 24], "branches": []}
# gained: {"lines": [21, 22, 24], "branches": []}

import pytest
from httpie.output.streams import BinarySuppressedError, BINARY_SUPPRESSED_NOTICE

def test_binary_suppressed_error_message():
    error = BinarySuppressedError()
    assert error.message == BINARY_SUPPRESSED_NOTICE
