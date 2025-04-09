# file: lib/ansible/utils/version.py:210-212
# asked: {"lines": [210, 211, 212], "branches": []}
# gained: {"lines": [210, 211, 212], "branches": []}

import pytest
from ansible.utils.version import SemanticVersion
from packaging.version import Version

@pytest.fixture
def version_factory():
    def _create_version(version_str):
        return SemanticVersion(version_str)
    return _create_version

def test_is_prerelease_true(version_factory):
    version = version_factory("1.0.0-alpha")
    assert version.is_prerelease is True

def test_is_prerelease_false(version_factory):
    version = version_factory("1.0.0")
    assert version.is_prerelease is False
