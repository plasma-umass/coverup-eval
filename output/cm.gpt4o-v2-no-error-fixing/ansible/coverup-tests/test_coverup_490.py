# file: lib/ansible/utils/_junit_xml.py:94-97
# asked: {"lines": [94, 95, 97], "branches": []}
# gained: {"lines": [94, 95, 97], "branches": []}

import pytest
from ansible.utils._junit_xml import TestCase

def test_is_skipped():
    # Test when skipped is None
    test_case = TestCase(name="test_case_1", skipped=None)
    assert not test_case.is_skipped

    # Test when skipped is an empty string
    test_case = TestCase(name="test_case_2", skipped="")
    assert not test_case.is_skipped

    # Test when skipped is a non-empty string
    test_case = TestCase(name="test_case_3", skipped="some reason")
    assert test_case.is_skipped
