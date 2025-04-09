# file tqdm/contrib/logging.py:48-98
# lines [82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 97, 98]
# branches ['82->83', '82->84', '86->87', '86->95', '89->90', '89->92', '97->exit', '97->98']

import logging
import pytest
from tqdm import trange
from tqdm.contrib.logging import logging_redirect_tqdm

class _TqdmLoggingHandler(logging.Handler):
    def __init__(self, tqdm_class):
        super().__init__()
        self.tqdm_class = tqdm_class

    def emit(self, record):
        try:
            msg = self.format(record)
            self.tqdm_class.write(msg)
        except Exception:
            self.handleError(record)

def _get_first_found_console_logging_handler(handlers):
    for handler in handlers:
        if _is_console_logging_handler(handler):
            return handler
    return None

def _is_console_logging_handler(handler):
    return isinstance(handler, logging.StreamHandler) and handler.stream in {sys.stdout, sys.stderr}

@pytest.fixture
def mock_tqdm_class(mocker):
    return mocker.patch('tqdm.contrib.logging.std_tqdm')

def test_logging_redirect_tqdm(mock_tqdm_class):
    logger = logging.getLogger('test_logger')
    logger.setLevel(logging.INFO)
    stream_handler = logging.StreamHandler()
    logger.addHandler(stream_handler)

    with logging_redirect_tqdm([logger], tqdm_class=mock_tqdm_class):
        logger.info("Test message")
        assert any("Test message" in call.args[0] for call in mock_tqdm_class.write.call_args_list)

    # Ensure handlers are restored
    assert logger.handlers == [stream_handler]

    # Clean up
    logger.removeHandler(stream_handler)
    mock_tqdm_class.reset_mock()
