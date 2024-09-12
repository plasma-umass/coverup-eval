# file: lib/ansible/constants.py:33-40
# asked: {"lines": [33, 35, 36, 37, 38, 39, 40], "branches": []}
# gained: {"lines": [33, 35, 36, 37, 38, 39, 40], "branches": []}

import pytest
import sys
from unittest.mock import patch, MagicMock

# Assuming the function _deprecated is imported from ansible.constants
from ansible.constants import _deprecated

def test_deprecated_with_display(monkeypatch):
    mock_display = MagicMock()
    monkeypatch.setattr('ansible.utils.display.Display', lambda: mock_display)
    
    _deprecated("test message", "2.0")
    
    mock_display.deprecated.assert_called_once_with("test message", version="2.0")

def test_deprecated_without_display(monkeypatch):
    mock_stderr = MagicMock()
    monkeypatch.setattr(sys, 'stderr', mock_stderr)
    
    with patch('ansible.utils.display.Display', side_effect=ImportError):
        _deprecated("test message", "2.0")
    
    mock_stderr.write.assert_called_once_with(' [DEPRECATED] test message, to be removed in 2.0\n')
