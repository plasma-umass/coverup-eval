# file: lib/ansible/utils/_junit_xml.py:89-92
# asked: {"lines": [89, 90, 92], "branches": []}
# gained: {"lines": [89, 90, 92], "branches": []}

import pytest
from ansible.utils._junit_xml import TestCase, TestError

def test_is_error():
    # Create a TestCase instance with errors
    test_case_with_errors = TestCase(name="test_with_errors", errors=[TestError()])
    assert test_case_with_errors.is_error is True

    # Create a TestCase instance without errors
    test_case_without_errors = TestCase(name="test_without_errors")
    assert test_case_without_errors.is_error is False
