# file: lib/ansible/utils/_junit_xml.py:167-170
# asked: {"lines": [167, 168, 170], "branches": []}
# gained: {"lines": [167, 168, 170], "branches": []}

import pytest
import decimal
from ansible.utils._junit_xml import TestSuite

class TestCase:
    def __init__(self, time):
        self.time = time

@pytest.fixture
def test_suite():
    return TestSuite(name="example")

def test_time_property(test_suite):
    # Add test cases with different times
    test_suite.cases.append(TestCase(time=decimal.Decimal('1.1')))
    test_suite.cases.append(TestCase(time=decimal.Decimal('2.2')))
    test_suite.cases.append(TestCase(time=decimal.Decimal('0')))
    test_suite.cases.append(TestCase(time=None))

    # Assert the total time is the sum of the times of the test cases
    assert test_suite.time == decimal.Decimal('3.3')

    # Clean up
    test_suite.cases.clear()
