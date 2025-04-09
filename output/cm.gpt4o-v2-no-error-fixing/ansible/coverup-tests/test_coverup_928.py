# file: lib/ansible/utils/_junit_xml.py:142-145
# asked: {"lines": [145], "branches": []}
# gained: {"lines": [145], "branches": []}

import pytest
from unittest.mock import Mock

from ansible.utils._junit_xml import TestSuite, TestCase

def test_disabled_property():
    # Create mock test cases
    case1 = Mock(spec=TestCase)
    case1.is_disabled = True
    case2 = Mock(spec=TestCase)
    case2.is_disabled = False
    case3 = Mock(spec=TestCase)
    case3.is_disabled = True

    # Create a TestSuite with the mock test cases
    suite = TestSuite(name="suite", cases=[case1, case2, case3])

    # Assert that the disabled property counts the correct number of disabled cases
    assert suite.disabled == 2
