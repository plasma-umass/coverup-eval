# file lib/ansible/utils/_junit_xml.py:89-92
# lines [89, 90, 92]
# branches []

import dataclasses
from ansible.utils._junit_xml import TestCase
import pytest

def test_testcase_is_error_property():
    # Create a TestCase instance with no errors
    test_case_no_errors = TestCase(name="test_no_errors", errors=[])
    assert not test_case_no_errors.is_error, "is_error should be False when there are no errors"

    # Create a TestCase instance with errors
    test_case_with_errors = TestCase(name="test_with_errors", errors=["Some error"])
    assert test_case_with_errors.is_error, "is_error should be True when there are errors"
