# file lib/ansible/utils/_junit_xml.py:206-212
# lines [206, 207, 208, 209, 211]
# branches []

import pytest
from ansible.utils._junit_xml import TestSuites, TestSuite

def test_testsuites_initialization():
    # Test initialization with default values
    ts_default = TestSuites()
    assert ts_default.name is None
    assert isinstance(ts_default.suites, list)
    assert len(ts_default.suites) == 0

    # Test initialization with custom values
    ts_custom_suite = TestSuite(name="Custom Test Suite")
    ts_custom = TestSuites(name="Custom Suite", suites=[ts_custom_suite])
    assert ts_custom.name == "Custom Suite"
    assert isinstance(ts_custom.suites, list)
    assert len(ts_custom.suites) == 1
    assert isinstance(ts_custom.suites[0], TestSuite)
    assert ts_custom.suites[0].name == "Custom Test Suite"
