# file lib/ansible/utils/_junit_xml.py:238-247
# lines [238, 240, 241, 242, 243, 244, 245, 246]
# branches []

import pytest
from ansible.utils._junit_xml import TestSuites

# Assuming the existence of the _attributes function within the same module
# If it doesn't exist, this test will need to be adjusted accordingly.

def test_get_attributes():
    # Setup
    test_suites = TestSuites()

    # Exercise
    attributes = test_suites.get_attributes()

    # Verify
    assert isinstance(attributes, dict)

    # Cleanup - nothing to clean up as no external resources were modified
