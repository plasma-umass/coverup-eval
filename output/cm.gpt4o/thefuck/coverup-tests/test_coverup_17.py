# file thefuck/logs.py:28-36
# lines [28, 29, 30, 31, 32, 33, 34, 35, 36]
# branches []

import sys
import colorama
from thefuck.logs import exception
import pytest
from unittest.mock import patch
from traceback import format_exception

@pytest.fixture(autouse=True)
def setup_and_teardown():
    colorama.init()
    yield
    colorama.deinit()

def test_exception(mocker):
    mock_stderr = mocker.patch('sys.stderr.write')
    title = "Test Exception"
    exc_info = (ValueError, ValueError("An error occurred"), None)

    exception(title, exc_info)

    assert mock_stderr.call_count == 1
    written_output = mock_stderr.call_args_list[0][0][0]
    assert "[WARN] Test Exception:" in written_output
    assert "An error occurred" in written_output
    assert "----------------------------" in written_output
