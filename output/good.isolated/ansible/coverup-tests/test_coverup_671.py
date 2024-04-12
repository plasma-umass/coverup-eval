# file lib/ansible/utils/_junit_xml.py:206-212
# lines [206, 207, 208, 209, 211]
# branches []

import pytest
from ansible.utils._junit_xml import TestSuites, TestSuite

# Assuming the existence of the TestSuite class, which is not provided in the snippet.
# If the TestSuite class does not exist, this test will need to be adjusted accordingly.

def test_test_suites_initialization():
    # Test initialization of TestSuites with default values
    test_suites = TestSuites()
    assert test_suites.name is None
    assert isinstance(test_suites.suites, list)
    assert len(test_suites.suites) == 0

    # Test initialization of TestSuites with a name and a list of suites
    suite = TestSuite(name="suite1")
    test_suites_with_data = TestSuites(name="test_suites", suites=[suite])
    assert test_suites_with_data.name == "test_suites"
    assert len(test_suites_with_data.suites) == 1
    assert test_suites_with_data.suites[0] == suite

# Note: No cleanup is necessary for this test as it does not modify any external state or resources.
# No use of pytest-mock is required as there are no external dependencies or side effects to mock.
