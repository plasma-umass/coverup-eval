# file: lib/ansible/utils/version.py:136-145
# asked: {"lines": [136, 137, 138, 139, 140, 141, 142, 144, 145], "branches": [[144, 0], [144, 145]]}
# gained: {"lines": [136, 137, 138, 139, 140, 141, 142, 144, 145], "branches": [[144, 0], [144, 145]]}

import pytest
from ansible.utils.version import SemanticVersion

def test_semantic_version_init_with_vstring(mocker):
    mock_parse = mocker.patch.object(SemanticVersion, 'parse', autospec=True)
    version_string = "1.2.3"
    semver = SemanticVersion(version_string)
    
    assert semver.vstring == version_string
    assert semver.major is None
    assert semver.minor is None
    assert semver.patch is None
    assert semver.prerelease == ()
    assert semver.buildmetadata == ()
    mock_parse.assert_called_once_with(semver, version_string)

def test_semantic_version_init_without_vstring():
    semver = SemanticVersion()
    
    assert semver.vstring is None
    assert semver.major is None
    assert semver.minor is None
    assert semver.patch is None
    assert semver.prerelease == ()
    assert semver.buildmetadata == ()
