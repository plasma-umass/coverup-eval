# file: semantic_release/helpers.py:42-77
# asked: {"lines": [42, 43, 52, 53, 55, 56, 57, 59, 60, 61, 62, 63, 64, 70, 73, 74, 75, 77], "branches": [[73, 74], [73, 75]]}
# gained: {"lines": [42, 43, 52, 53, 55, 56, 57, 59, 60, 61, 62, 63, 64, 70, 73, 74, 75, 77], "branches": [[73, 74], [73, 75]]}

import pytest
import logging
from semantic_release.helpers import LoggedFunction

def format_arg(arg):
    return repr(arg)

@pytest.fixture
def logger():
    logger = logging.getLogger('test_logger')
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    return logger

def test_logged_function_decorator(logger, caplog):
    @LoggedFunction(logger)
    def sample_function(x, y=2):
        return x + y

    with caplog.at_level(logging.DEBUG):
        result = sample_function(3, y=4)
        assert result == 7

    assert "sample_function(3, y=4)" in caplog.text
    assert "sample_function -> 7" in caplog.text

def test_logged_function_decorator_no_result(logger, caplog):
    @LoggedFunction(logger)
    def sample_function(x, y=2):
        pass

    with caplog.at_level(logging.DEBUG):
        result = sample_function(3, y=4)
        assert result is None

    assert "sample_function(3, y=4)" in caplog.text
    assert "sample_function ->" not in caplog.text
