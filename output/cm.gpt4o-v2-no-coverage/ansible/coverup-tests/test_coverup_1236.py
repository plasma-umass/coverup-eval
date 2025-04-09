# file: lib/ansible/utils/version.py:271-272
# asked: {"lines": [272], "branches": []}
# gained: {"lines": [272], "branches": []}

import pytest
from ansible.utils.version import SemanticVersion

def test_semantic_version_ge():
    v1 = SemanticVersion("1.0.0")
    v2 = SemanticVersion("2.0.0")
    v3 = SemanticVersion("1.0.0-alpha")
    v4 = SemanticVersion("1.0.0-beta")

    assert v2 >= v1
    assert v1 >= v1
    assert not (v1 >= v2)
    assert v1 >= v3
    assert v4 >= v3
    assert not (v3 >= v4)

def test_semantic_version_cmp():
    v1 = SemanticVersion("1.0.0")
    v2 = SemanticVersion("2.0.0")
    v3 = SemanticVersion("1.0.0-alpha")
    v4 = SemanticVersion("1.0.0-beta")

    assert v1._cmp(v2) == -1
    assert v2._cmp(v1) == 1
    assert v1._cmp(v1) == 0
    assert v1._cmp(v3) == 1
    assert v3._cmp(v1) == -1
    assert v3._cmp(v4) == -1
    assert v4._cmp(v3) == 1
    assert v4._cmp(v4) == 0

