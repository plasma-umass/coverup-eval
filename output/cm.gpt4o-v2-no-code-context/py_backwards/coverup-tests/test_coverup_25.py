# file: py_backwards/utils/helpers.py:39-40
# asked: {"lines": [39, 40], "branches": []}
# gained: {"lines": [39, 40], "branches": []}

import pytest
import sys
from io import StringIO
from py_backwards.utils import helpers
from unittest import mock

def test_warn(monkeypatch):
    # Mock the sys.stderr to capture the output
    mock_stderr = StringIO()
    monkeypatch.setattr(sys, 'stderr', mock_stderr)
    
    # Mock the messages.warn function
    with mock.patch('py_backwards.utils.helpers.messages.warn', return_value="Warning message") as mock_warn:
        helpers.warn("Test warning")
        
        # Ensure the mock_warn was called with the correct argument
        mock_warn.assert_called_once_with("Test warning")
        
        # Ensure the output was written to stderr
        assert mock_stderr.getvalue() == "Warning message\n"
