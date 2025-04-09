# file: lib/ansible/utils/version.py:191-204
# asked: {"lines": [194], "branches": [[193, 194]]}
# gained: {"lines": [194], "branches": [[193, 194]]}

import pytest
from ansible.utils.version import SemanticVersion

def test_invalid_semantic_version():
    with pytest.raises(ValueError, match="invalid semantic version '1.0'"):
        SemanticVersion("1.0")

def test_valid_semantic_version():
    version = SemanticVersion("1.0.0")
    assert version.major == 1
    assert version.minor == 0
    assert version.patch == 0
    assert version.prerelease == ()
    assert version.buildmetadata == ()
