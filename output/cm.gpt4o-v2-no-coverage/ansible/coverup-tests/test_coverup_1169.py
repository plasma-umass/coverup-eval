# file: lib/ansible/constants.py:23-30
# asked: {"lines": [25, 26, 27, 28, 29, 30], "branches": []}
# gained: {"lines": [25, 26, 27, 28, 29, 30], "branches": []}

import pytest
import sys
from unittest import mock

def test_warning_with_display(monkeypatch):
    # Mock the Display class and its warning method
    mock_display = mock.Mock()
    monkeypatch.setattr('ansible.utils.display.Display', mock_display)
    
    from ansible.constants import _warning
    
    test_msg = "Test message"
    _warning(test_msg)
    
    # Assert that Display().warning was called with the correct message
    mock_display().warning.assert_called_once_with(test_msg)

def test_warning_without_display(monkeypatch):
    # Mock the import to raise an ImportError
    def mock_import(name, *args):
        if name == 'ansible.utils.display':
            raise ImportError()
        return original_import(name, *args)
    
    original_import = __import__
    monkeypatch.setattr('builtins.__import__', mock_import)
    
    from ansible.constants import _warning
    
    test_msg = "Test message"
    
    with mock.patch('sys.stderr', new_callable=mock.Mock()) as mock_stderr:
        _warning(test_msg)
        # Assert that sys.stderr.write was called with the correct message
        mock_stderr.write.assert_called_once_with(' [WARNING] %s\n' % test_msg)
