# file lib/ansible/utils/_junit_xml.py:162-165
# lines [165]
# branches []

import pytest
from unittest import mock
from ansible.utils._junit_xml import TestSuite

@pytest.fixture
def mock_test_suite():
    with mock.patch.object(TestSuite, '__annotations__', {'cases': list}):
        yield

def test_tests_property(mock_test_suite):
    # Arrange
    test_suite = TestSuite(name="dummy_name")
    test_suite.cases = [mock.Mock(), mock.Mock(), mock.Mock()]  # Mocking 3 test cases

    # Act
    result = test_suite.tests

    # Assert
    assert result == 3

    # Clean up
    test_suite.cases = []
