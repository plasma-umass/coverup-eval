# file: lib/ansible/utils/_junit_xml.py:233-236
# asked: {"lines": [233, 234, 236], "branches": []}
# gained: {"lines": [233, 234, 236], "branches": []}

import pytest
import decimal
from unittest.mock import Mock
from ansible.utils._junit_xml import TestSuites

def test_time_property():
    # Create mock test suites with predefined times
    mock_suite1 = Mock()
    mock_suite1.time = decimal.Decimal('1.1')
    mock_suite2 = Mock()
    mock_suite2.time = decimal.Decimal('2.2')
    
    # Create a TestSuites instance with the mock suites
    test_suites = TestSuites(suites=[mock_suite1, mock_suite2])
    
    # Assert that the time property returns the correct total time
    assert test_suites.time == decimal.Decimal('3.3')
