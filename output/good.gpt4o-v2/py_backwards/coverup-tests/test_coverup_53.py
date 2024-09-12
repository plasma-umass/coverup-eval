# file: py_backwards/utils/helpers.py:39-40
# asked: {"lines": [39, 40], "branches": []}
# gained: {"lines": [39, 40], "branches": []}

import pytest
import sys
from io import StringIO
from py_backwards.utils.helpers import warn
from py_backwards import messages

def test_warn(monkeypatch):
    # Mock sys.stderr to capture the output
    mock_stderr = StringIO()
    monkeypatch.setattr(sys, 'stderr', mock_stderr)

    # Mock messages.warn to return a known string
    def mock_warn(message):
        return f"MOCK WARN: {message}"
    monkeypatch.setattr(messages, 'warn', mock_warn)

    # Call the function
    warn("test message")

    # Check the output
    assert mock_stderr.getvalue() == "MOCK WARN: test message\n"
