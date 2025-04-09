# file: lib/ansible/module_utils/compat/version.py:169-203
# asked: {"lines": [169, 170, 171, 172, 173, 175, 178, 179, 181, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 201, 203], "branches": [[170, 171], [170, 172], [172, 173], [172, 175], [175, 178], [175, 189], [178, 179], [178, 181], [189, 190], [189, 191], [191, 192], [191, 193], [193, 194], [193, 195], [195, 196], [195, 203], [196, 197], [196, 198], [198, 199], [198, 201]]}
# gained: {"lines": [169, 170, 171, 172, 173, 175, 178, 179, 181, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 201], "branches": [[170, 171], [170, 172], [172, 173], [172, 175], [175, 178], [175, 189], [178, 179], [178, 181], [189, 190], [189, 191], [191, 192], [191, 193], [193, 194], [193, 195], [195, 196], [196, 197], [196, 198], [198, 199], [198, 201]]}

import pytest
from ansible.module_utils.compat.version import StrictVersion

def test_cmp_with_string(monkeypatch):
    v1 = StrictVersion("1.0")
    v2 = "1.0"
    assert v1._cmp(v2) == 0

def test_cmp_with_non_strict_version(monkeypatch):
    class DummyVersion:
        pass

    v1 = StrictVersion("1.0")
    v2 = DummyVersion()
    assert v1._cmp(v2) == NotImplemented

def test_cmp_version_less(monkeypatch):
    v1 = StrictVersion("1.0")
    v2 = StrictVersion("2.0")
    assert v1._cmp(v2) == -1

def test_cmp_version_greater(monkeypatch):
    v1 = StrictVersion("2.0")
    v2 = StrictVersion("1.0")
    assert v1._cmp(v2) == 1

def test_cmp_no_prerelease(monkeypatch):
    v1 = StrictVersion("1.0")
    v2 = StrictVersion("1.0")
    assert v1._cmp(v2) == 0

def test_cmp_self_prerelease_other_not(monkeypatch):
    v1 = StrictVersion("1.0a1")
    v2 = StrictVersion("1.0")
    assert v1._cmp(v2) == -1

def test_cmp_self_not_prerelease_other(monkeypatch):
    v1 = StrictVersion("1.0")
    v2 = StrictVersion("1.0a1")
    assert v1._cmp(v2) == 1

def test_cmp_both_prerelease_equal(monkeypatch):
    v1 = StrictVersion("1.0a1")
    v2 = StrictVersion("1.0a1")
    assert v1._cmp(v2) == 0

def test_cmp_both_prerelease_less(monkeypatch):
    v1 = StrictVersion("1.0a1")
    v2 = StrictVersion("1.0a2")
    assert v1._cmp(v2) == -1

def test_cmp_both_prerelease_greater(monkeypatch):
    v1 = StrictVersion("1.0a2")
    v2 = StrictVersion("1.0a1")
    assert v1._cmp(v2) == 1
