# file: pytutils/lazy/lazy_import.py:105-106
# asked: {"lines": [106], "branches": []}
# gained: {"lines": [106], "branches": []}

import pytest
from pytutils.lazy.lazy_import import IllegalUseOfScopeReplacer

def test_illegal_use_of_scope_replacer_repr(monkeypatch):
    # Mock the _get_format_string method to avoid dependency issues
    def mock_get_format_string(self):
        return "ScopeReplacer object %(name)r was used incorrectly: %(msg)s%(extra)s"
    
    monkeypatch.setattr(IllegalUseOfScopeReplacer, "_get_format_string", mock_get_format_string)
    
    # Mock the __str__ method to avoid the 'unicode' issue
    def mock_str(self):
        s = self._format()
        return str(s)
    
    monkeypatch.setattr(IllegalUseOfScopeReplacer, "__str__", mock_str)
    
    # Create an instance of the exception
    exception_instance = IllegalUseOfScopeReplacer(name="test_name", msg="test_msg")
    
    # Check the __repr__ method
    expected_repr = "IllegalUseOfScopeReplacer(ScopeReplacer object 'test_name' was used incorrectly: test_msg)"
    assert repr(exception_instance) == expected_repr

    # Clean up
    del exception_instance
