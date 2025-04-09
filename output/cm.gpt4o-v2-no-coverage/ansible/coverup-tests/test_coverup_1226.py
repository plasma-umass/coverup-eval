# file: lib/ansible/utils/_junit_xml.py:84-87
# asked: {"lines": [87], "branches": []}
# gained: {"lines": [87], "branches": []}

import pytest
from ansible.utils._junit_xml import TestCase, TestFailure

def test_is_failure_with_failures():
    test_case = TestCase(name="test_case_with_failures", failures=[TestFailure()])
    assert test_case.is_failure is True

def test_is_failure_without_failures():
    test_case = TestCase(name="test_case_without_failures")
    assert test_case.is_failure is False
