# file: pytutils/log.py:142-155
# asked: {"lines": [142, 150, 152, 153, 155], "branches": [[152, 153], [152, 155]]}
# gained: {"lines": [142, 150, 152, 153, 155], "branches": [[152, 153], [152, 155]]}

import pytest
import logging
from unittest import mock

from pytutils.log import get_logger

@pytest.fixture
def reset_logging_config():
    logging.getLogger().handlers = []
    logging.getLogger().setLevel(logging.NOTSET)
    yield
    logging.getLogger().handlers = []
    logging.getLogger().setLevel(logging.NOTSET)

def test_get_logger_no_name(monkeypatch, reset_logging_config):
    with mock.patch('pytutils.log._ensure_configured') as mock_ensure_configured, \
         mock.patch('pytutils.log._namespace_from_calling_context', return_value='test_namespace') as mock_namespace:
        
        logger = get_logger()
        
        mock_ensure_configured.assert_called_once()
        mock_namespace.assert_called_once()
        assert logger.name == 'test_namespace'

def test_get_logger_with_name(monkeypatch, reset_logging_config):
    with mock.patch('pytutils.log._ensure_configured') as mock_ensure_configured:
        
        logger = get_logger('test_logger')
        
        mock_ensure_configured.assert_called_once()
        assert logger.name == 'test_logger'
