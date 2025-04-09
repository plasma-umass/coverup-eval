# file: lib/ansible/utils/version.py:268-269
# asked: {"lines": [268, 269], "branches": []}
# gained: {"lines": [268, 269], "branches": []}

import pytest
from ansible.utils.version import SemanticVersion

def test_semantic_version_gt(monkeypatch):
    # Create mock versions for testing
    version1 = SemanticVersion("1.0.0")
    version2 = SemanticVersion("2.0.0")

    # Test __gt__ method
    assert version2 > version1
    assert not (version1 > version2)

    # Test equality to ensure __gt__ is not falsely triggered
    version3 = SemanticVersion("1.0.0")
    assert not (version1 > version3)
    assert not (version3 > version1)
