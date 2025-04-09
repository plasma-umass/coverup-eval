# file: lib/ansible/utils/version.py:191-204
# asked: {"lines": [191, 192, 193, 194, 196, 197, 198, 199, 201, 202, 203, 204], "branches": [[193, 194], [193, 196], [201, 202], [201, 203], [203, 0], [203, 204]]}
# gained: {"lines": [191, 192, 193, 194, 196, 197, 198, 199, 201, 202, 203, 204], "branches": [[193, 194], [193, 196], [201, 202], [201, 203], [203, 0], [203, 204]]}

import pytest
from ansible.utils.version import SemanticVersion, _Numeric, _Alpha
import re

SEMVER_RE = re.compile(
    r"""
    ^
        (?P<major>0|[1-9]\d*)
        \.
        (?P<minor>0|[1-9]\d*)
        \.
        (?P<patch>0|[1-9]\d*)
        (?: 
            -
            (?P<prerelease>
                (?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)
                (?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*
            )
        )?
        (?: 
            \+
            (?P<buildmetadata>[0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*)
        )?
    $
    """, re.VERBOSE
)

class TestSemanticVersion:
    def test_parse_valid_version(self):
        version = SemanticVersion("1.2.3")
        assert version.major == 1
        assert version.minor == 2
        assert version.patch == 3

    def test_parse_invalid_version(self):
        with pytest.raises(ValueError, match="invalid semantic version '1.2'"):
            SemanticVersion("1.2")

    def test_parse_with_prerelease(self):
        version = SemanticVersion("1.2.3-alpha.1")
        assert version.prerelease == (_Alpha("alpha"), _Numeric("1"))

    def test_parse_with_buildmetadata(self):
        version = SemanticVersion("1.2.3+build.123")
        assert version.buildmetadata == (_Alpha("build"), _Numeric("123"))

    def test_parse_with_prerelease_and_buildmetadata(self):
        version = SemanticVersion("1.2.3-alpha.1+build.123")
        assert version.prerelease == (_Alpha("alpha"), _Numeric("1"))
        assert version.buildmetadata == (_Alpha("build"), _Numeric("123"))
