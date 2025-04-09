# file: lib/ansible/utils/_junit_xml.py:152-155
# asked: {"lines": [152, 153, 155], "branches": []}
# gained: {"lines": [152, 153, 155], "branches": []}

import pytest
from ansible.utils._junit_xml import TestSuite, TestCase

@pytest.fixture
def test_suite():
    return TestSuite(name="SampleTestSuite")

def test_failures_property(test_suite, mocker):
    # Create mock TestCase instances
    case1 = mocker.Mock(spec=TestCase)
    case2 = mocker.Mock(spec=TestCase)
    case3 = mocker.Mock(spec=TestCase)

    # Set the return values for the is_failure property
    case1.is_failure = True
    case2.is_failure = False
    case3.is_failure = True

    # Add the mock cases to the test suite
    test_suite.cases = [case1, case2, case3]

    # Assert that the failures property returns the correct count
    assert test_suite.failures == 2
