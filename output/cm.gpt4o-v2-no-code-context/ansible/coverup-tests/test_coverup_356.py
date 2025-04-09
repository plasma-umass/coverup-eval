# file: lib/ansible/utils/version.py:136-145
# asked: {"lines": [136, 137, 138, 139, 140, 141, 142, 144, 145], "branches": [[144, 0], [144, 145]]}
# gained: {"lines": [136, 137, 138, 139, 140, 141, 142, 144, 145], "branches": [[144, 0], [144, 145]]}

import pytest
from ansible.utils.version import SemanticVersion

def test_semantic_version_init_with_vstring(mocker):
    vstring = "1.2.3"
    mocker.patch.object(SemanticVersion, 'parse', return_value=None)
    version = SemanticVersion(vstring)
    assert version.vstring == vstring
    assert version.major is None
    assert version.minor is None
    assert version.patch is None
    assert version.prerelease == ()
    assert version.buildmetadata == ()
    version.parse.assert_called_once_with(vstring)

def test_semantic_version_init_without_vstring():
    version = SemanticVersion()
    assert version.vstring is None
    assert version.major is None
    assert version.minor is None
    assert version.patch is None
    assert version.prerelease == ()
    assert version.buildmetadata == ()
