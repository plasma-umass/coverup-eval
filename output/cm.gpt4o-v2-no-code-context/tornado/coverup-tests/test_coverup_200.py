# file: tornado/log.py:164-208
# asked: {"lines": [], "branches": [[199, 201]]}
# gained: {"lines": [], "branches": [[199, 201]]}

import logging
import pytest
from tornado.log import LogFormatter

def test_log_formatter_with_exception_text(monkeypatch):
    # Create a logger and a log record with exc_info
    logger = logging.getLogger("test_logger")
    formatter = LogFormatter()

    # Mock the _safe_unicode function to return the input as is
    def mock_safe_unicode(s):
        return s

    monkeypatch.setattr("tornado.log._safe_unicode", mock_safe_unicode)

    try:
        1 / 0
    except ZeroDivisionError as e:
        record = logger.makeRecord(
            name="test_logger",
            level=logging.ERROR,
            fn="test_log_formatter_with_exception_text",
            lno=10,
            msg="An error occurred",
            args=(),
            exc_info=(type(e), e, e.__traceback__),
        )

    # Ensure exc_text is None initially
    assert record.exc_text is None

    formatted_message = formatter.format(record)

    # Ensure exc_text is now populated
    assert record.exc_text is not None
    assert "ZeroDivisionError" in record.exc_text

    # Ensure the formatted message contains the exception text
    assert "An error occurred" in formatted_message
    assert "ZeroDivisionError" in formatted_message

def test_log_formatter_with_preexisting_exc_text(monkeypatch):
    # Create a logger and a log record with exc_info and preexisting exc_text
    logger = logging.getLogger("test_logger")
    formatter = LogFormatter()

    # Mock the _safe_unicode function to return the input as is
    def mock_safe_unicode(s):
        return s

    monkeypatch.setattr("tornado.log._safe_unicode", mock_safe_unicode)

    try:
        1 / 0
    except ZeroDivisionError as e:
        record = logger.makeRecord(
            name="test_logger",
            level=logging.ERROR,
            fn="test_log_formatter_with_preexisting_exc_text",
            lno=10,
            msg="An error occurred",
            args=(),
            exc_info=(type(e), e, e.__traceback__),
        )
        record.exc_text = "Preexisting exception text"

    # Ensure exc_text is not None initially
    assert record.exc_text is not None

    formatted_message = formatter.format(record)

    # Ensure the formatted message contains the preexisting exception text
    assert "An error occurred" in formatted_message
    assert "Preexisting exception text" in formatted_message

def test_log_formatter_without_exception_text(monkeypatch):
    # Create a logger and a log record without exc_info
    logger = logging.getLogger("test_logger")
    formatter = LogFormatter()

    # Mock the _safe_unicode function to return the input as is
    def mock_safe_unicode(s):
        return s

    monkeypatch.setattr("tornado.log._safe_unicode", mock_safe_unicode)

    record = logger.makeRecord(
        name="test_logger",
        level=logging.INFO,
        fn="test_log_formatter_without_exception_text",
        lno=20,
        msg="A simple log message",
        args=(),
        exc_info=None,
    )

    formatted_message = formatter.format(record)

    # Ensure exc_text is None
    assert record.exc_text is None

    # Ensure the formatted message does not contain exception text
    assert "A simple log message" in formatted_message
    assert "ZeroDivisionError" not in formatted_message
