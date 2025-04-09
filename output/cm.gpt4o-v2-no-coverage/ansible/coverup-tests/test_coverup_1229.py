# file: lib/ansible/utils/_junit_xml.py:167-170
# asked: {"lines": [170], "branches": []}
# gained: {"lines": [170], "branches": []}

import pytest
import decimal
from unittest.mock import Mock

from ansible.utils._junit_xml import TestSuite

@pytest.fixture
def mock_test_case():
    mock_case = Mock()
    mock_case.time = decimal.Decimal('1.23')
    return mock_case

def test_time_property(mock_test_case):
    suite = TestSuite(name="suite", cases=[mock_test_case])
    assert suite.time == decimal.Decimal('1.23')

def test_time_property_no_cases():
    suite = TestSuite(name="suite", cases=[])
    assert suite.time == decimal.Decimal('0')

def test_time_property_case_without_time():
    mock_case = Mock()
    mock_case.time = None
    suite = TestSuite(name="suite", cases=[mock_case])
    assert suite.time == decimal.Decimal('0')
