# file: lib/ansible/utils/_junit_xml.py:147-150
# asked: {"lines": [150], "branches": []}
# gained: {"lines": [150], "branches": []}

import pytest
from unittest.mock import MagicMock

# Assuming the TestSuite class is imported from ansible.utils._junit_xml
from ansible.utils._junit_xml import TestSuite

@pytest.fixture
def mock_test_case():
    class MockTestCase:
        def __init__(self, is_error):
            self.is_error = is_error
    return MockTestCase

@pytest.fixture
def test_suite(mock_test_case):
    class TestSuiteWithCases(TestSuite):
        def __init__(self, name, cases):
            super().__init__(name)
            self.cases = cases
    return TestSuiteWithCases

def test_errors_property_all_cases_error(test_suite, mock_test_case):
    cases = [mock_test_case(True), mock_test_case(True), mock_test_case(True)]
    test_suite_instance = test_suite("test_suite", cases)
    assert test_suite_instance.errors == 3

def test_errors_property_no_cases_error(test_suite, mock_test_case):
    cases = [mock_test_case(False), mock_test_case(False), mock_test_case(False)]
    test_suite_instance = test_suite("test_suite", cases)
    assert test_suite_instance.errors == 0

def test_errors_property_some_cases_error(test_suite, mock_test_case):
    cases = [mock_test_case(True), mock_test_case(False), mock_test_case(True)]
    test_suite_instance = test_suite("test_suite", cases)
    assert test_suite_instance.errors == 2
