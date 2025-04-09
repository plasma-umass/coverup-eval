# file: lib/ansible/utils/version.py:256-257
# asked: {"lines": [256, 257], "branches": []}
# gained: {"lines": [256, 257], "branches": []}

import pytest
from ansible.utils.version import SemanticVersion
from packaging.version import Version

@pytest.fixture
def version_a():
    return SemanticVersion("1.0.0")

@pytest.fixture
def version_b():
    return SemanticVersion("1.0.0")

@pytest.fixture
def version_c():
    return SemanticVersion("2.0.0")

def test_semantic_version_eq(version_a, version_b, version_c):
    # Test equality
    assert version_a == version_b
    assert not (version_a == version_c)

def test_semantic_version_not_eq(version_a, version_c):
    # Test inequality
    assert version_a != version_c
    assert not (version_a != version_a)
