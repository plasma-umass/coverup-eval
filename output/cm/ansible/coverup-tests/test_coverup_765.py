# file lib/ansible/utils/version.py:210-212
# lines [210, 211, 212]
# branches []

import pytest
from ansible.utils.version import SemanticVersion

# Test function to check the is_prerelease property
def test_is_prerelease():
    # Create a SemanticVersion instance with a prerelease version
    prerelease_version = SemanticVersion('1.0.0-alpha')
    assert prerelease_version.is_prerelease is True, "The is_prerelease property should return True for a prerelease version"

    # Create a SemanticVersion instance with a non-prerelease version
    non_prerelease_version = SemanticVersion('1.0.0')
    assert non_prerelease_version.is_prerelease is False, "The is_prerelease property should return False for a non-prerelease version"
