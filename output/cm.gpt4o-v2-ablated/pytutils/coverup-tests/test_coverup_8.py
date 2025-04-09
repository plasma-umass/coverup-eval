# file: pytutils/log.py:142-155
# asked: {"lines": [142, 150, 152, 153, 155], "branches": [[152, 153], [152, 155]]}
# gained: {"lines": [142, 150, 152, 153, 155], "branches": [[152, 153], [152, 155]]}

import pytest
import logging
from unittest import mock
from pytutils.log import get_logger

@pytest.fixture(autouse=True)
def reset_logging():
    logging.shutdown()
    import importlib
    importlib.reload(logging)

def test_get_logger_no_name(monkeypatch):
    mock_ensure_configured = mock.Mock()
    monkeypatch.setattr('pytutils.log._ensure_configured', mock_ensure_configured)
    
    mock_namespace = 'mock_namespace'
    monkeypatch.setattr('pytutils.log._namespace_from_calling_context', lambda: mock_namespace)
    
    logger = get_logger()
    
    mock_ensure_configured.assert_called_once()
    assert logger.name == mock_namespace

def test_get_logger_with_name(monkeypatch):
    mock_ensure_configured = mock.Mock()
    monkeypatch.setattr('pytutils.log._ensure_configured', mock_ensure_configured)
    
    logger_name = 'test_logger'
    logger = get_logger(logger_name)
    
    mock_ensure_configured.assert_called_once()
    assert logger.name == logger_name
