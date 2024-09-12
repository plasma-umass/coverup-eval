# file: lib/ansible/module_utils/compat/version.py:330-341
# asked: {"lines": [330, 331, 332, 333, 334, 336, 337, 338, 339, 340, 341], "branches": [[331, 332], [331, 333], [333, 334], [333, 336], [336, 337], [336, 338], [338, 339], [338, 340], [340, 0], [340, 341]]}
# gained: {"lines": [330, 331, 332, 333, 334, 336, 337, 338, 339, 340, 341], "branches": [[331, 332], [331, 333], [333, 334], [333, 336], [336, 337], [336, 338], [338, 339], [338, 340], [340, 341]]}

import pytest
from ansible.module_utils.compat.version import LooseVersion

def test_cmp_with_string():
    v1 = LooseVersion("1.0")
    result = v1._cmp("1.0")
    assert result == 0

def test_cmp_with_looseversion():
    v1 = LooseVersion("1.0")
    v2 = LooseVersion("1.0")
    result = v1._cmp(v2)
    assert result == 0

def test_cmp_with_higher_version():
    v1 = LooseVersion("1.0")
    v2 = LooseVersion("2.0")
    result = v1._cmp(v2)
    assert result == -1

def test_cmp_with_lower_version():
    v1 = LooseVersion("2.0")
    v2 = LooseVersion("1.0")
    result = v1._cmp(v2)
    assert result == 1

def test_cmp_with_non_comparable():
    v1 = LooseVersion("1.0")
    result = v1._cmp(1.0)
    assert result == NotImplemented
