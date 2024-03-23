# file lib/ansible/utils/_junit_xml.py:84-87
# lines [84, 85, 87]
# branches []

import dataclasses
from ansible.utils._junit_xml import TestCase
import pytest

# Test function to check the is_failure property
def test_is_failure_property():
    # Create a TestCase instance with no failures
    test_case_no_failures = TestCase(name="test_case_no_failures", classname="TestClass", time="0.1", failures=None)
    assert not test_case_no_failures.is_failure, "is_failure should be False when there are no failures"

    # Create a TestCase instance with failures
    test_case_with_failures = TestCase(name="test_case_with_failures", classname="TestClass", time="0.1", failures=["failure"])
    assert test_case_with_failures.is_failure, "is_failure should be True when there are failures"
