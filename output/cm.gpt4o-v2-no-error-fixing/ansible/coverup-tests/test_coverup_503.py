# file: lib/ansible/utils/version.py:214-219
# asked: {"lines": [214, 215, 219], "branches": []}
# gained: {"lines": [214, 215, 219], "branches": []}

import pytest
from ansible.utils.version import SemanticVersion

def test_semantic_version_is_stable():
    # Test case where major version is 0 (not stable)
    version = SemanticVersion("0.1.0")
    assert not version.is_stable

    # Test case where it is a prerelease (not stable)
    version = SemanticVersion("1.0.0-alpha")
    assert not version.is_stable

    # Test case where it is a stable release
    version = SemanticVersion("1.0.0")
    assert version.is_stable

    # Test case where it is a stable release with build metadata
    version = SemanticVersion("1.0.0+20130313144700")
    assert version.is_stable

    # Test case where it is a stable release with prerelease and build metadata
    version = SemanticVersion("1.0.0-beta+exp.sha.5114f85")
    assert not version.is_stable
