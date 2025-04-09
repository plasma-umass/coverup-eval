# file: py_backwards/utils/helpers.py:39-40
# asked: {"lines": [40], "branches": []}
# gained: {"lines": [40], "branches": []}

import pytest
import sys
from py_backwards.utils.helpers import warn
from py_backwards import messages

def test_warn(monkeypatch):
    # Mock the messages.warn function
    def mock_warn(message):
        return f"MOCK WARN: {message}"
    
    monkeypatch.setattr(messages, "warn", mock_warn)
    
    # Capture the output to stderr
    captured_output = []
    
    def mock_print(*args, **kwargs):
        captured_output.append(args[0])
    
    monkeypatch.setattr(sys, "stderr", captured_output)
    monkeypatch.setattr("builtins.print", mock_print)
    
    # Call the warn function
    warn("This is a test warning")
    
    # Assert the output
    assert captured_output == ["MOCK WARN: This is a test warning"]
