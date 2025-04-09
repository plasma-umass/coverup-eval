# file: lib/ansible/module_utils/compat/version.py:169-203
# asked: {"lines": [181, 194, 197, 201, 203], "branches": [[178, 181], [193, 194], [195, 203], [196, 197], [198, 201]]}
# gained: {"lines": [181, 194, 197, 201], "branches": [[178, 181], [193, 194], [196, 197], [198, 201]]}

import pytest
from ansible.module_utils.compat.version import StrictVersion

def test_cmp_numeric_versions():
    v1 = StrictVersion("1.0")
    v2 = StrictVersion("2.0")
    assert v1._cmp(v2) == -1
    assert v2._cmp(v1) == 1

def test_cmp_prerelease_versions():
    v1 = StrictVersion("1.0a1")
    v2 = StrictVersion("1.0")
    assert v1._cmp(v2) == -1
    assert v2._cmp(v1) == 1

def test_cmp_equal_versions():
    v1 = StrictVersion("1.0")
    v2 = StrictVersion("1.0")
    assert v1._cmp(v2) == 0

def test_cmp_equal_prerelease_versions():
    v1 = StrictVersion("1.0a1")
    v2 = StrictVersion("1.0a1")
    assert v1._cmp(v2) == 0

def test_cmp_different_prerelease_versions():
    v1 = StrictVersion("1.0a1")
    v2 = StrictVersion("1.0a2")
    assert v1._cmp(v2) == -1
    assert v2._cmp(v1) == 1

def test_cmp_non_version():
    v1 = StrictVersion("1.0")
    assert v1._cmp("1.0") == 0
    assert v1._cmp("2.0") == -1
    assert v1._cmp("0.5") == 1
    assert v1._cmp(StrictVersion("1.0")) == 0

def test_cmp_invalid_type():
    v1 = StrictVersion("1.0")
    assert v1._cmp(1.0) == NotImplemented
