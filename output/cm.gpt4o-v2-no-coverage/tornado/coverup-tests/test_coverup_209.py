# file: tornado/log.py:164-208
# asked: {"lines": [165, 166, 167, 184, 185, 186, 188, 190, 191, 192, 194, 196, 198, 199, 200, 201, 205, 206, 207, 208], "branches": [[190, 191], [190, 194], [198, 199], [198, 201], [199, 200], [199, 201], [201, 205], [201, 208]]}
# gained: {"lines": [165, 166, 167, 184, 185, 186, 188, 190, 191, 192, 194, 196, 198, 199, 200, 201, 205, 206, 207, 208], "branches": [[190, 191], [190, 194], [198, 199], [198, 201], [199, 200], [201, 205], [201, 208]]}

import pytest
import logging
from tornado.log import LogFormatter
from tornado.escape import _unicode
from typing import Any

def _safe_unicode(s: Any) -> str:
    try:
        return _unicode(s)
    except UnicodeDecodeError:
        return repr(s)

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
    return record

@pytest.fixture
def log_formatter():
    return LogFormatter()

def test_format_message(log_formatter, log_record):
    formatted = log_formatter.format(log_record)
    assert "Test message" in formatted

def test_format_bad_message(log_formatter, log_record, monkeypatch):
    def bad_get_message():
        raise ValueError("Bad message")

    monkeypatch.setattr(log_record, "getMessage", bad_get_message)
    formatted = log_formatter.format(log_record)
    assert "Bad message" in formatted

def test_format_with_exception(log_formatter, log_record):
    try:
        raise ValueError("Test exception")
    except ValueError:
        log_record.exc_info = logging.sys.exc_info()

    formatted = log_formatter.format(log_record)
    assert "Test exception" in formatted
    assert "ValueError" in formatted

def test_format_with_colors(log_formatter, log_record, monkeypatch):
    monkeypatch.setattr(log_formatter, "_colors", {logging.INFO: "\x1b[32m"})
    formatted = log_formatter.format(log_record)
    assert "\x1b[32m" in formatted

def test_format_without_colors(log_formatter, log_record, monkeypatch):
    monkeypatch.setattr(log_formatter, "_colors", {})
    formatted = log_formatter.format(log_record)
    assert "\x1b[32m" not in formatted
