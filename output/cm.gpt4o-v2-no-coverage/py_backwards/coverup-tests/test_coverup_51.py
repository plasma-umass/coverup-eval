# file: py_backwards/transformers/metaclass.py:7-9
# asked: {"lines": [7, 8, 9], "branches": []}
# gained: {"lines": [7, 8, 9], "branches": []}

import pytest
import importlib
import sys

def test_six_import(monkeypatch):
    # Ensure 'six' is not already imported
    if 'six' in sys.modules:
        del sys.modules['six']
    
    # Mock the import of 'six'
    mock_six = type(sys)('six')
    mock_six.with_metaclass = 'mocked_with_metaclass'
    monkeypatch.setitem(sys.modules, 'six', mock_six)
    
    # Import the module containing six_import
    module = importlib.import_module('py_backwards.transformers.metaclass')
    
    # Access the snippet function
    snippet_fn = module.six_import._fn
    
    # Execute the snippet function
    snippet_fn()
    
    # Verify that the import was successful and the alias is correct
    assert 'six' in sys.modules
    assert sys.modules['six'].with_metaclass == 'mocked_with_metaclass'
    
    # Clean up
    del sys.modules['six']
    del sys.modules['py_backwards.transformers.metaclass']
