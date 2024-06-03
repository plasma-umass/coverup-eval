# file tornado/log.py:164-208
# lines [164, 165, 166, 167, 184, 185, 186, 188, 190, 191, 192, 194, 196, 198, 199, 200, 201, 205, 206, 207, 208]
# branches ['190->191', '190->194', '198->199', '198->201', '199->200', '199->201', '201->205', '201->208']

import logging
import pytest
from tornado.log import LogFormatter

def _safe_unicode(s):
    try:
        return str(s)
    except UnicodeDecodeError:
        return repr(s)

@pytest.fixture
def mock_record(mocker):
    record = logging.LogRecord(
        name="test",
        level=logging.INFO,
        pathname="test_path",
        lineno=10,
        msg="Test message",
        args=(),
        exc_info=None
    )
    return record

def test_log_formatter_format(mock_record, mocker):
    formatter = LogFormatter()
    mocker.patch.object(formatter, '_colors', {logging.INFO: '\033[32m'})
    mocker.patch.object(formatter, '_normal', '\033[0m')
    mocker.patch.object(formatter, '_fmt', '%(color)s%(message)s%(end_color)s')

    formatted_message = formatter.format(mock_record)

    assert formatted_message == '\033[32mTest message\033[0m'

def test_log_formatter_format_with_exception(mock_record, mocker):
    formatter = LogFormatter()
    mocker.patch.object(formatter, '_colors', {logging.ERROR: '\033[31m'})
    mocker.patch.object(formatter, '_normal', '\033[0m')
    mocker.patch.object(formatter, '_fmt', '%(color)s%(message)s%(end_color)s')

    mock_record.levelno = logging.ERROR
    mock_record.exc_info = (None, Exception("Test exception"), None)
    mock_record.exc_text = "Traceback (most recent call last):\nException: Test exception"

    formatted_message = formatter.format(mock_record)

    assert '\033[31mTest message\033[0m' in formatted_message
    assert 'Traceback (most recent call last):' in formatted_message
    assert 'Exception: Test exception' in formatted_message

def test_log_formatter_format_with_bad_message(mocker):
    formatter = LogFormatter()
    mocker.patch.object(formatter, '_colors', {logging.INFO: '\033[32m'})
    mocker.patch.object(formatter, '_normal', '\033[0m')
    mocker.patch.object(formatter, '_fmt', '%(color)s%(message)s%(end_color)s')

    bad_record = logging.LogRecord(
        name="test",
        level=logging.INFO,
        pathname="test_path",
        lineno=10,
        msg="Test message",
        args=(),
        exc_info=None
    )
    mocker.patch.object(bad_record, 'getMessage', side_effect=Exception("Bad message"))

    formatted_message = formatter.format(bad_record)

    assert "Bad message" in formatted_message
    assert "Bad message" in bad_record.message
