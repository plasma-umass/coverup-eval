# file: tqdm/contrib/logging.py:101-128
# asked: {"lines": [123, 124, 125, 126, 127, 128], "branches": []}
# gained: {"lines": [123, 124, 125, 126, 127, 128], "branches": []}

import pytest
import logging
from tqdm import trange
from tqdm.contrib.logging import tqdm_logging_redirect

LOG = logging.getLogger(__name__)

def test_tqdm_logging_redirect_default(monkeypatch):
    # Setup
    log_output = []

    def mock_info(msg):
        log_output.append(msg)

    monkeypatch.setattr(LOG, "info", mock_info)

    # Test
    with tqdm_logging_redirect(total=5) as pbar:
        for i in range(5):
            pbar.update(1)
            if i == 2:
                LOG.info("Test log message")

    # Assert
    assert log_output == ["Test log message"]

def test_tqdm_logging_redirect_custom_logger(monkeypatch):
    # Setup
    custom_logger = logging.getLogger("custom_logger")
    log_output = []

    def mock_info(msg):
        log_output.append(msg)

    monkeypatch.setattr(custom_logger, "info", mock_info)

    # Test
    with tqdm_logging_redirect(total=5, loggers=[custom_logger]) as pbar:
        for i in range(5):
            pbar.update(1)
            if i == 2:
                custom_logger.info("Custom logger message")

    # Assert
    assert log_output == ["Custom logger message"]

def test_tqdm_logging_redirect_custom_tqdm_class(monkeypatch):
    from tqdm import tqdm

    # Setup
    log_output = []

    def mock_info(msg):
        log_output.append(msg)

    monkeypatch.setattr(LOG, "info", mock_info)

    # Test
    with tqdm_logging_redirect(total=5, tqdm_class=tqdm) as pbar:
        for i in range(5):
            pbar.update(1)
            if i == 2:
                LOG.info("Test log message with custom tqdm")

    # Assert
    assert log_output == ["Test log message with custom tqdm"]
