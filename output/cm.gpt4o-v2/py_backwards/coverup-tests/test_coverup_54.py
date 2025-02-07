# file: py_backwards/transformers/metaclass.py:7-9
# asked: {"lines": [7, 8, 9], "branches": []}
# gained: {"lines": [7, 8, 9], "branches": []}

import pytest
import sys
from py_backwards.transformers.metaclass import six_import

def test_six_import(monkeypatch):
    # Ensure the six module is not already imported
    if 'six' in sys.modules:
        monkeypatch.delitem(sys.modules, 'six')

    # Access the original function wrapped by the snippet decorator
    original_six_import = six_import._fn

    # Call the original function to trigger the import
    original_six_import()

    # Verify that the six module is now imported
    assert 'six' in sys.modules
    assert hasattr(sys.modules['six'], 'with_metaclass')
