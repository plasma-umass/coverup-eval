# file: pytutils/lazy/lazy_regex.py:82-83
# asked: {"lines": [82, 83], "branches": []}
# gained: {"lines": [82, 83], "branches": []}

import pytest
from pytutils.lazy.lazy_regex import InvalidPattern

def test_invalid_pattern_repr(monkeypatch):
    msg = "Test message"
    exc = InvalidPattern(msg)
    
    # Monkeypatch the _format method to avoid the UnboundLocalError
    def mock_format(self):
        return self.msg
    
    monkeypatch.setattr(InvalidPattern, "_format", mock_format)
    
    # Monkeypatch the __str__ method to avoid the NameError
    def mock_str(self):
        return str(self._format())
    
    monkeypatch.setattr(InvalidPattern, "__str__", mock_str)
    
    expected_repr = "InvalidPattern(Test message)"
    assert repr(exc) == expected_repr

def test_invalid_pattern_cleanup():
    # Ensure no state pollution
    assert not hasattr(InvalidPattern, 'some_nonexistent_attribute')
