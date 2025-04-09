# file: lib/ansible/utils/_junit_xml.py:218-221
# asked: {"lines": [218, 219, 221], "branches": []}
# gained: {"lines": [218, 219, 221], "branches": []}

import pytest
from unittest.mock import MagicMock

from ansible.utils._junit_xml import TestSuites, TestSuite

@pytest.fixture
def mock_test_suite():
    suite = MagicMock(spec=TestSuite)
    suite.errors = 1
    return suite

def test_errors_property(mock_test_suite):
    test_suites = TestSuites(suites=[mock_test_suite, mock_test_suite])
    assert test_suites.errors == 2

    mock_test_suite.errors = 0
    test_suites = TestSuites(suites=[mock_test_suite, mock_test_suite])
    assert test_suites.errors == 0
