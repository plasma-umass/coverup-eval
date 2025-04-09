# file tornado/log.py:81-115
# lines [81, 82, 106, 107, 108, 109, 110, 111, 112, 113]
# branches []

import logging
import pytest
from tornado.log import LogFormatter

@pytest.fixture
def mock_colorama(mocker):
    colorama = mocker.patch("tornado.log.colorama", create=True)
    colorama.init = mocker.Mock()
    return colorama

def test_log_formatter_with_colorama(mock_colorama):
    # Simulate a terminal that supports color
    mock_colorama.Fore = mock_colorama.Back = mock_colorama.Style = mock_colorama
    mock_colorama.Fore.RESET = ''
    mock_colorama.Back.RESET = ''
    mock_colorama.Style.RESET_ALL = ''

    # Initialize the LogFormatter
    formatter = LogFormatter()

    # Manually call colorama.init to simulate the environment setup
    mock_colorama.init()

    # Create a log record
    record = logging.LogRecord(
        name="test",
        level=logging.INFO,
        pathname=__file__,
        lineno=10,
        msg="Test message",
        args=(),
        exc_info=None
    )

    # Format the log record
    formatted_message = formatter.format(record)

    # Check if the formatted message contains the expected parts
    assert "[I " in formatted_message
    assert "Test message" in formatted_message

    # Ensure colorama.init was called
    mock_colorama.init.assert_called_once()

def test_log_formatter_without_colorama(mocker):
    # Remove colorama to simulate environment without it
    mocker.patch("tornado.log.colorama", None)

    # Initialize the LogFormatter
    formatter = LogFormatter()

    # Create a log record
    record = logging.LogRecord(
        name="test",
        level=logging.INFO,
        pathname=__file__,
        lineno=10,
        msg="Test message",
        args=(),
        exc_info=None
    )

    # Format the log record
    formatted_message = formatter.format(record)

    # Check if the formatted message contains the expected parts
    assert "[I " in formatted_message
    assert "Test message" in formatted_message
