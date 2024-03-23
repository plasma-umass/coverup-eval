# file lib/ansible/utils/version.py:206-208
# lines [206, 207, 208]
# branches []

import pytest
from ansible.utils.version import SemanticVersion

# Test function to cover the 'core' property
def test_semantic_version_core():
    version = SemanticVersion('1.2.3')
    assert version.core == (1, 2, 3), "The core property did not return the expected tuple (major, minor, patch)"
