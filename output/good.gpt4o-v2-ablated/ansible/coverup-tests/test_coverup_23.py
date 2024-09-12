# file: lib/ansible/utils/version.py:221-251
# asked: {"lines": [221, 222, 223, 225, 228, 229, 231, 233, 234, 236, 237, 238, 239, 241, 242, 243, 244, 251], "branches": [[222, 223], [222, 225], [225, 228], [225, 233], [228, 229], [228, 231], [233, 234], [233, 236], [236, 237], [236, 238], [238, 239], [238, 241], [241, 242], [241, 243], [243, 244], [243, 251]]}
# gained: {"lines": [221, 222, 223, 225, 228, 229, 231, 233, 234, 236, 237, 238, 239, 241, 242, 243, 244, 251], "branches": [[222, 223], [222, 225], [225, 228], [225, 233], [228, 229], [228, 231], [233, 234], [233, 236], [236, 237], [236, 238], [238, 239], [238, 241], [241, 242], [241, 243], [243, 244], [243, 251]]}

import pytest
from ansible.utils.version import SemanticVersion

@pytest.mark.parametrize("version1, version2, expected", [
    ("1.0.0", "1.0.0", 0),
    ("1.0.0", "1.0.1", -1),
    ("1.0.1", "1.0.0", 1),
    ("1.0.0-alpha", "1.0.0", -1),
    ("1.0.0", "1.0.0-alpha", 1),
    ("1.0.0-alpha", "1.0.0-beta", -1),
    ("1.0.0-beta", "1.0.0-alpha", 1),
    ("1.0.0-alpha.1", "1.0.0-alpha.2", -1),
    ("1.0.0-alpha.2", "1.0.0-alpha.1", 1),
    ("1.0.0+build1", "1.0.0+build2", 0),
    ("1.0.0-alpha+build1", "1.0.0-alpha+build2", 0),
])
def test_semantic_version_cmp(version1, version2, expected):
    v1 = SemanticVersion(version1)
    v2 = SemanticVersion(version2)
    assert v1._cmp(v2) == expected

@pytest.mark.parametrize("version1, version2, expected", [
    ("1.0.0", "1.0.0", 0),
    ("1.0.0", "1.0.1", -1),
    ("1.0.1", "1.0.0", 1),
    ("1.0.0-alpha", "1.0.0", -1),
    ("1.0.0", "1.0.0-alpha", 1),
    ("1.0.0-alpha", "1.0.0-beta", -1),
    ("1.0.0-beta", "1.0.0-alpha", 1),
    ("1.0.0-alpha.1", "1.0.0-alpha.2", -1),
    ("1.0.0-alpha.2", "1.0.0-alpha.1", 1),
    ("1.0.0+build1", "1.0.0+build2", 0),
    ("1.0.0-alpha+build1", "1.0.0-alpha+build2", 0),
])
def test_semantic_version_cmp_str(version1, version2, expected):
    v1 = SemanticVersion(version1)
    assert v1._cmp(version2) == expected
