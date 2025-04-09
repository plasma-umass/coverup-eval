# file: lib/ansible/utils/version.py:221-251
# asked: {"lines": [221, 222, 223, 225, 228, 229, 231, 233, 234, 236, 237, 238, 239, 241, 242, 243, 244, 251], "branches": [[222, 223], [222, 225], [225, 228], [225, 233], [228, 229], [228, 231], [233, 234], [233, 236], [236, 237], [236, 238], [238, 239], [238, 241], [241, 242], [241, 243], [243, 244], [243, 251]]}
# gained: {"lines": [221, 222, 223, 225, 228, 229, 233, 234, 236, 237, 238, 239, 241, 242, 243, 251], "branches": [[222, 223], [222, 225], [225, 228], [225, 233], [228, 229], [233, 234], [233, 236], [236, 237], [236, 238], [238, 239], [238, 241], [241, 242], [241, 243], [243, 251]]}

import pytest
from ansible.utils.version import SemanticVersion

def test_cmp_with_string():
    v1 = SemanticVersion("1.0.0")
    result = v1._cmp("1.0.1")
    assert result == -1

def test_cmp_core_not_equal():
    v1 = SemanticVersion("1.0.0")
    v2 = SemanticVersion("2.0.0")
    result = v1._cmp(v2)
    assert result == -1

def test_cmp_core_equal_prerelease_none():
    v1 = SemanticVersion("1.0.0")
    v2 = SemanticVersion("1.0.0")
    result = v1._cmp(v2)
    assert result == 0

def test_cmp_prerelease_self_only():
    v1 = SemanticVersion("1.0.0-alpha")
    v2 = SemanticVersion("1.0.0")
    result = v1._cmp(v2)
    assert result == -1

def test_cmp_prerelease_other_only():
    v1 = SemanticVersion("1.0.0")
    v2 = SemanticVersion("1.0.0-alpha")
    result = v1._cmp(v2)
    assert result == 1

def test_cmp_prerelease_both():
    v1 = SemanticVersion("1.0.0-alpha")
    v2 = SemanticVersion("1.0.0-beta")
    result = v1._cmp(v2)
    assert result == -1

def test_cmp_prerelease_equal():
    v1 = SemanticVersion("1.0.0-alpha")
    v2 = SemanticVersion("1.0.0-alpha")
    result = v1._cmp(v2)
    assert result == 0
