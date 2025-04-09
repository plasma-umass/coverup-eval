# file: lib/ansible/utils/version.py:221-251
# asked: {"lines": [244], "branches": [[243, 244]]}
# gained: {"lines": [244], "branches": [[243, 244]]}

import pytest
from ansible.utils.version import SemanticVersion

def test_cmp_with_prerelease_greater():
    v1 = SemanticVersion("1.0.0-alpha")
    v2 = SemanticVersion("1.0.0-beta")
    assert v1._cmp(v2) == -1
    assert v2._cmp(v1) == 1

def test_cmp_with_prerelease_equal():
    v1 = SemanticVersion("1.0.0-alpha")
    v2 = SemanticVersion("1.0.0-alpha")
    assert v1._cmp(v2) == 0
    assert v2._cmp(v1) == 0

def test_cmp_with_prerelease_and_core_different():
    v1 = SemanticVersion("1.0.0-alpha")
    v2 = SemanticVersion("1.0.1-alpha")
    assert v1._cmp(v2) == -1
    assert v2._cmp(v1) == 1

def test_cmp_with_no_prerelease():
    v1 = SemanticVersion("1.0.0")
    v2 = SemanticVersion("1.0.0")
    assert v1._cmp(v2) == 0
    assert v2._cmp(v1) == 0

def test_cmp_with_core_different():
    v1 = SemanticVersion("1.0.0")
    v2 = SemanticVersion("2.0.0")
    assert v1._cmp(v2) == -1
    assert v2._cmp(v1) == 1

def test_cmp_with_string_input():
    v1 = SemanticVersion("1.0.0")
    v2 = "2.0.0"
    assert v1._cmp(v2) == -1
    assert SemanticVersion(v2)._cmp(v1) == 1
