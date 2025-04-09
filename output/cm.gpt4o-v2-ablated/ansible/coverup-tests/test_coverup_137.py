# file: lib/ansible/utils/version.py:136-145
# asked: {"lines": [136, 137, 138, 139, 140, 141, 142, 144, 145], "branches": [[144, 0], [144, 145]]}
# gained: {"lines": [136, 137, 138, 139, 140, 141, 142, 144, 145], "branches": [[144, 0], [144, 145]]}

import pytest
from ansible.utils.version import SemanticVersion

def test_semantic_version_init_no_vstring():
    version = SemanticVersion()
    assert version.vstring is None
    assert version.major is None
    assert version.minor is None
    assert version.patch is None
    assert version.prerelease == ()
    assert version.buildmetadata == ()

def test_semantic_version_init_with_vstring(monkeypatch):
    def mock_parse(self, vstring):
        self.major = 1
        self.minor = 2
        self.patch = 3
        self.prerelease = ('alpha',)
        self.buildmetadata = ('001',)
    
    monkeypatch.setattr(SemanticVersion, 'parse', mock_parse)
    
    version = SemanticVersion("1.2.3-alpha+001")
    assert version.vstring == "1.2.3-alpha+001"
    assert version.major == 1
    assert version.minor == 2
    assert version.patch == 3
    assert version.prerelease == ('alpha',)
    assert version.buildmetadata == ('001',)
