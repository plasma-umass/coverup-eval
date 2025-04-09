# file: lib/ansible/utils/_junit_xml.py:233-236
# asked: {"lines": [233, 234, 236], "branches": []}
# gained: {"lines": [233, 234, 236], "branches": []}

import pytest
import decimal
from unittest.mock import MagicMock
from ansible.utils._junit_xml import TestSuites, TestSuite

def test_testsuites_time():
    # Create mock TestSuite instances with predefined times
    suite1 = MagicMock(spec=TestSuite)
    suite1.time = decimal.Decimal('1.1')
    
    suite2 = MagicMock(spec=TestSuite)
    suite2.time = decimal.Decimal('2.2')
    
    # Create a TestSuites instance with the mock suites
    test_suites = TestSuites(suites=[suite1, suite2])
    
    # Assert that the time property returns the correct total time
    assert test_suites.time == decimal.Decimal('3.3')
