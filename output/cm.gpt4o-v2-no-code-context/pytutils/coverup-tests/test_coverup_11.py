# file: pytutils/log.py:142-155
# asked: {"lines": [142, 150, 152, 153, 155], "branches": [[152, 153], [152, 155]]}
# gained: {"lines": [142, 150, 152, 153, 155], "branches": [[152, 153], [152, 155]]}

import pytest
import logging
from pytutils.log import get_logger, _ensure_configured, _namespace_from_calling_context

@pytest.fixture(autouse=True)
def setup_and_teardown(monkeypatch):
    # Setup: Ensure the logger is configured and mock necessary functions
    monkeypatch.setattr('pytutils.log._ensure_configured', lambda: None)
    monkeypatch.setattr('pytutils.log._namespace_from_calling_context', lambda: 'default_namespace')
    yield
    # Teardown: Reset logging configuration
    logging.shutdown()
    import importlib
    importlib.reload(logging)

def test_get_logger_no_name():
    logger = get_logger()
    assert logger.name == 'default_namespace'
    assert isinstance(logger, logging.Logger)

def test_get_logger_with_name():
    logger_name = 'test_logger'
    logger = get_logger(logger_name)
    assert logger.name == logger_name
    assert isinstance(logger, logging.Logger)
