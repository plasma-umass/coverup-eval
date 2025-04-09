# file: lib/ansible/utils/version.py:256-257
# asked: {"lines": [256, 257], "branches": []}
# gained: {"lines": [256, 257], "branches": []}

import pytest
from ansible.utils.version import SemanticVersion

def test_semantic_version_eq(monkeypatch):
    # Create a mock for the _cmp method to control its return value
    def mock_cmp(self, other):
        return 0

    # Apply the monkeypatch to the _cmp method
    monkeypatch.setattr(SemanticVersion, "_cmp", mock_cmp)

    # Create two instances of SemanticVersion
    version1 = SemanticVersion("1.0.0")
    version2 = SemanticVersion("1.0.0")

    # Test the __eq__ method
    assert version1 == version2

    # Clean up by removing the monkeypatch
    monkeypatch.undo()
