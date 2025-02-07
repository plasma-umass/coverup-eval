# file: lib/ansible/utils/_junit_xml.py:94-97
# asked: {"lines": [94, 95, 97], "branches": []}
# gained: {"lines": [94, 95, 97], "branches": []}

import pytest
from ansible.utils._junit_xml import TestCase

def test_is_skipped():
    # Test when the test case is skipped
    test_case = TestCase(name="test_case_1", skipped="Skipped for some reason")
    assert test_case.is_skipped is True

    # Test when the test case is not skipped
    test_case = TestCase(name="test_case_2", skipped=None)
    assert test_case.is_skipped is False
