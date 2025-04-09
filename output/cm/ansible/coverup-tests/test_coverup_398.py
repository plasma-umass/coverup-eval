# file lib/ansible/utils/version.py:136-145
# lines [136, 137, 138, 139, 140, 141, 142, 144, 145]
# branches ['144->exit', '144->145']

import pytest
from ansible.utils.version import SemanticVersion

# Test function to cover the missing lines in SemanticVersion.__init__
def test_semantic_version_initialization():
    # Test with a valid version string
    version_str = "1.2.3-alpha.1+build.123"
    version = SemanticVersion(version_str)
    assert version.vstring == version_str
    assert version.major == 1
    assert version.minor == 2
    assert version.patch == 3
    assert version.prerelease == ('alpha', 1)
    assert version.buildmetadata == ('build', 123)

    # Test with an empty version string
    empty_version = SemanticVersion("")
    assert empty_version.vstring == ""
    assert empty_version.major is None
    assert empty_version.minor is None
    assert empty_version.patch is None
    assert empty_version.prerelease == ()
    assert empty_version.buildmetadata == ()

    # Test with None as version string
    none_version = SemanticVersion(None)
    assert none_version.vstring is None
    assert none_version.major is None
    assert none_version.minor is None
    assert none_version.patch is None
    assert none_version.prerelease == ()
    assert none_version.buildmetadata == ()

# Note: The actual parsing logic is not implemented in the provided code snippet.
# The test assumes that the parse method sets the major, minor, patch, prerelease,
# and buildmetadata attributes correctly based on the provided version string.
# If the parse method is not implemented, the test will fail as the attributes
# will not be set. The test is designed based on the assumption that the parse
# method works as expected.
