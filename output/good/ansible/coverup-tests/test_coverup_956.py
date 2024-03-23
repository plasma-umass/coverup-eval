# file lib/ansible/utils/version.py:259-260
# lines [259, 260]
# branches []

import pytest
from ansible.utils.version import SemanticVersion

# Assuming the SemanticVersion class has an __eq__ method defined elsewhere

def test_semantic_version_ne_method():
    version_a = SemanticVersion('1.0.0')
    version_b = SemanticVersion('1.0.0')
    version_c = SemanticVersion('2.0.0')

    # Test equality
    assert not (version_a != version_b), "Equal versions should return False for '!='"

    # Test inequality
    assert version_a != version_c, "Different versions should return True for '!='"
