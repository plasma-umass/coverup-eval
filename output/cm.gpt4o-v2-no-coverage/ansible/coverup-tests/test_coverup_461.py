# file: lib/ansible/module_utils/compat/version.py:158-167
# asked: {"lines": [158, 159, 160, 162, 164, 165, 167], "branches": [[159, 160], [159, 162], [164, 165], [164, 167]]}
# gained: {"lines": [158, 159, 160, 162, 164, 165, 167], "branches": [[159, 160], [159, 162], [164, 165], [164, 167]]}

import pytest
from ansible.module_utils.compat.version import StrictVersion, Version

class MockVersion(Version):
    def __init__(self, version, prerelease=None):
        self.version = version
        self.prerelease = prerelease

@pytest.fixture
def mock_version_zero():
    return MockVersion([1, 2, 0])

@pytest.fixture
def mock_version_non_zero():
    return MockVersion([1, 2, 3])

@pytest.fixture
def mock_version_prerelease():
    return MockVersion([1, 2, 3], ('a', 1))

def test_strict_version_str_zero(mock_version_zero):
    sv = StrictVersion.__new__(StrictVersion)
    sv.version = mock_version_zero.version
    sv.prerelease = mock_version_zero.prerelease
    assert str(sv) == "1.2"

def test_strict_version_str_non_zero(mock_version_non_zero):
    sv = StrictVersion.__new__(StrictVersion)
    sv.version = mock_version_non_zero.version
    sv.prerelease = mock_version_non_zero.prerelease
    assert str(sv) == "1.2.3"

def test_strict_version_str_prerelease(mock_version_prerelease):
    sv = StrictVersion.__new__(StrictVersion)
    sv.version = mock_version_prerelease.version
    sv.prerelease = mock_version_prerelease.prerelease
    assert str(sv) == "1.2.3a1"
