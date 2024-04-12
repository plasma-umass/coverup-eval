# file lib/ansible/utils/version.py:262-263
# lines [262, 263]
# branches []

import pytest
from ansible.utils.version import SemanticVersion

# Test function to cover __lt__ method in SemanticVersion class
def test_semantic_version_less_than():
    # Create two SemanticVersion instances
    version1 = SemanticVersion('1.0.0')
    version2 = SemanticVersion('2.0.0')

    # Assert that version1 is less than version2
    assert version1 < version2, "version1 should be less than version2"

    # Assert that version2 is not less than version1
    assert not (version2 < version1), "version2 should not be less than version1"

    # Cleanup is not necessary as no external state is modified
