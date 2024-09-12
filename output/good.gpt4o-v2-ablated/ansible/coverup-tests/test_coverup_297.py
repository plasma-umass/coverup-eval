# file: lib/ansible/utils/version.py:214-219
# asked: {"lines": [214, 215, 219], "branches": []}
# gained: {"lines": [214, 215, 219], "branches": []}

import pytest
from ansible.utils.version import SemanticVersion

@pytest.fixture
def version_factory():
    def _create_version(major, minor, patch, prerelease=None):
        class MockVersion(SemanticVersion):
            def __init__(self, major, minor, patch, prerelease):
                self.major = major
                self.minor = minor
                self.patch = patch
                self.prerelease = prerelease

            @property
            def is_prerelease(self):
                return self.prerelease is not None

        return MockVersion(major, minor, patch, prerelease)
    return _create_version

def test_is_stable_major_zero(version_factory):
    version = version_factory(0, 1, 0)
    assert not version.is_stable

def test_is_stable_prerelease(version_factory):
    version = version_factory(1, 0, 0, prerelease='alpha')
    assert not version.is_stable

def test_is_stable_stable_version(version_factory):
    version = version_factory(1, 0, 0)
    assert version.is_stable
