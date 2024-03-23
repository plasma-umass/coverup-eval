# file lib/ansible/utils/version.py:214-219
# lines [219]
# branches []

import pytest
from ansible.utils.version import SemanticVersion

@pytest.fixture
def cleanup():
    # Fixture to perform cleanup if necessary
    yield
    # Perform cleanup here if needed

def test_semantic_version_is_stable(cleanup):
    # Test for stable version
    stable_version = SemanticVersion('1.0.0')
    assert stable_version.is_stable is True

    # Test for unstable version due to major version being 0
    unstable_version_major_zero = SemanticVersion('0.1.0')
    assert unstable_version_major_zero.is_stable is False

    # Test for unstable version due to prerelease
    unstable_version_prerelease = SemanticVersion('1.0.0-alpha')
    assert unstable_version_prerelease.is_stable is False
