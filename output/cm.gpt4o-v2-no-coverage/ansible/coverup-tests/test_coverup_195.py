# file: lib/ansible/module_utils/compat/version.py:330-341
# asked: {"lines": [330, 331, 332, 333, 334, 336, 337, 338, 339, 340, 341], "branches": [[331, 332], [331, 333], [333, 334], [333, 336], [336, 337], [336, 338], [338, 339], [338, 340], [340, 0], [340, 341]]}
# gained: {"lines": [330, 331, 332, 333, 334, 336, 337, 338, 339, 340, 341], "branches": [[331, 332], [331, 333], [333, 334], [333, 336], [336, 337], [336, 338], [338, 339], [338, 340], [340, 341]]}

import pytest
from ansible.module_utils.compat.version import LooseVersion

class MockVersion:
    def __init__(self, version):
        self.version = version

@pytest.fixture
def mock_version(monkeypatch):
    def mock_init(self, vstring=None):
        if vstring:
            self.version = vstring.split('.')
    monkeypatch.setattr(LooseVersion, "__init__", mock_init)

def test_cmp_with_string(mock_version):
    v1 = LooseVersion("1.0")
    assert v1._cmp("1.0") == 0
    assert v1._cmp("0.9") == 1
    assert v1._cmp("1.1") == -1

def test_cmp_with_looseversion(mock_version):
    v1 = LooseVersion("1.0")
    v2 = LooseVersion("1.0")
    v3 = LooseVersion("0.9")
    v4 = LooseVersion("1.1")
    assert v1._cmp(v2) == 0
    assert v1._cmp(v3) == 1
    assert v1._cmp(v4) == -1

def test_cmp_with_other_type(mock_version):
    v1 = LooseVersion("1.0")
    assert v1._cmp(123) == NotImplemented
