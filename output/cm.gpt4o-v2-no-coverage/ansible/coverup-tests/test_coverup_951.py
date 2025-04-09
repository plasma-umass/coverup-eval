# file: lib/ansible/utils/version.py:268-269
# asked: {"lines": [268, 269], "branches": []}
# gained: {"lines": [268, 269], "branches": []}

import pytest
from ansible.utils.version import SemanticVersion
from ansible.module_utils.compat.version import Version

class MockVersion(Version):
    def __init__(self, vstring=None):
        self.vstring = vstring

    def _cmp(self, other):
        if self.vstring == other.vstring:
            return 0
        return 1 if self.vstring > other.vstring else -1

def test_semantic_version_gt():
    version1 = SemanticVersion("1.0.0")
    version2 = SemanticVersion("0.9.0")
    assert version1 > version2

    version3 = SemanticVersion("1.0.0")
    version4 = SemanticVersion("1.0.0")
    assert not (version3 > version4)

    version5 = SemanticVersion("0.9.0")
    version6 = SemanticVersion("1.0.0")
    assert not (version5 > version6)

def test_semantic_version_gt_with_mock(monkeypatch):
    def mock_cmp(self, other):
        if self.major == 1 and other.major == 0:
            return 1
        return -1

    monkeypatch.setattr(SemanticVersion, "_cmp", mock_cmp)

    version1 = SemanticVersion("1.0.0")
    version2 = SemanticVersion("0.9.0")
    assert version1 > version2

    version3 = SemanticVersion("0.9.0")
    version4 = SemanticVersion("1.0.0")
    assert not (version3 > version4)
