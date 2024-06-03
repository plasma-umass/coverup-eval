# file tornado/log.py:211-258
# lines []
# branches ['219->223', '225->227']

import logging
import pytest
from tornado.log import enable_pretty_logging
from unittest import mock

@pytest.fixture
def mock_options():
    class MockOptions:
        logging = None
        log_file_prefix = None
        log_rotate_mode = None
        log_file_max_size = None
        log_file_num_backups = None
        log_rotate_when = None
        log_rotate_interval = None
        log_to_stderr = None

    return MockOptions()

def test_enable_pretty_logging_no_options(mock_options):
    with mock.patch('tornado.options.options', mock_options):
        enable_pretty_logging()
        assert True  # If no exception is raised, the test passes

def test_enable_pretty_logging_logging_none(mock_options):
    mock_options.logging = "none"
    enable_pretty_logging(options=mock_options)
    assert True  # If no exception is raised, the test passes

def test_enable_pretty_logging_no_logger(mock_options):
    mock_options.logging = "info"
    with mock.patch('tornado.options.options', mock_options):
        enable_pretty_logging()
        logger = logging.getLogger()
        assert logger.level == logging.INFO

@pytest.mark.parametrize("log_level", ["debug", "info", "warning", "error", "critical"])
def test_enable_pretty_logging_various_levels(mock_options, log_level):
    mock_options.logging = log_level
    enable_pretty_logging(options=mock_options)
    logger = logging.getLogger()
    assert logger.level == getattr(logging, log_level.upper())
