# file: lib/ansible/utils/_junit_xml.py:84-87
# asked: {"lines": [84, 85, 87], "branches": []}
# gained: {"lines": [84, 85, 87], "branches": []}

import pytest
from ansible.utils._junit_xml import TestCase, TestFailure

def test_is_failure():
    # Test case with failures
    failure = TestFailure(message="failure message", type="failure type")
    test_case_with_failure = TestCase(name="test_with_failure", failures=[failure])
    assert test_case_with_failure.is_failure is True

    # Test case without failures
    test_case_without_failure = TestCase(name="test_without_failure")
    assert test_case_without_failure.is_failure is False
