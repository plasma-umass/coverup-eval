# file pytutils/log.py:142-155
# lines [142, 150, 152, 153, 155]
# branches ['152->153', '152->155']

import logging
import pytest
from unittest.mock import patch
from pytutils.log import get_logger

@pytest.fixture
def logger_cleanup():
    # Fixture to reset the logger to its original state after the test
    original_logging_getLogger = logging.getLogger
    yield
    logging.getLogger = original_logging_getLogger

def test_get_logger_without_name(mocker):
    # Mock the _ensure_configured and _namespace_from_calling_context functions
    ensure_configured_mock = mocker.patch('pytutils.log._ensure_configured')
    namespace_mock = mocker.patch('pytutils.log._namespace_from_calling_context', return_value='mocked_name')

    # Call get_logger without a name to trigger the branch where name is None
    logger = get_logger()

    # Assert that the logger name is the one returned by _namespace_from_calling_context
    assert logger.name == 'mocked_name'
    # Assert that _ensure_configured was called
    ensure_configured_mock.assert_called_once()
    # Assert that _namespace_from_calling_context was called
    namespace_mock.assert_called_once()

def test_get_logger_with_name(mocker):
    # Mock the _ensure_configured function
    ensure_configured_mock = mocker.patch('pytutils.log._ensure_configured')

    # Call get_logger with a specific name
    logger = get_logger('specific_name')

    # Assert that the logger name is the one provided
    assert logger.name == 'specific_name'
    # Assert that _ensure_configured was called
    ensure_configured_mock.assert_called_once()
