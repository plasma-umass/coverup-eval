# file: lib/ansible/utils/_junit_xml.py:142-145
# asked: {"lines": [142, 143, 145], "branches": []}
# gained: {"lines": [142, 143, 145], "branches": []}

import pytest
from ansible.utils._junit_xml import TestSuite, TestCase

def test_disabled_property():
    # Create test cases
    case1 = TestCase(name="test1", is_disabled=True)
    case2 = TestCase(name="test2", is_disabled=False)
    case3 = TestCase(name="test3", is_disabled=True)

    # Create a test suite with the test cases
    suite = TestSuite(name="suite1", cases=[case1, case2, case3])

    # Assert the number of disabled test cases
    assert suite.disabled == 2

    # Clean up
    del case1
    del case2
    del case3
    del suite
