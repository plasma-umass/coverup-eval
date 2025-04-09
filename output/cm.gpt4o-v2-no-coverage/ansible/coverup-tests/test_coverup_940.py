# file: lib/ansible/utils/version.py:256-257
# asked: {"lines": [256, 257], "branches": []}
# gained: {"lines": [256, 257], "branches": []}

import pytest
from ansible.utils.version import SemanticVersion

class MockVersion:
    def _cmp(self, other):
        if self.vstring == other.vstring:
            return 0
        return -1 if self.vstring < other.vstring else 1

def test_semantic_version_eq():
    version1 = SemanticVersion("1.0.0")
    version2 = SemanticVersion("1.0.0")
    version3 = SemanticVersion("2.0.0")

    assert version1 == version2
    assert not (version1 == version3)

@pytest.fixture(autouse=True)
def mock_version(monkeypatch):
    monkeypatch.setattr(SemanticVersion, "_cmp", MockVersion._cmp)
