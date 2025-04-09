# file tornado/log.py:164-208
# lines [200]
# branches ['199->200']

import logging
import pytest
from tornado.log import LogFormatter

def test_log_formatter_exc_info(mocker):
    # Create a logger
    logger = logging.getLogger("test_logger")
    logger.setLevel(logging.DEBUG)

    # Create a stream handler with the custom formatter
    stream_handler = logging.StreamHandler()
    formatter = LogFormatter()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    # Mock the stream to capture the output
    mock_stream = mocker.Mock()
    stream_handler.stream = mock_stream

    # Create an exception to log
    try:
        raise ValueError("Test exception")
    except ValueError:
        logger.exception("Logging an exception")

    # Ensure the exception text was set
    assert mock_stream.write.call_count > 0
    log_output = "".join(call.args[0] for call in mock_stream.write.call_args_list)
    assert "Test exception" in log_output
    assert "Logging an exception" in log_output

    # Clean up by removing the handler
    logger.removeHandler(stream_handler)
