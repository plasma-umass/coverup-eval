# file: lib/ansible/utils/_junit_xml.py:228-231
# asked: {"lines": [228, 229, 231], "branches": []}
# gained: {"lines": [228, 229, 231], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.utils._junit_xml import TestSuites, TestSuite

def test_tests_property():
    # Create mock TestSuite objects with a 'tests' property
    suite1 = MagicMock(spec=TestSuite)
    suite1.tests = 5
    suite2 = MagicMock(spec=TestSuite)
    suite2.tests = 10
    
    # Create a TestSuites object with the mock suites
    test_suites = TestSuites(suites=[suite1, suite2])
    
    # Assert that the 'tests' property returns the correct sum
    assert test_suites.tests == 15

    # Clean up
    del suite1
    del suite2
    del test_suites
