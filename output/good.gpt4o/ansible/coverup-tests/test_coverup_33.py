# file lib/ansible/module_utils/compat/version.py:39-81
# lines [39, 40, 46, 47, 48, 50, 51, 53, 54, 55, 56, 57, 59, 60, 61, 62, 63, 65, 66, 67, 68, 69, 71, 72, 73, 74, 75, 77, 78, 79, 80, 81]
# branches ['47->exit', '47->48', '55->56', '55->57', '61->62', '61->63', '67->68', '67->69', '73->74', '73->75', '79->80', '79->81']

import pytest
from unittest.mock import MagicMock

# Assuming the Version class is imported from ansible.module_utils.compat.version
from ansible.module_utils.compat.version import Version

class TestVersion(Version):
    def _cmp(self, other):
        if not isinstance(other, TestVersion):
            return NotImplemented
        return (self.vstring > other.vstring) - (self.vstring < other.vstring)

    def parse(self, vstring):
        self.vstring = vstring

    def __str__(self):
        return self.vstring

@pytest.fixture
def version_a():
    return TestVersion("1.0")

@pytest.fixture
def version_b():
    return TestVersion("2.0")

def test_version_eq(version_a, version_b):
    assert not (version_a == version_b)
    version_c = TestVersion("1.0")
    assert version_a == version_c

def test_version_lt(version_a, version_b):
    assert version_a < version_b

def test_version_le(version_a, version_b):
    assert version_a <= version_b
    version_c = TestVersion("1.0")
    assert version_a <= version_c

def test_version_gt(version_a, version_b):
    assert version_b > version_a

def test_version_ge(version_a, version_b):
    assert version_b >= version_a
    version_c = TestVersion("2.0")
    assert version_b >= version_c

def test_version_repr(version_a):
    assert repr(version_a) == "TestVersion ('1.0')"

def test_version_cmp_not_implemented():
    version_a = TestVersion("1.0")
    other = MagicMock()
    other.vstring = "mock"
    assert version_a._cmp(other) is NotImplemented
