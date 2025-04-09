# file tornado/log.py:164-208
# lines [164, 165, 166, 167, 184, 185, 186, 188, 190, 191, 192, 194, 196, 198, 199, 200, 201, 205, 206, 207, 208]
# branches ['190->191', '190->194', '198->199', '198->201', '199->200', '199->201', '201->205', '201->208']

import logging
import pytest
from tornado.log import LogFormatter

# Define a helper function to simulate a byte string message
def _simulate_byte_string_message(record, message):
    record.msg = message
    record.args = None
    return record

# Define a helper function to simulate an exception in getMessage
def _simulate_exception_in_getMessage(record, side_effect):
    record.getMessage = lambda: (_ for _ in ()).throw(side_effect)
    return record

# Define the test function for the LogFormatter
@pytest.fixture
def log_record():
    record = logging.LogRecord(
        name="test",
        level=logging.INFO,
        pathname=__file__,
        lineno=10,
        msg="Test message",
        args=(),
        exc_info=None,
    )
    yield record

@pytest.fixture
def log_formatter():
    formatter = LogFormatter()
    yield formatter

def test_log_formatter_with_byte_string_message(log_record, log_formatter):
    byte_string_message = b'Test byte string message'
    record = _simulate_byte_string_message(log_record, byte_string_message)
    formatted = log_formatter.format(record)
    assert isinstance(formatted, str)
    assert "Test byte string message" in formatted

def test_log_formatter_with_exception_in_getMessage(log_record, log_formatter):
    record = _simulate_exception_in_getMessage(log_record, ValueError("Simulated exception"))
    formatted = log_formatter.format(record)
    assert "Bad message" in formatted
    assert "Simulated exception" in formatted
