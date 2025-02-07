# file: lib/ansible/utils/_junit_xml.py:223-226
# asked: {"lines": [223, 224, 226], "branches": []}
# gained: {"lines": [223, 224, 226], "branches": []}

import pytest
from ansible.utils._junit_xml import TestSuites, TestSuite, TestCase, TestFailure

def test_failures_property():
    # Create mock TestCase objects with 'failures' attributes
    case1 = TestCase(name="case1", failures=[TestFailure(message="failure1")])
    case2 = TestCase(name="case2", failures=[TestFailure(message="failure2")])
    case3 = TestCase(name="case3")

    # Create TestSuite objects containing the TestCase objects
    suite1 = TestSuite(name="suite1", cases=[case1])
    suite2 = TestSuite(name="suite2", cases=[case2])
    suite3 = TestSuite(name="suite3", cases=[case3])

    # Create a TestSuites object with the TestSuite objects
    test_suites = TestSuites(suites=[suite1, suite2, suite3])

    # Assert that the 'failures' property returns the correct sum
    assert test_suites.failures == 2

    # Clean up
    del case1
    del case2
    del case3
    del suite1
    del suite2
    del suite3
    del test_suites
