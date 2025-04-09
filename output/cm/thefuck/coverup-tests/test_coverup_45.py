# file thefuck/logs.py:43-47
# lines [43, 44, 45, 46, 47]
# branches []

import sys
from unittest.mock import patch
import pytest
from thefuck.logs import failed
from colorama import Fore, Style

@pytest.fixture
def mock_stderr():
    with patch('sys.stderr.write') as mock:
        yield mock

def color(text):
    return text

def test_failed_writes_to_stderr(mock_stderr):
    test_message = "Test error message"
    expected_output = f'{Fore.RED}{test_message}{Style.RESET_ALL}\n'
    
    with patch('thefuck.logs.color', side_effect=color):
        failed(test_message)
    
    mock_stderr.assert_called_once_with(expected_output)
