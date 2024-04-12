# file lib/ansible/module_utils/compat/version.py:158-167
# lines [158, 159, 160, 162, 164, 165, 167]
# branches ['159->160', '159->162', '164->165', '164->167']

import pytest
from ansible.module_utils.compat.version import StrictVersion

def test_strict_version_str_with_prerelease():
    strict_version = StrictVersion()
    strict_version.version = (1, 2, 3)
    strict_version.prerelease = ('a', 4)
    result = str(strict_version)
    assert result == '1.2.3a4', "The __str__ method should return '1.2.3a4' with prerelease"

def test_strict_version_str_without_prerelease_and_patch_version_zero():
    strict_version = StrictVersion()
    strict_version.version = (1, 2, 0)
    strict_version.prerelease = None
    result = str(strict_version)
    assert result == '1.2', "The __str__ method should return '1.2' when patch version is zero and no prerelease"

def test_strict_version_str_without_prerelease_and_non_zero_patch():
    strict_version = StrictVersion()
    strict_version.version = (1, 2, 3)
    strict_version.prerelease = None
    result = str(strict_version)
    assert result == '1.2.3', "The __str__ method should return '1.2.3' when patch version is non-zero and no prerelease"
