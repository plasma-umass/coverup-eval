# file: lib/ansible/utils/_junit_xml.py:233-236
# asked: {"lines": [233, 234, 236], "branches": []}
# gained: {"lines": [233, 234, 236], "branches": []}

import pytest
import decimal
from ansible.utils._junit_xml import TestSuites, TestSuite

class MockTestSuite:
    def __init__(self, time):
        self._time = time

    @property
    def time(self):
        return self._time

def test_time_property():
    # Create mock TestSuite objects with predefined times
    suite1 = MockTestSuite(time=decimal.Decimal('1.1'))
    suite2 = MockTestSuite(time=decimal.Decimal('2.2'))
    suite3 = MockTestSuite(time=decimal.Decimal('3.3'))

    # Create a TestSuites object with the mock TestSuite objects
    test_suites = TestSuites(suites=[suite1, suite2, suite3])

    # Assert that the time property returns the correct total time
    assert test_suites.time == decimal.Decimal('6.6')
