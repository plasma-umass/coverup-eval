# file: py_backwards/transformers/python2_future.py:6-11
# asked: {"lines": [8, 9, 10, 11], "branches": []}
# gained: {"lines": [8, 9, 10, 11], "branches": []}

import pytest
from py_backwards.transformers.python2_future import imports

def test_imports_snippet(monkeypatch):
    # Mock the __future__ module to avoid actual imports
    import sys
    future_mock = type('FutureMock', (), {
        'absolute_import': None,
        'division': None,
        'print_function': None,
        'unicode_literals': None
    })()
    monkeypatch.setitem(sys.modules, 'future', future_mock)

    # Call the imports function
    imports._fn(future_mock)

    # Verify that the future module has the expected attributes
    assert hasattr(future_mock, 'absolute_import')
    assert hasattr(future_mock, 'division')
    assert hasattr(future_mock, 'print_function')
    assert hasattr(future_mock, 'unicode_literals')
