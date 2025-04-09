# file: lib/ansible/utils/version.py:214-219
# asked: {"lines": [214, 215, 219], "branches": []}
# gained: {"lines": [214, 215, 219], "branches": []}

import pytest
from ansible.utils.version import SemanticVersion

def test_semantic_version_is_stable():
    # Test case where major version is 0 (should be unstable)
    version = SemanticVersion("0.1.0")
    assert not version.is_stable

    # Test case where it is a prerelease (should be unstable)
    version = SemanticVersion("1.0.0-alpha")
    assert not version.is_stable

    # Test case where major version is non-zero and not a prerelease (should be stable)
    version = SemanticVersion("1.0.0")
    assert version.is_stable

    # Test case where major version is non-zero and is a prerelease (should be unstable)
    version = SemanticVersion("1.0.0-beta")
    assert not version.is_stable
