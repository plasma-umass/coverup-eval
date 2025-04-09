# file: lib/ansible/utils/_junit_xml.py:218-221
# asked: {"lines": [221], "branches": []}
# gained: {"lines": [221], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.utils._junit_xml import TestSuites, TestSuite

def test_errors_property():
    # Create mock TestSuite objects with errors attribute
    suite1 = MagicMock()
    suite1.errors = 1
    suite2 = MagicMock()
    suite2.errors = 2

    # Create a TestSuites object with the mock TestSuite objects
    test_suites = TestSuites(suites=[suite1, suite2])

    # Assert that the errors property returns the correct sum
    assert test_suites.errors == 3
