# file: tornado/log.py:164-208
# asked: {"lines": [164, 165, 166, 167, 184, 185, 186, 188, 190, 191, 192, 194, 196, 198, 199, 200, 201, 205, 206, 207, 208], "branches": [[190, 191], [190, 194], [198, 199], [198, 201], [199, 200], [199, 201], [201, 205], [201, 208]]}
# gained: {"lines": [164, 165, 166, 167, 184, 185, 186, 188, 190, 191, 192, 194, 196, 198, 199, 200, 201, 205, 206, 207, 208], "branches": [[190, 191], [190, 194], [198, 199], [198, 201], [199, 200], [201, 205], [201, 208]]}

import logging
import pytest
from tornado.log import LogFormatter
from tornado.escape import _unicode

class TestLogFormatter:
    @pytest.fixture
    def log_formatter(self):
        return LogFormatter()

    @pytest.fixture
    def log_record(self):
        record = logging.LogRecord(
            name="test",
            level=logging.INFO,
            pathname=__file__,
            lineno=10,
            msg="Test message",
            args=(),
            exc_info=None,
        )
        return record

    def test_format_basic_message(self, log_formatter, log_record):
        formatted = log_formatter.format(log_record)
        assert "Test message" in formatted

    def test_format_with_non_ascii_bytestring(self, log_formatter, log_record):
        log_record.msg = b"Test message with non-ascii \xe2\x98\x83"
        formatted = log_formatter.format(log_record)
        assert "Test message with non-ascii" in formatted

    def test_format_with_exception(self, log_formatter, log_record):
        try:
            raise ValueError("Test exception")
        except ValueError:
            log_record.exc_info = True
            log_record.exc_info = logging.sys.exc_info()
        formatted = log_formatter.format(log_record)
        assert "Test exception" in formatted

    def test_format_with_custom_time_format(self, log_formatter, log_record, monkeypatch):
        monkeypatch.setattr(log_formatter, 'datefmt', "%Y-%m-%d %H:%M:%S")
        formatted = log_formatter.format(log_record)
        assert "Test message" in formatted

    def test_format_with_color(self, log_formatter, log_record, monkeypatch):
        monkeypatch.setattr(log_formatter, '_colors', {logging.INFO: '\033[1;32m'})
        monkeypatch.setattr(log_formatter, '_normal', '\033[0m')
        formatted = log_formatter.format(log_record)
        assert '\033[1;32m' in formatted
        assert '\033[0m' in formatted

    def test_format_with_bad_message(self, log_formatter, log_record, monkeypatch):
        def bad_get_message():
            raise ValueError("Bad message")
        monkeypatch.setattr(log_record, 'getMessage', bad_get_message)
        formatted = log_formatter.format(log_record)
        assert "Bad message" in formatted
