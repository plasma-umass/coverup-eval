# file: tqdm/contrib/logging.py:18-34
# asked: {"lines": [32], "branches": []}
# gained: {"lines": [32], "branches": []}

import logging
import pytest
from tqdm.contrib.logging import _TqdmLoggingHandler
from tqdm.std import tqdm as std_tqdm

class CustomException(Exception):
    pass

def test_emit_handles_keyboard_interrupt(mocker):
    logger = logging.getLogger('test_logger')
    logger.setLevel(logging.DEBUG)
    tqdm_handler = _TqdmLoggingHandler()
    logger.addHandler(tqdm_handler)

    mocker.patch.object(tqdm_handler, 'format', side_effect=KeyboardInterrupt)

    with pytest.raises(KeyboardInterrupt):
        logger.debug('This should raise KeyboardInterrupt')

def test_emit_handles_system_exit(mocker):
    logger = logging.getLogger('test_logger')
    logger.setLevel(logging.DEBUG)
    tqdm_handler = _TqdmLoggingHandler()
    logger.addHandler(tqdm_handler)

    mocker.patch.object(tqdm_handler, 'format', side_effect=SystemExit)

    with pytest.raises(SystemExit):
        logger.debug('This should raise SystemExit')

def test_emit_handles_generic_exception(mocker):
    logger = logging.getLogger('test_logger')
    logger.setLevel(logging.DEBUG)
    tqdm_handler = _TqdmLoggingHandler()
    logger.addHandler(tqdm_handler)

    mock_handle_error = mocker.patch.object(tqdm_handler, 'handleError')
    mocker.patch.object(tqdm_handler, 'format', side_effect=CustomException)

    logger.debug('This should be handled as a generic exception')

    mock_handle_error.assert_called_once()
