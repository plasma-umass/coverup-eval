# file lib/ansible/utils/_junit_xml.py:142-145
# lines [142, 143, 145]
# branches []

import dataclasses
from ansible.utils._junit_xml import TestSuite, TestCase
import pytest

# Define a test case for the TestSuite.disabled property
def test_testsuite_disabled_property():
    # Create a mock test case with is_disabled set to True
    disabled_case = TestCase(name="disabled_case")
    disabled_case.is_disabled = True

    # Create a mock test case with is_disabled set to False
    enabled_case = TestCase(name="enabled_case")
    enabled_case.is_disabled = False

    # Create a TestSuite with both disabled and enabled test cases
    suite = TestSuite(name="mock_suite", cases=[disabled_case, enabled_case])

    # Assert that the disabled property returns the correct count of disabled test cases
    assert suite.disabled == 1

    # Add another disabled test case to the suite
    another_disabled_case = TestCase(name="another_disabled_case")
    another_disabled_case.is_disabled = True
    suite.cases.append(another_disabled_case)

    # Assert that the disabled property is updated correctly
    assert suite.disabled == 2

    # Clean up by removing the test cases from the suite
    suite.cases.remove(disabled_case)
    suite.cases.remove(enabled_case)
    suite.cases.remove(another_disabled_case)

    # Assert that the disabled property is now 0 after cleanup
    assert suite.disabled == 0
