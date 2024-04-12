# file lib/ansible/utils/_junit_xml.py:218-221
# lines [218, 219, 221]
# branches []

import dataclasses
from ansible.utils._junit_xml import TestSuites

# Assuming there is a TestSuite dataclass with an 'errors' attribute
@dataclasses.dataclass
class TestSuite:
    errors: int

# Test function to cover the 'errors' property
def test_test_suites_errors_property():
    # Create mock test suites with varying numbers of errors
    suite1 = TestSuite(errors=1)
    suite2 = TestSuite(errors=2)
    suite3 = TestSuite(errors=3)

    # Create a TestSuites instance with the mock test suites
    test_suites = TestSuites(suites=[suite1, suite2, suite3])

    # Assert that the 'errors' property correctly sums the errors
    assert test_suites.errors == 6
