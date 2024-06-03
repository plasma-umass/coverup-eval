# file thefuck/logs.py:43-47
# lines [44, 45, 46, 47]
# branches []

import pytest
import sys
from io import StringIO
from unittest import mock
import colorama
from thefuck.logs import failed

@pytest.fixture
def mock_stderr():
    original_stderr = sys.stderr
    sys.stderr = StringIO()
    yield sys.stderr
    sys.stderr = original_stderr

def test_failed_function(mock_stderr, mocker):
    mock_color = mocker.patch('thefuck.logs.color', side_effect=lambda x: x)
    colorama.init(autoreset=True)
    
    test_message = "This is a test error message"
    with mock.patch('sys.stderr', mock_stderr):
        failed(test_message)
    
    expected_output = f"{colorama.Fore.RED}{test_message}{colorama.Style.RESET_ALL}\n"
    assert mock_stderr.getvalue() == expected_output
    mock_color.assert_any_call(colorama.Fore.RED)
    mock_color.assert_any_call(colorama.Style.RESET_ALL)
