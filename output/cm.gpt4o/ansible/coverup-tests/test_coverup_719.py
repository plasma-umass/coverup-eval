# file lib/ansible/utils/version.py:210-212
# lines [210, 211, 212]
# branches []

import pytest
from ansible.utils.version import Version
from packaging.version import Version as PackagingVersion

class TestSemanticVersion:
    def test_is_prerelease(self):
        class SemanticVersion(Version):
            def __init__(self, vstring=None):
                if vstring:
                    self._version = PackagingVersion(vstring)
            
            @property
            def is_prerelease(self):
                return bool(self._version.pre)

        # Create a mock version with a prerelease
        version_with_prerelease = SemanticVersion("1.0.0-alpha")
        assert version_with_prerelease.is_prerelease is True

        # Create a mock version without a prerelease
        version_without_prerelease = SemanticVersion("1.0.0")
        assert version_without_prerelease.is_prerelease is False
