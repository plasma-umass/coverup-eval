# file: cookiecutter/log.py:19-51
# asked: {"lines": [19, 26, 27, 31, 34, 35, 36, 37, 38, 39, 42, 43, 46, 47, 48, 49, 51], "branches": [[34, 35], [34, 42]]}
# gained: {"lines": [19, 26, 27, 31, 34, 35, 36, 37, 38, 39, 42, 43, 46, 47, 48, 49, 51], "branches": [[34, 35], [34, 42]]}

import pytest
import logging
import sys
from cookiecutter.log import configure_logger, LOG_FORMATS, LOG_LEVELS

def test_configure_logger_debug_file(tmp_path, monkeypatch):
    debug_file = tmp_path / "debug.log"
    
    # Ensure no handlers are attached before the test
    logger = logging.getLogger('cookiecutter')
    logger.handlers = []
    
    # Configure logger with a debug file
    configure_logger(stream_level='DEBUG', debug_file=str(debug_file))
    
    # Check if file handler is added
    file_handler = next((h for h in logger.handlers if isinstance(h, logging.FileHandler)), None)
    assert file_handler is not None
    assert file_handler.level == LOG_LEVELS['DEBUG']
    assert file_handler.formatter._fmt == LOG_FORMATS['DEBUG']
    
    # Check if stream handler is added
    stream_handler = next((h for h in logger.handlers if isinstance(h, logging.StreamHandler)), None)
    assert stream_handler is not None
    assert stream_handler.level == LOG_LEVELS['DEBUG']
    assert stream_handler.formatter._fmt == LOG_FORMATS['DEBUG']
    
    # Clean up handlers
    logger.handlers = []

def test_configure_logger_no_debug_file(monkeypatch):
    # Ensure no handlers are attached before the test
    logger = logging.getLogger('cookiecutter')
    logger.handlers = []
    
    # Configure logger without a debug file
    configure_logger(stream_level='INFO')
    
    # Check if file handler is not added
    file_handler = next((h for h in logger.handlers if isinstance(h, logging.FileHandler)), None)
    assert file_handler is None
    
    # Check if stream handler is added
    stream_handler = next((h for h in logger.handlers if isinstance(h, logging.StreamHandler)), None)
    assert stream_handler is not None
    assert stream_handler.level == LOG_LEVELS['INFO']
    assert stream_handler.formatter._fmt == LOG_FORMATS['INFO']
    
    # Clean up handlers
    logger.handlers = []
