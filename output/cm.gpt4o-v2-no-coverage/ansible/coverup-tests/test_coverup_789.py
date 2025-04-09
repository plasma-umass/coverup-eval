# file: lib/ansible/utils/_junit_xml.py:213-216
# asked: {"lines": [213, 214, 216], "branches": []}
# gained: {"lines": [213, 214, 216], "branches": []}

import pytest
from ansible.utils._junit_xml import TestSuites

class MockTestSuite:
    def __init__(self, disabled):
        self.disabled = disabled

def test_disabled_property():
    # Create mock test suites with different disabled counts
    suite1 = MockTestSuite(disabled=1)
    suite2 = MockTestSuite(disabled=2)
    suite3 = MockTestSuite(disabled=3)
    
    # Create a TestSuites instance with the mock test suites
    test_suites = TestSuites(suites=[suite1, suite2, suite3])
    
    # Assert that the disabled property returns the correct sum
    assert test_suites.disabled == 6

    # Clean up
    del suite1
    del suite2
    del suite3
    del test_suites
