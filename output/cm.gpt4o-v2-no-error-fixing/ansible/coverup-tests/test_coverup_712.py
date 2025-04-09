# file: lib/ansible/module_utils/compat/version.py:169-203
# asked: {"lines": [170, 171, 172, 173, 175, 178, 179, 181, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 201, 203], "branches": [[170, 171], [170, 172], [172, 173], [172, 175], [175, 178], [175, 189], [178, 179], [178, 181], [189, 190], [189, 191], [191, 192], [191, 193], [193, 194], [193, 195], [195, 196], [195, 203], [196, 197], [196, 198], [198, 199], [198, 201]]}
# gained: {"lines": [170, 171, 172, 173, 175, 178, 179, 189, 190, 191, 192, 193, 195, 196, 198, 199], "branches": [[170, 171], [170, 172], [172, 173], [172, 175], [175, 178], [175, 189], [178, 179], [189, 190], [189, 191], [191, 192], [191, 193], [193, 195], [195, 196], [196, 198], [198, 199]]}

import pytest
from ansible.module_utils.compat.version import StrictVersion

def test_cmp_with_string():
    v1 = StrictVersion("1.0")
    result = v1._cmp("1.0")
    assert result == 0

def test_cmp_with_strictversion():
    v1 = StrictVersion("1.0")
    v2 = StrictVersion("1.0")
    result = v1._cmp(v2)
    assert result == 0

def test_cmp_with_different_versions():
    v1 = StrictVersion("1.0")
    v2 = StrictVersion("1.1")
    result = v1._cmp(v2)
    assert result == -1

def test_cmp_with_prerelease():
    v1 = StrictVersion("1.0a1")
    v2 = StrictVersion("1.0")
    result = v1._cmp(v2)
    assert result == -1

def test_cmp_with_both_prerelease():
    v1 = StrictVersion("1.0a1")
    v2 = StrictVersion("1.0a2")
    result = v1._cmp(v2)
    assert result == -1

def test_cmp_with_non_strictversion():
    v1 = StrictVersion("1.0")
    result = v1._cmp(1.0)
    assert result == NotImplemented
