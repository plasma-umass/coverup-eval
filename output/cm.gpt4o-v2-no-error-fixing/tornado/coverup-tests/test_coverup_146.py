# file: tornado/log.py:164-208
# asked: {"lines": [165, 166, 167, 184, 185, 186, 188, 190, 191, 192, 194, 196, 198, 199, 200, 201, 205, 206, 207, 208], "branches": [[190, 191], [190, 194], [198, 199], [198, 201], [199, 200], [199, 201], [201, 205], [201, 208]]}
# gained: {"lines": [165, 166, 167, 184, 185, 186, 188, 190, 191, 192, 194, 196, 198, 199, 201, 205, 206, 207, 208], "branches": [[190, 191], [190, 194], [198, 199], [198, 201], [199, 201], [201, 205], [201, 208]]}

import pytest
import logging
from tornado.log import LogFormatter
from tornado.escape import _unicode

class TestLogFormatter:
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

    @pytest.fixture
    def formatter(self):
        return LogFormatter()

    def test_format_message(self, formatter, log_record):
        formatted = formatter.format(log_record)
        assert "Test message" in formatted

    def test_format_bad_message(self, formatter, log_record, monkeypatch):
        def bad_get_message():
            raise ValueError("Bad message")

        monkeypatch.setattr(log_record, "getMessage", bad_get_message)
        formatted = formatter.format(log_record)
        assert "Bad message" in formatted

    def test_format_with_color(self, formatter, log_record, monkeypatch):
        monkeypatch.setattr(formatter, "_colors", {logging.INFO: "\x1b[32m"})
        formatted = formatter.format(log_record)
        assert "\x1b[32m" in formatted

    def test_format_without_color(self, formatter, log_record, monkeypatch):
        monkeypatch.setattr(formatter, "_colors", {})
        formatted = formatter.format(log_record)
        assert "\x1b[32m" not in formatted

    def test_format_with_exception(self, formatter, log_record):
        try:
            raise ValueError("Test exception")
        except ValueError:
            log_record.exc_info = True
            log_record.exc_text = "Traceback (most recent call last):\nValueError: Test exception"
        formatted = formatter.format(log_record)
        assert "Traceback (most recent call last):" in formatted
        assert "ValueError: Test exception" in formatted

    def test_format_with_multiline_exception(self, formatter, log_record):
        try:
            raise ValueError("Test exception")
        except ValueError:
            log_record.exc_info = True
            log_record.exc_text = "Traceback (most recent call last):\nValueError: Test exception\nAnother line"
        formatted = formatter.format(log_record)
        assert "Traceback (most recent call last):" in formatted
        assert "ValueError: Test exception" in formatted
        assert "Another line" in formatted
