# file: lib/ansible/utils/_junit_xml.py:223-226
# asked: {"lines": [223, 224, 226], "branches": []}
# gained: {"lines": [223, 224, 226], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.utils._junit_xml import TestSuites, TestSuite

def test_failures_property():
    # Create mock TestSuite objects with 'failures' properties
    suite1 = MagicMock(spec=TestSuite)
    suite1.failures = 1
    suite2 = MagicMock(spec=TestSuite)
    suite2.failures = 2
    suite3 = MagicMock(spec=TestSuite)
    suite3.failures = 0

    # Create a TestSuites object with the mock TestSuite objects
    test_suites = TestSuites(suites=[suite1, suite2, suite3])

    # Assert that the 'failures' property returns the correct sum
    assert test_suites.failures == 3
