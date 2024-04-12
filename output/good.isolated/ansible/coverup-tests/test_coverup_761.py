# file lib/ansible/utils/_junit_xml.py:223-226
# lines [223, 224, 226]
# branches []

import dataclasses
from ansible.utils._junit_xml import TestSuites

# Assuming there is a TestSuite dataclass with a 'failures' attribute
@dataclasses.dataclass
class TestSuite:
    failures: int

def test_test_suites_failures_property():
    # Create mock test suites with varying numbers of failures
    suite1 = TestSuite(failures=1)
    suite2 = TestSuite(failures=2)
    suite3 = TestSuite(failures=0)

    # Create a TestSuites instance with the mock test suites
    test_suites = TestSuites(suites=[suite1, suite2, suite3])

    # Assert that the failures property sums the failures correctly
    assert test_suites.failures == 3
