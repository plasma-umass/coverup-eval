# file: lib/ansible/utils/_junit_xml.py:142-145
# asked: {"lines": [142, 143, 145], "branches": []}
# gained: {"lines": [142, 143, 145], "branches": []}

import pytest
from ansible.utils._junit_xml import TestSuite, TestCase

def test_disabled_property():
    # Create test cases with different 'is_disabled' values
    test_cases = [
        TestCase(name="test1", is_disabled=True),
        TestCase(name="test2", is_disabled=False),
        TestCase(name="test3", is_disabled=True)
    ]
    
    # Create a TestSuite with the test cases
    test_suite = TestSuite(name="suite1", cases=test_cases)
    
    # Assert that the 'disabled' property returns the correct count of disabled test cases
    assert test_suite.disabled == 2

    # Clean up
    del test_suite
    del test_cases
