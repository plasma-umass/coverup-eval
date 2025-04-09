# file tornado/util.py:470-474
# lines [470, 472, 474]
# branches []

import unittest
import pytest
from tornado.util import doctests

def test_doctests(mocker):
    # Mock the doctest.DocTestSuite to ensure it's called and to prevent actual doctest running
    mock_doctest_suite = mocker.patch('doctest.DocTestSuite', return_value=unittest.TestSuite())

    # Call the function under test
    result = doctests()

    # Assert that the result is an instance of unittest.TestSuite
    assert isinstance(result, unittest.TestSuite)

    # Assert that doctest.DocTestSuite was called once
    mock_doctest_suite.assert_called_once()
