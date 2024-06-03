# file pytutils/log.py:142-155
# lines [142, 150, 152, 153, 155]
# branches ['152->153', '152->155']

import pytest
import logging
from pytutils.log import get_logger

@pytest.fixture
def mock_ensure_configured(mocker):
    return mocker.patch('pytutils.log._ensure_configured')

@pytest.fixture
def mock_namespace_from_calling_context(mocker):
    return mocker.patch('pytutils.log._namespace_from_calling_context', return_value='mocked_namespace')

def test_get_logger_no_name(mock_ensure_configured, mock_namespace_from_calling_context):
    logger = get_logger()
    assert logger.name == 'mocked_namespace'
    assert mock_ensure_configured.called
    assert mock_namespace_from_calling_context.called

def test_get_logger_with_name(mock_ensure_configured):
    logger_name = 'test_logger'
    logger = get_logger(logger_name)
    assert logger.name == logger_name
    assert mock_ensure_configured.called
