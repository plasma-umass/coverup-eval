# file thefuck/logs.py:28-36
# lines [29, 30, 31, 32, 33, 34, 35, 36]
# branches []

import pytest
from thefuck.logs import exception
from unittest.mock import patch
import sys
import colorama
from traceback import format_exception


@pytest.fixture
def mock_stderr(mocker):
    return mocker.patch('sys.stderr')


@pytest.fixture
def mock_format_exception(mocker):
    return mocker.patch('thefuck.logs.format_exception', return_value=['Traceback'])


def test_exception_logging(mock_stderr, mock_format_exception):
    exc_type = ValueError
    exc_value = ValueError('An error occurred')
    exc_traceback = None  # Normally you'd use a real traceback, but for this test, it's not necessary

    with patch('sys.stderr.write') as mock_write:
        exception('Test Exception', (exc_type, exc_value, exc_traceback))

    expected_output = (
        u'{warn}[WARN] Test Exception:{reset}\nTraceback'
        u'{warn}----------------------------{reset}\n\n'.format(
            warn=colorama.Back.RED + colorama.Fore.WHITE + colorama.Style.BRIGHT,
            reset=colorama.Style.RESET_ALL
        )
    )

    mock_write.assert_called_once_with(expected_output)
    mock_format_exception.assert_called_once_with(exc_type, exc_value, exc_traceback)
