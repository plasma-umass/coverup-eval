# file: lib/ansible/utils/_junit_xml.py:94-97
# asked: {"lines": [94, 95, 97], "branches": []}
# gained: {"lines": [94, 95, 97], "branches": []}

import pytest
from ansible.utils._junit_xml import TestCase

@pytest.fixture
def test_case():
    return TestCase(name="test_case")

def test_is_skipped_true(test_case):
    test_case.skipped = "some reason"
    assert test_case.is_skipped is True

def test_is_skipped_false(test_case):
    test_case.skipped = None
    assert test_case.is_skipped is False
