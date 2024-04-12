# file lib/ansible/utils/_junit_xml.py:233-236
# lines [233, 234, 236]
# branches []

import decimal
import dataclasses
import pytest
from ansible.utils._junit_xml import TestSuites

# Assuming there is a TestSuite dataclass with a 'time' property
@dataclasses.dataclass
class TestSuite:
    time: decimal.Decimal

# Test function to cover the 'time' property of TestSuites
def test_testsuites_time_property():
    # Create some TestSuite instances with different times
    suite1 = TestSuite(time=decimal.Decimal('1.23'))
    suite2 = TestSuite(time=decimal.Decimal('4.56'))
    suite3 = TestSuite(time=decimal.Decimal('7.89'))

    # Create a TestSuites instance with the above test suites
    test_suites = TestSuites(suites=[suite1, suite2, suite3])

    # Calculate the expected total time
    expected_total_time = suite1.time + suite2.time + suite3.time

    # Assert that the 'time' property returns the correct total time
    assert test_suites.time == expected_total_time
