# file tornado/log.py:81-115
# lines [81, 82, 106, 107, 108, 109, 110, 111, 112, 113]
# branches []

import logging
import pytest
from tornado.log import LogFormatter

@pytest.fixture
def logger():
    logger = logging.getLogger('tornado.test')
    logger.propagate = False
    return logger

@pytest.fixture
def stream_handler(mocker, logger):
    stream = mocker.MagicMock()
    handler = logging.StreamHandler(stream)
    logger.addHandler(handler)
    yield handler, stream
    logger.removeHandler(handler)

def test_log_formatter_with_color(logger, stream_handler, mocker):
    handler, stream = stream_handler
    mocker.patch('sys.stderr.isatty', return_value=True)
    formatter = LogFormatter()
    handler.setFormatter(formatter)
    logger.setLevel(logging.DEBUG)
    logger.error("test message with color")
    stream.write.assert_called()
    args, _ = stream.write.call_args
    assert "\x1b[31m" in args[0]  # Red color code for ERROR level

def test_log_formatter_without_color(logger, stream_handler, mocker):
    handler, stream = stream_handler
    mocker.patch('sys.stderr.isatty', return_value=False)
    formatter = LogFormatter()
    handler.setFormatter(formatter)
    logger.setLevel(logging.DEBUG)
    logger.error("test message without color")
    stream.write.assert_called()
    args, _ = stream.write.call_args
    assert "\x1b[31m" not in args[0]  # No color code should be present
