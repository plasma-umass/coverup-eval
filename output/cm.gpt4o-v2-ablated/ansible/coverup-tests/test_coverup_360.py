# file: lib/ansible/utils/version.py:265-266
# asked: {"lines": [265, 266], "branches": []}
# gained: {"lines": [265, 266], "branches": []}

import pytest
from ansible.utils.version import SemanticVersion
from packaging.version import Version

@pytest.fixture
def version_1():
    return SemanticVersion("1.0.0")

@pytest.fixture
def version_2():
    return SemanticVersion("2.0.0")

def test_semantic_version_le(version_1, version_2):
    assert version_1 <= version_2
    assert not (version_2 <= version_1)

def test_semantic_version_le_equal(version_1):
    version_1_copy = SemanticVersion("1.0.0")
    assert version_1 <= version_1_copy
    assert version_1_copy <= version_1
