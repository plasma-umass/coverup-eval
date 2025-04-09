# file: lib/ansible/utils/version.py:191-204
# asked: {"lines": [191, 192, 193, 194, 196, 197, 198, 199, 201, 202, 203, 204], "branches": [[193, 194], [193, 196], [201, 202], [201, 203], [203, 0], [203, 204]]}
# gained: {"lines": [191, 192, 193, 194, 196, 197, 198, 199, 201, 202, 203, 204], "branches": [[193, 194], [193, 196], [201, 202], [201, 203], [203, 0], [203, 204]]}

import pytest
from ansible.utils.version import SemanticVersion

def test_semantic_version_parse_valid(monkeypatch):
    version_string = "1.2.3-alpha.1+build.123"
    semver = SemanticVersion("0.0.0")
    
    semver.parse(version_string)
    
    assert semver.major == 1
    assert semver.minor == 2
    assert semver.patch == 3
    assert semver.prerelease == ('alpha', 1)
    assert semver.buildmetadata == ('build', 123)

def test_semantic_version_parse_no_prerelease(monkeypatch):
    version_string = "1.2.3+build.123"
    semver = SemanticVersion("0.0.0")
    
    semver.parse(version_string)
    
    assert semver.major == 1
    assert semver.minor == 2
    assert semver.patch == 3
    assert semver.prerelease == ()
    assert semver.buildmetadata == ('build', 123)

def test_semantic_version_parse_no_buildmetadata(monkeypatch):
    version_string = "1.2.3-alpha.1"
    semver = SemanticVersion("0.0.0")
    
    semver.parse(version_string)
    
    assert semver.major == 1
    assert semver.minor == 2
    assert semver.patch == 3
    assert semver.prerelease == ('alpha', 1)
    assert semver.buildmetadata == ()

def test_semantic_version_parse_invalid(monkeypatch):
    version_string = "invalid.version.string"
    semver = SemanticVersion("0.0.0")
    
    with pytest.raises(ValueError, match="invalid semantic version 'invalid.version.string'"):
        semver.parse(version_string)
