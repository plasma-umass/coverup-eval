# file: tornado/log.py:164-208
# asked: {"lines": [200], "branches": [[199, 200]]}
# gained: {"lines": [200], "branches": [[199, 200]]}

import logging
import pytest
from tornado.log import LogFormatter
from unittest.mock import Mock

def _safe_unicode(s):
    try:
        return str(s)
    except UnicodeDecodeError:
        return repr(s)

@pytest.fixture
def log_record():
    record = logging.LogRecord(
        name="test",
        level=logging.ERROR,
        pathname=__file__,
        lineno=10,
        msg="Test message",
        args=(),
        exc_info=(None, None, None)
    )
    return record

def test_format_with_exception(log_record, monkeypatch):
    formatter = LogFormatter()
    log_record.exc_info = (Exception, Exception("Test exception"), None)
    log_record.exc_text = None

    monkeypatch.setattr("tornado.log._safe_unicode", _safe_unicode)
    formatted_message = formatter.format(log_record)

    assert "Test exception" in formatted_message
    assert "Bad message" not in formatted_message

def test_format_without_exception(log_record, monkeypatch):
    formatter = LogFormatter()
    log_record.exc_info = None
    log_record.exc_text = None

    monkeypatch.setattr("tornado.log._safe_unicode", _safe_unicode)
    formatted_message = formatter.format(log_record)

    assert "Test message" in formatted_message
    assert "Bad message" not in formatted_message
