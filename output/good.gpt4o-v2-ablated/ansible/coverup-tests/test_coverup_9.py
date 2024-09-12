# file: lib/ansible/module_utils/compat/version.py:169-203
# asked: {"lines": [169, 170, 171, 172, 173, 175, 178, 179, 181, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 201, 203], "branches": [[170, 171], [170, 172], [172, 173], [172, 175], [175, 178], [175, 189], [178, 179], [178, 181], [189, 190], [189, 191], [191, 192], [191, 193], [193, 194], [193, 195], [195, 196], [195, 203], [196, 197], [196, 198], [198, 199], [198, 201]]}
# gained: {"lines": [169, 170, 171, 172, 173, 175, 178, 179, 181, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 201], "branches": [[170, 171], [170, 172], [172, 173], [172, 175], [175, 178], [175, 189], [178, 179], [178, 181], [189, 190], [189, 191], [191, 192], [191, 193], [193, 194], [193, 195], [195, 196], [196, 197], [196, 198], [198, 199], [198, 201]]}

import pytest
from ansible.module_utils.compat.version import StrictVersion

class TestStrictVersion:
    def test_cmp_with_string(self):
        v1 = StrictVersion("1.0")
        v2 = "1.0"
        assert v1._cmp(v2) == 0

    def test_cmp_with_strictversion(self):
        v1 = StrictVersion("1.0")
        v2 = StrictVersion("1.0")
        assert v1._cmp(v2) == 0

    def test_cmp_with_non_strictversion(self):
        v1 = StrictVersion("1.0")
        v2 = 1.0
        assert v1._cmp(v2) == NotImplemented

    def test_cmp_version_less_than(self):
        v1 = StrictVersion("1.0")
        v2 = StrictVersion("2.0")
        assert v1._cmp(v2) == -1

    def test_cmp_version_greater_than(self):
        v1 = StrictVersion("2.0")
        v2 = StrictVersion("1.0")
        assert v1._cmp(v2) == 1

    def test_cmp_prerelease_equal(self, monkeypatch):
        v1 = StrictVersion("1.0a1")
        v2 = StrictVersion("1.0a1")
        monkeypatch.setattr(v1, 'prerelease', ('a', 1))
        monkeypatch.setattr(v2, 'prerelease', ('a', 1))
        assert v1._cmp(v2) == 0

    def test_cmp_prerelease_self_less_than(self, monkeypatch):
        v1 = StrictVersion("1.0a1")
        v2 = StrictVersion("1.0a2")
        monkeypatch.setattr(v1, 'prerelease', ('a', 1))
        monkeypatch.setattr(v2, 'prerelease', ('a', 2))
        assert v1._cmp(v2) == -1

    def test_cmp_prerelease_self_greater_than(self, monkeypatch):
        v1 = StrictVersion("1.0a2")
        v2 = StrictVersion("1.0a1")
        monkeypatch.setattr(v1, 'prerelease', ('a', 2))
        monkeypatch.setattr(v2, 'prerelease', ('a', 1))
        assert v1._cmp(v2) == 1

    def test_cmp_self_prerelease_other_not(self, monkeypatch):
        v1 = StrictVersion("1.0a1")
        v2 = StrictVersion("1.0")
        monkeypatch.setattr(v1, 'prerelease', ('a', 1))
        monkeypatch.setattr(v2, 'prerelease', None)
        assert v1._cmp(v2) == -1

    def test_cmp_self_not_prerelease_other(self, monkeypatch):
        v1 = StrictVersion("1.0")
        v2 = StrictVersion("1.0a1")
        monkeypatch.setattr(v1, 'prerelease', None)
        monkeypatch.setattr(v2, 'prerelease', ('a', 1))
        assert v1._cmp(v2) == 1
