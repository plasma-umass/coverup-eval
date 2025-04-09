# file: lib/ansible/utils/version.py:221-251
# asked: {"lines": [221, 222, 223, 225, 228, 229, 231, 233, 234, 236, 237, 238, 239, 241, 242, 243, 244, 251], "branches": [[222, 223], [222, 225], [225, 228], [225, 233], [228, 229], [228, 231], [233, 234], [233, 236], [236, 237], [236, 238], [238, 239], [238, 241], [241, 242], [241, 243], [243, 244], [243, 251]]}
# gained: {"lines": [221, 222, 223, 225, 228, 229, 231, 233, 234, 236, 237, 238, 239, 241, 242, 243, 244, 251], "branches": [[222, 223], [222, 225], [225, 228], [225, 233], [228, 229], [228, 231], [233, 234], [233, 236], [236, 237], [236, 238], [238, 239], [238, 241], [241, 242], [241, 243], [243, 244], [243, 251]]}

import pytest
from ansible.utils.version import SemanticVersion

def test_cmp_with_string():
    v1 = SemanticVersion("1.0.0")
    assert v1._cmp("1.0.0") == 0
    assert v1._cmp("2.0.0") == -1
    assert v1._cmp("0.1.0") == 1

def test_cmp_with_core_version():
    v1 = SemanticVersion("1.0.0")
    v2 = SemanticVersion("2.0.0")
    v3 = SemanticVersion("0.1.0")
    assert v1._cmp(v2) == -1
    assert v1._cmp(v3) == 1
    assert v1._cmp(v1) == 0

def test_cmp_with_prerelease():
    v1 = SemanticVersion("1.0.0-alpha")
    v2 = SemanticVersion("1.0.0-beta")
    v3 = SemanticVersion("1.0.0")
    assert v1._cmp(v2) == -1
    assert v2._cmp(v1) == 1
    assert v1._cmp(v3) == -1
    assert v3._cmp(v1) == 1

def test_cmp_with_equal_prerelease():
    v1 = SemanticVersion("1.0.0-alpha")
    v2 = SemanticVersion("1.0.0-alpha")
    assert v1._cmp(v2) == 0

def test_cmp_with_build_metadata():
    v1 = SemanticVersion("1.0.0+build1")
    v2 = SemanticVersion("1.0.0+build2")
    assert v1._cmp(v2) == 0
