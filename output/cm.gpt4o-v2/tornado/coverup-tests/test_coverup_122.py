# file: tornado/util.py:470-474
# asked: {"lines": [470, 472, 474], "branches": []}
# gained: {"lines": [470, 472, 474], "branches": []}

import unittest
import pytest
import tornado.util

def test_doctests(monkeypatch):
    # Mock the DocTestSuite to avoid running actual doctests
    mock_doctest_suite = unittest.TestSuite()
    monkeypatch.setattr('doctest.DocTestSuite', lambda: mock_doctest_suite)
    
    # Call the function and assert the return value
    result = tornado.util.doctests()
    assert result is mock_doctest_suite
