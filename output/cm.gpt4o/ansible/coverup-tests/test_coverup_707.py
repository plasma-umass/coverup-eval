# file lib/ansible/utils/version.py:206-208
# lines [206, 207, 208]
# branches []

import pytest
from ansible.utils.version import SemanticVersion

def test_semantic_version_core():
    # Create a mock version object with major, minor, and patch attributes
    class MockVersion:
        major = 1
        minor = 2
        patch = 3

    # Create an instance of SemanticVersion using the mock version
    version = SemanticVersion()
    version.major = MockVersion.major
    version.minor = MockVersion.minor
    version.patch = MockVersion.patch

    # Assert that the core property returns the correct tuple
    assert version.core == (1, 2, 3)
