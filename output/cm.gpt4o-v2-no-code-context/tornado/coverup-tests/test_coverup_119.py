# file: tornado/escape.py:173-175
# asked: {"lines": [173, 174, 175], "branches": []}
# gained: {"lines": [173, 174], "branches": []}

import pytest
from tornado.escape import utf8

def test_utf8_bytes():
    # Test that utf8 function with bytes input returns the same bytes
    input_value = b"test"
    result = utf8(input_value)
    assert result == input_value

# Ensure the test runs and cleans up properly
@pytest.fixture(autouse=True)
def cleanup():
    yield
    # No specific cleanup required for this test
