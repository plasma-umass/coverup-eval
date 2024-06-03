# file lib/ansible/utils/version.py:214-219
# lines [214, 215, 219]
# branches []

import pytest
from packaging.version import Version
from ansible.utils.version import SemanticVersion

def test_semantic_version_is_stable():
    # Test case where major version is 0
    version = SemanticVersion("0.1.0")
    assert not version.is_stable, "Version 0.1.0 should not be stable"

    # Test case where it is a prerelease
    version = SemanticVersion("1.0.0-alpha")
    assert not version.is_stable, "Version 1.0.0-alpha should not be stable"

    # Test case where it is a stable release
    version = SemanticVersion("1.0.0")
    assert version.is_stable, "Version 1.0.0 should be stable"

    # Test case where it is a stable release with patch version
    version = SemanticVersion("1.0.1")
    assert version.is_stable, "Version 1.0.1 should be stable"

    # Test case where it is a stable release with minor version
    version = SemanticVersion("1.1.0")
    assert version.is_stable, "Version 1.1.0 should be stable"
