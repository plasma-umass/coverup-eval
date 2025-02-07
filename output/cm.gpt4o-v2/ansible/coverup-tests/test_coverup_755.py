# file: lib/ansible/utils/_junit_xml.py:218-221
# asked: {"lines": [218, 219, 221], "branches": []}
# gained: {"lines": [218, 219, 221], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.utils._junit_xml import TestSuites, TestSuite

def test_testsuites_errors():
    # Create mock TestSuite instances
    suite1 = MagicMock(spec=TestSuite)
    suite2 = MagicMock(spec=TestSuite)
    
    # Set the return value for the errors property
    suite1.errors = 1
    suite2.errors = 2
    
    # Create a TestSuites instance with the mock suites
    test_suites = TestSuites(suites=[suite1, suite2])
    
    # Assert that the errors property returns the correct sum
    assert test_suites.errors == 3
