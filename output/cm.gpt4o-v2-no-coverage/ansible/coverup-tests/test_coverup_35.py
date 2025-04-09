# file: lib/ansible/module_utils/compat/version.py:169-203
# asked: {"lines": [169, 170, 171, 172, 173, 175, 178, 179, 181, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 201, 203], "branches": [[170, 171], [170, 172], [172, 173], [172, 175], [175, 178], [175, 189], [178, 179], [178, 181], [189, 190], [189, 191], [191, 192], [191, 193], [193, 194], [193, 195], [195, 196], [195, 203], [196, 197], [196, 198], [198, 199], [198, 201]]}
# gained: {"lines": [169, 170, 171, 172, 173, 175, 178, 179, 181, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 201], "branches": [[170, 171], [170, 172], [172, 173], [172, 175], [175, 178], [175, 189], [178, 179], [178, 181], [189, 190], [189, 191], [191, 192], [191, 193], [193, 194], [193, 195], [195, 196], [196, 197], [196, 198], [198, 199], [198, 201]]}

import pytest
from ansible.module_utils.compat.version import StrictVersion

def test_cmp_with_string():
    v1 = StrictVersion("1.0")
    assert v1._cmp("1.0") == 0
    assert v1._cmp("1.1") == -1
    assert v1._cmp("0.9") == 1

def test_cmp_with_strictversion():
    v1 = StrictVersion("1.0")
    v2 = StrictVersion("1.0")
    v3 = StrictVersion("1.1")
    v4 = StrictVersion("0.9")
    assert v1._cmp(v2) == 0
    assert v1._cmp(v3) == -1
    assert v1._cmp(v4) == 1

def test_cmp_with_invalid_type():
    v1 = StrictVersion("1.0")
    assert v1._cmp(1.0) == NotImplemented

def test_cmp_with_prerelease():
    v1 = StrictVersion("1.0a1")
    v2 = StrictVersion("1.0")
    v3 = StrictVersion("1.0a2")
    v4 = StrictVersion("1.0b1")
    assert v1._cmp(v2) == -1
    assert v2._cmp(v1) == 1
    assert v1._cmp(v3) == -1
    assert v3._cmp(v1) == 1
    assert v3._cmp(v4) == -1
    assert v4._cmp(v3) == 1
    assert v1._cmp(v1) == 0

def test_cmp_with_both_prerelease():
    v1 = StrictVersion("1.0a1")
    v2 = StrictVersion("1.0a1")
    v3 = StrictVersion("1.0a2")
    v4 = StrictVersion("1.0b1")
    assert v1._cmp(v2) == 0
    assert v1._cmp(v3) == -1
    assert v3._cmp(v1) == 1
    assert v3._cmp(v4) == -1
    assert v4._cmp(v3) == 1
