# file: flutils/packages.py:44-50
# asked: {"lines": [44, 45, 46, 47, 48, 49, 50], "branches": []}
# gained: {"lines": [44, 45, 46, 47, 48, 49, 50], "branches": []}

import pytest
from flutils.packages import _VersionPart

@pytest.fixture
def version_part():
    return _VersionPart(pos=1, txt="1.0.0", num=100, pre_txt="alpha", pre_num=1, name="version")

def test_version_part_attributes(version_part):
    assert version_part.pos == 1
    assert version_part.txt == "1.0.0"
    assert version_part.num == 100
    assert version_part.pre_txt == "alpha"
    assert version_part.pre_num == 1
    assert version_part.name == "version"

def test_version_part_namedtuple():
    vp = _VersionPart(pos=2, txt="2.0.0", num=200, pre_txt="beta", pre_num=2, name="version2")
    assert vp.pos == 2
    assert vp.txt == "2.0.0"
    assert vp.num == 200
    assert vp.pre_txt == "beta"
    assert vp.pre_num == 2
    assert vp.name == "version2"
