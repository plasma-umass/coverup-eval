# file: lib/ansible/utils/_junit_xml.py:89-92
# asked: {"lines": [89, 90, 92], "branches": []}
# gained: {"lines": [89, 90, 92], "branches": []}

import pytest
from ansible.utils._junit_xml import TestCase, TestError

def test_is_error_with_errors():
    test_case = TestCase(name="test_case_with_errors", errors=[TestError()])
    assert test_case.is_error is True

def test_is_error_without_errors():
    test_case = TestCase(name="test_case_without_errors", errors=[])
    assert test_case.is_error is False
