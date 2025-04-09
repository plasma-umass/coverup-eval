# file: lib/ansible/utils/version.py:262-263
# asked: {"lines": [262, 263], "branches": []}
# gained: {"lines": [262, 263], "branches": []}

import pytest
from ansible.utils.version import SemanticVersion
from packaging.version import Version

@pytest.fixture
def version_a():
    return SemanticVersion("1.0.0")

@pytest.fixture
def version_b():
    return SemanticVersion("2.0.0")

def test_semantic_version_lt(version_a, version_b):
    assert version_a < version_b

def test_semantic_version_not_lt(version_b, version_a):
    assert not (version_b < version_a)

def test_semantic_version_equal(version_a):
    version_c = SemanticVersion("1.0.0")
    assert not (version_a < version_c)
    assert not (version_c < version_a)
