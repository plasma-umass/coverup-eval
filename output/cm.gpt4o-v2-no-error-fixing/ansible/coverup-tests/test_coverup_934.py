# file: lib/ansible/utils/_junit_xml.py:228-231
# asked: {"lines": [231], "branches": []}
# gained: {"lines": [231], "branches": []}

import pytest
from unittest.mock import MagicMock

from ansible.utils._junit_xml import TestSuites, TestSuite

def test_tests_property():
    # Create mock TestSuite instances
    suite1 = MagicMock(spec=TestSuite)
    suite1.tests = 5
    suite2 = MagicMock(spec=TestSuite)
    suite2.tests = 3

    # Create a TestSuites instance with the mock suites
    test_suites = TestSuites(suites=[suite1, suite2])

    # Assert that the tests property returns the correct sum
    assert test_suites.tests == 8

    # Clean up
    del test_suites
    del suite1
    del suite2
