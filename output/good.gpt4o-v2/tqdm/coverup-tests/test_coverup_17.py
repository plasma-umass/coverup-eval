# file: tqdm/contrib/logging.py:48-98
# asked: {"lines": [48, 49, 50, 51, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 97, 98], "branches": [[82, 83], [82, 84], [86, 87], [86, 95], [89, 90], [89, 92], [97, 0], [97, 98]]}
# gained: {"lines": [48, 49, 50, 51, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 97, 98], "branches": [[82, 83], [82, 84], [86, 87], [86, 95], [89, 90], [89, 92], [97, 0], [97, 98]]}

import logging
import pytest
from tqdm.contrib.logging import logging_redirect_tqdm
from tqdm.std import tqdm as std_tqdm

def test_logging_redirect_tqdm_default_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    stream_handler = logging.StreamHandler()
    logger.addHandler(stream_handler)

    with logging_redirect_tqdm():
        logger.info("Test message")

    assert any(isinstance(handler, logging.StreamHandler) for handler in logger.handlers)
    logger.handlers.clear()

def test_logging_redirect_tqdm_custom_logger():
    custom_logger = logging.getLogger("custom_logger")
    custom_logger.setLevel(logging.INFO)
    stream_handler = logging.StreamHandler()
    custom_logger.addHandler(stream_handler)

    with logging_redirect_tqdm(loggers=[custom_logger]):
        custom_logger.info("Test message")

    assert any(isinstance(handler, logging.StreamHandler) for handler in custom_logger.handlers)
    custom_logger.handlers.clear()

def test_logging_redirect_tqdm_no_console_handler():
    custom_logger = logging.getLogger("custom_logger_no_console")
    custom_logger.setLevel(logging.INFO)

    with logging_redirect_tqdm(loggers=[custom_logger]):
        custom_logger.info("Test message")

    assert len(custom_logger.handlers) == 0
    custom_logger.handlers.clear()

def test_logging_redirect_tqdm_with_formatter():
    custom_logger = logging.getLogger("custom_logger_with_formatter")
    custom_logger.setLevel(logging.INFO)
    stream_handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    stream_handler.setFormatter(formatter)
    custom_logger.addHandler(stream_handler)

    with logging_redirect_tqdm(loggers=[custom_logger]):
        custom_logger.info("Test message")

    assert any(handler.formatter == formatter for handler in custom_logger.handlers)
    custom_logger.handlers.clear()
