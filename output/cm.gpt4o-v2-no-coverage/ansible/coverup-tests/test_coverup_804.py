# file: lib/ansible/utils/_junit_xml.py:157-160
# asked: {"lines": [157, 158, 160], "branches": []}
# gained: {"lines": [157, 158, 160], "branches": []}

import pytest
import dataclasses
from unittest.mock import Mock

from ansible.utils._junit_xml import TestSuite

@dataclasses.dataclass
class TestCase:
    is_skipped: bool

def test_skipped_property():
    # Create test cases
    case1 = TestCase(is_skipped=True)
    case2 = TestCase(is_skipped=False)
    case3 = TestCase(is_skipped=True)

    # Create a test suite with the test cases
    suite = TestSuite(name="suite", cases=[case1, case2, case3])

    # Assert the skipped property
    assert suite.skipped == 2

    # Clean up
    del suite
    del case1
    del case2
    del case3
