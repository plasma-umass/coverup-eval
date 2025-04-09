# file: lib/ansible/utils/_junit_xml.py:147-150
# asked: {"lines": [150], "branches": []}
# gained: {"lines": [150], "branches": []}

import pytest
from unittest.mock import Mock

from ansible.utils._junit_xml import TestSuite

class TestCase:
    def __init__(self, is_error):
        self.is_error = is_error

@pytest.fixture
def mock_test_cases():
    return [TestCase(is_error=True), TestCase(is_error=False), TestCase(is_error=True)]

def test_errors_property(mock_test_cases):
    test_suite = TestSuite(name="Sample Suite", cases=mock_test_cases)
    assert test_suite.errors == 2

def test_errors_property_no_errors():
    test_suite = TestSuite(name="Sample Suite", cases=[TestCase(is_error=False), TestCase(is_error=False)])
    assert test_suite.errors == 0
