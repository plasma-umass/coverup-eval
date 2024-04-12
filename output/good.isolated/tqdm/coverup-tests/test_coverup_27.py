# file tqdm/contrib/logging.py:48-98
# lines [90, 91]
# branches ['89->90']

import logging
import pytest
from tqdm.contrib.logging import logging_redirect_tqdm

@pytest.fixture
def logger_with_stream_handler():
    logger = logging.getLogger('test.tqdm')
    stream_handler = logging.StreamHandler()
    formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    yield logger
    logger.removeHandler(stream_handler)

def test_logging_redirect_tqdm_with_formatter_and_stream(logger_with_stream_handler, mocker):
    # Mock the _get_first_found_console_logging_handler to return our stream_handler
    mocker.patch(
        'tqdm.contrib.logging._get_first_found_console_logging_handler',
        return_value=logger_with_stream_handler.handlers[0]
    )

    # Use the context manager and check if the formatter and stream are set
    with logging_redirect_tqdm(loggers=[logger_with_stream_handler]):
        tqdm_handler = logger_with_stream_handler.handlers[-1]
        assert tqdm_handler.formatter == logger_with_stream_handler.handlers[0].formatter
        assert tqdm_handler.stream == logger_with_stream_handler.handlers[0].stream
