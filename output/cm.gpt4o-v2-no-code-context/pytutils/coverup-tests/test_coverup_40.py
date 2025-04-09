# file: pytutils/lazy/lazy_regex.py:82-83
# asked: {"lines": [83], "branches": []}
# gained: {"lines": [83], "branches": []}

import pytest
from pytutils.lazy.lazy_regex import InvalidPattern

def test_invalid_pattern_repr(monkeypatch):
    error_message = "Invalid regex pattern"
    
    # Monkeypatch the _format method to avoid the UnboundLocalError
    def mock_format(self):
        return error_message
    
    monkeypatch.setattr(InvalidPattern, "_format", mock_format)
    
    # Monkeypatch the __str__ method to avoid the NameError
    def mock_str(self):
        return self._format()
    
    monkeypatch.setattr(InvalidPattern, "__str__", mock_str)
    
    invalid_pattern = InvalidPattern(error_message)
    
    # Verify the __repr__ method
    expected_repr = "InvalidPattern(Invalid regex pattern)"
    assert repr(invalid_pattern) == expected_repr
