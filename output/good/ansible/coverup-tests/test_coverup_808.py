# file lib/ansible/utils/version.py:128-135
# lines [128, 129, 134]
# branches []

import pytest
from ansible.utils.version import SemanticVersion
import re

# Assuming SEMVER_RE is a regular expression defined in the same module
# that matches semantic version strings, e.g., "1.0.0", "2.1.0-alpha", etc.

def test_semantic_version_comparison(mocker):
    # Mock the SEMVER_RE to a simple regex for testing purposes
    # The regex must have named groups to match the expected groups in the original SEMVER_RE
    mocker.patch('ansible.utils.version.SEMVER_RE', new=re.compile(
        r'^(?P<major>\d+)\.(?P<minor>\d+)\.(?P<patch>\d+)(?:-(?P<prerelease>[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*))?(?:\+(?P<buildmetadata>[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*))?$'
    ))

    # Create instances of SemanticVersion
    v1 = SemanticVersion('1.0.0')
    v2 = SemanticVersion('2.0.0')

    # Test the comparison operations
    assert v1 < v2, "v1 should be less than v2"
    assert v2 > v1, "v2 should be greater than v1"
    assert v1 != v2, "v1 should not be equal to v2"
    assert v1 == SemanticVersion('1.0.0'), "v1 should be equal to another instance of v1"

    # Cleanup is handled by pytest-mock through the mocker fixture
