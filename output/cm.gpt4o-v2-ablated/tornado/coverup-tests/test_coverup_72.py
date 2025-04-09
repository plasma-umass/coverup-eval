# file: tornado/util.py:470-474
# asked: {"lines": [470, 472, 474], "branches": []}
# gained: {"lines": [470, 472, 474], "branches": []}

import unittest
import pytest
import doctest
from tornado.util import doctests

def test_doctests(monkeypatch):
    # Mock the DocTestSuite to ensure it is called and to avoid running actual doctests
    mock_doc_test_suite = unittest.TestSuite()
    monkeypatch.setattr(doctest, 'DocTestSuite', lambda: mock_doc_test_suite)
    
    # Call the function and assert the return value is the mocked DocTestSuite
    result = doctests()
    assert result is mock_doc_test_suite
