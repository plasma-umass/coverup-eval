# file: lib/ansible/module_utils/compat/version.py:158-167
# asked: {"lines": [158, 159, 160, 162, 164, 165, 167], "branches": [[159, 160], [159, 162], [164, 165], [164, 167]]}
# gained: {"lines": [158, 159, 160, 162, 164, 165, 167], "branches": [[159, 160], [159, 162], [164, 165], [164, 167]]}

import pytest
from ansible.module_utils.compat.version import StrictVersion

@pytest.mark.parametrize("version, expected", [
    ((1, 0, 0), "1.0"),
    ((1, 2, 0), "1.2"),
    ((1, 2, 3), "1.2.3"),
    ((1, 2, 3), "1.2.3"),
])
def test_strict_version_str(version, expected):
    v = StrictVersion()
    v.version = version
    v.prerelease = None
    assert str(v) == expected

@pytest.mark.parametrize("version, prerelease, expected", [
    ((1, 2, 0), ('a', 1), "1.2a1"),
    ((1, 2, 3), ('b', 2), "1.2.3b2"),
])
def test_strict_version_str_with_prerelease(version, prerelease, expected):
    v = StrictVersion()
    v.version = version
    v.prerelease = prerelease
    assert str(v) == expected
