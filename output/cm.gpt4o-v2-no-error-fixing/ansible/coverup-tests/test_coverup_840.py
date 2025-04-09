# file: lib/ansible/utils/_junit_xml.py:223-226
# asked: {"lines": [226], "branches": []}
# gained: {"lines": [226], "branches": []}

import pytest
from unittest.mock import MagicMock

from ansible.utils._junit_xml import TestSuites, TestSuite

@pytest.fixture
def mock_test_suite():
    suite = MagicMock(spec=TestSuite)
    suite.failures = 1
    return suite

def test_failures_property(mock_test_suite):
    test_suites = TestSuites(suites=[mock_test_suite, mock_test_suite])
    assert test_suites.failures == 2

    # Clean up
    mock_test_suite.reset_mock()
