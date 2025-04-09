# file: lib/ansible/utils/_junit_xml.py:162-165
# asked: {"lines": [162, 163, 165], "branches": []}
# gained: {"lines": [162, 163, 165], "branches": []}

import pytest
from ansible.utils._junit_xml import TestSuite

def test_tests_property():
    # Create a TestSuite instance with a specific number of cases
    test_cases = [object(), object(), object()]  # Replace with actual TestCase instances if available
    suite = TestSuite(name="example", cases=test_cases)
    
    # Assert that the tests property returns the correct number of cases
    assert suite.tests == len(test_cases)
