# file: lib/ansible/utils/_junit_xml.py:162-165
# asked: {"lines": [162, 163, 165], "branches": []}
# gained: {"lines": [162, 163, 165], "branches": []}

import pytest
from ansible.utils._junit_xml import TestSuite, TestCase

def test_tests_property():
    # Create a TestSuite instance with some test cases
    test_cases = [TestCase(name="test1"), TestCase(name="test2"), TestCase(name="test3")]
    test_suite = TestSuite(name="suite1", cases=test_cases)
    
    # Assert that the tests property returns the correct number of test cases
    assert test_suite.tests == 3

    # Clean up
    del test_suite
    del test_cases
