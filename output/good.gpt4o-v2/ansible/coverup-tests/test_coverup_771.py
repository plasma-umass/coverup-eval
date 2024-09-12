# file: lib/ansible/utils/_junit_xml.py:213-216
# asked: {"lines": [213, 214, 216], "branches": []}
# gained: {"lines": [213, 214, 216], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.utils._junit_xml import TestSuites, TestSuite

def test_disabled_property():
    # Create mock TestSuite objects with 'disabled' properties
    suite1 = MagicMock(spec=TestSuite, disabled=1)
    suite2 = MagicMock(spec=TestSuite, disabled=2)
    suite3 = MagicMock(spec=TestSuite, disabled=3)
    
    # Create a TestSuites object with the mock TestSuite objects
    test_suites = TestSuites(suites=[suite1, suite2, suite3])
    
    # Assert that the 'disabled' property returns the correct sum
    assert test_suites.disabled == 6

    # Clean up
    del suite1
    del suite2
    del suite3
    del test_suites
