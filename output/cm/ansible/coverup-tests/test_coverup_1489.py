# file lib/ansible/utils/_junit_xml.py:94-97
# lines [97]
# branches []

import dataclasses
from ansible.utils._junit_xml import TestCase
import pytest

def test_is_skipped_property():
    # Create a TestCase instance with skipped attribute set to True
    test_case_skipped = TestCase(name="test_case_1", skipped=True)
    assert test_case_skipped.is_skipped is True, "is_skipped should return True when skipped is True"

    # Create a TestCase instance with skipped attribute set to False
    test_case_not_skipped = TestCase(name="test_case_2", skipped=False)
    assert test_case_not_skipped.is_skipped is False, "is_skipped should return False when skipped is False"

    # Create a TestCase instance with skipped attribute set to None
    test_case_none_skipped = TestCase(name="test_case_3", skipped=None)
    assert test_case_none_skipped.is_skipped is False, "is_skipped should return False when skipped is None"
