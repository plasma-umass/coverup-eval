# file lib/ansible/utils/version.py:268-269
# lines [268, 269]
# branches []

import pytest
from ansible.utils.version import SemanticVersion

# Assuming the SemanticVersion class has an __init__ method and a _cmp method
# that need to be implemented for the test to work.

# Test function to cover the __gt__ method in SemanticVersion class
def test_semantic_version_greater_than():
    # Create instances of SemanticVersion
    version1 = SemanticVersion("2.0.0")
    version2 = SemanticVersion("1.0.0")

    # Assert that version1 is greater than version2
    assert version1 > version2

    # Clean up if necessary (not needed in this case as no external resources are used)
