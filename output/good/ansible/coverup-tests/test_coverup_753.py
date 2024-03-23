# file lib/ansible/utils/_junit_xml.py:228-231
# lines [228, 229, 231]
# branches []

import dataclasses
from ansible.utils._junit_xml import TestSuites

# Assuming there is a TestSuite dataclass with a 'tests' attribute
@dataclasses.dataclass
class TestSuite:
    tests: int

def test_tests_property():
    # Create mock test suites
    suite1 = TestSuite(tests=5)
    suite2 = TestSuite(tests=3)
    suite3 = TestSuite(tests=7)

    # Create a TestSuites instance with the mock test suites
    test_suites = TestSuites(suites=[suite1, suite2, suite3])

    # Assert that the 'tests' property returns the correct sum of tests
    assert test_suites.tests == 15
