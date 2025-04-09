# file: lib/ansible/utils/_junit_xml.py:213-216
# asked: {"lines": [216], "branches": []}
# gained: {"lines": [216], "branches": []}

import pytest
from unittest.mock import MagicMock

from ansible.utils._junit_xml import TestSuites, TestSuite

def test_disabled_property():
    # Create mock TestSuite instances
    suite1 = MagicMock()
    suite1.disabled = 1
    suite2 = MagicMock()
    suite2.disabled = 2

    # Create a TestSuites instance with the mock suites
    test_suites = TestSuites(suites=[suite1, suite2])

    # Assert that the disabled property returns the correct sum
    assert test_suites.disabled == 3

    # Clean up
    del test_suites
    del suite1
    del suite2
