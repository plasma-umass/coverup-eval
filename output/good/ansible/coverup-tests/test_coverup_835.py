# file lib/ansible/utils/_junit_xml.py:167-170
# lines [167, 168, 170]
# branches []

import decimal
import dataclasses
import pytest
from ansible.utils._junit_xml import TestSuite, TestCase

# Assuming TestCase is a dataclass with a 'name' field and a 'time' field, similar to TestSuite
# If TestCase is not defined in the module, you would need to define it accordingly

def test_test_suite_time():
    # Create test cases with different times and names
    test_case1 = TestCase(name='test_case1', time=decimal.Decimal('1.23'))
    test_case2 = TestCase(name='test_case2', time=decimal.Decimal('2.34'))
    test_case3 = TestCase(name='test_case3', time=decimal.Decimal('0'))  # This should not affect the sum
    test_case4 = TestCase(name='test_case4', time=None)  # This should not affect the sum

    # Create a TestSuite with the test cases
    test_suite = TestSuite(name='test_suite', cases=[test_case1, test_case2, test_case3, test_case4])

    # Assert that the time property sums the times correctly
    expected_time = test_case1.time + test_case2.time
    assert test_suite.time == expected_time, "The total time should be the sum of the times of the test cases with non-zero and non-None times"
