# file: semantic_release/helpers.py:42-77
# asked: {"lines": [42, 43, 52, 53, 55, 56, 57, 59, 60, 61, 62, 63, 64, 70, 73, 74, 75, 77], "branches": [[73, 74], [73, 75]]}
# gained: {"lines": [42, 43, 52, 53, 55, 56, 57, 59, 60, 61, 62, 63, 64, 70, 73, 74, 75, 77], "branches": [[73, 74], [73, 75]]}

import pytest
import logging
from unittest.mock import MagicMock
from semantic_release.helpers import LoggedFunction

def format_arg(arg):
    return repr(arg)

@pytest.fixture
def mock_logger():
    return MagicMock()

def test_logged_function_no_args(mock_logger):
    @LoggedFunction(mock_logger)
    def sample_function():
        return "no args"

    result = sample_function()
    mock_logger.debug.assert_any_call("sample_function()")
    mock_logger.debug.assert_any_call("sample_function -> no args")
    assert result == "no args"

def test_logged_function_with_args(mock_logger):
    @LoggedFunction(mock_logger)
    def sample_function(a, b):
        return a + b

    result = sample_function(1, 2)
    mock_logger.debug.assert_any_call("sample_function(1, 2)")
    mock_logger.debug.assert_any_call("sample_function -> 3")
    assert result == 3

def test_logged_function_with_kwargs(mock_logger):
    @LoggedFunction(mock_logger)
    def sample_function(a, b=2):
        return a + b

    result = sample_function(1, b=3)
    mock_logger.debug.assert_any_call("sample_function(1, b=3)")
    mock_logger.debug.assert_any_call("sample_function -> 4")
    assert result == 4

def test_logged_function_with_args_and_kwargs(mock_logger):
    @LoggedFunction(mock_logger)
    def sample_function(a, b, c=3):
        return a + b + c

    result = sample_function(1, 2, c=4)
    mock_logger.debug.assert_any_call("sample_function(1, 2, c=4)")
    mock_logger.debug.assert_any_call("sample_function -> 7")
    assert result == 7

def test_logged_function_none_result(mock_logger):
    @LoggedFunction(mock_logger)
    def sample_function(a, b):
        pass

    result = sample_function(1, 2)
    mock_logger.debug.assert_any_call("sample_function(1, 2)")
    assert result is None
