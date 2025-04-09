# file: tornado/util.py:470-474
# asked: {"lines": [470, 472, 474], "branches": []}
# gained: {"lines": [470, 472, 474], "branches": []}

import unittest
import pytest
from tornado.util import doctests

def test_doctests():
    suite = doctests()
    assert isinstance(suite, unittest.TestSuite)
    assert len(suite._tests) > 0  # Ensure that the suite contains tests

