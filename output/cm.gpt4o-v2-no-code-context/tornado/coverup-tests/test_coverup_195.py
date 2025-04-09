# file: tornado/util.py:470-474
# asked: {"lines": [472, 474], "branches": []}
# gained: {"lines": [472, 474], "branches": []}

import unittest
import pytest
from tornado.util import doctests

def test_doctests(monkeypatch):
    # Mock the doctest module to ensure the import line is executed
    import sys
    import doctest
    mock_doctest = unittest.mock.MagicMock()
    monkeypatch.setitem(sys.modules, 'doctest', mock_doctest)
    
    # Call the function and assert the return value
    result = doctests()
    mock_doctest.DocTestSuite.assert_called_once()
    assert result == mock_doctest.DocTestSuite()
