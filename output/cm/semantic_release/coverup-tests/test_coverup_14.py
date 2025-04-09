# file semantic_release/helpers.py:42-77
# lines [42, 43, 52, 53, 55, 56, 57, 59, 60, 61, 62, 63, 64, 70, 73, 74, 75, 77]
# branches ['73->74', '73->75']

import logging
import pytest
from semantic_release.helpers import LoggedFunction

def format_arg(arg):
    return str(arg)

@pytest.fixture
def mock_logger(mocker):
    return mocker.Mock(spec=logging.Logger)

def test_logged_function_with_args_and_result(mock_logger):
    @LoggedFunction(mock_logger)
    def func_with_args_and_result(a, b, c=None):
        return a + b if c is None else a + b + c

    result = func_with_args_and_result(1, 2, c=3)

    assert result == 6
    mock_logger.debug.assert_any_call("func_with_args_and_result(1, 2, c=3)")
    mock_logger.debug.assert_any_call("func_with_args_and_result -> 6")

def test_logged_function_with_no_args_and_no_result(mock_logger):
    @LoggedFunction(mock_logger)
    def func_with_no_args_and_no_result():
        pass

    result = func_with_no_args_and_no_result()

    assert result is None
    mock_logger.debug.assert_called_once_with("func_with_no_args_and_no_result()")
