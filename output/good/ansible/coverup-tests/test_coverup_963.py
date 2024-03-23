# file lib/ansible/utils/version.py:256-257
# lines [256, 257]
# branches []

import pytest
from ansible.utils.version import SemanticVersion

def test_semantic_version_eq(mocker):
    # Create two SemanticVersion instances
    version_a = SemanticVersion('1.0.0')
    version_b = SemanticVersion('1.0.0')
    version_c = SemanticVersion('2.0.0')

    # Test __eq__ method for equality
    assert version_a == version_b, "SemanticVersion __eq__ should return True for equal versions"
    assert not (version_a == version_c), "SemanticVersion __eq__ should return False for different versions"

    # Cleanup is not necessary as we are not modifying any external state
