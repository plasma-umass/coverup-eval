# file: lib/ansible/utils/_junit_xml.py:147-150
# asked: {"lines": [147, 148, 150], "branches": []}
# gained: {"lines": [147, 148, 150], "branches": []}

import pytest
from unittest.mock import Mock

from ansible.utils._junit_xml import TestSuite

@pytest.fixture
def mock_test_case():
    mock_case = Mock()
    mock_case.is_error = False
    return mock_case

def test_errors_no_errors(mock_test_case):
    suite = TestSuite(name="suite", cases=[mock_test_case])
    assert suite.errors == 0

def test_errors_with_errors(mock_test_case):
    mock_test_case.is_error = True
    suite = TestSuite(name="suite", cases=[mock_test_case])
    assert suite.errors == 1

def test_errors_mixed_cases(mock_test_case):
    mock_test_case1 = Mock()
    mock_test_case1.is_error = True
    mock_test_case2 = Mock()
    mock_test_case2.is_error = False
    suite = TestSuite(name="suite", cases=[mock_test_case1, mock_test_case2])
    assert suite.errors == 1
