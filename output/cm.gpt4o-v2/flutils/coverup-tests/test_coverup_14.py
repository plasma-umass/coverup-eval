# file: flutils/packages.py:44-50
# asked: {"lines": [44, 45, 46, 47, 48, 49, 50], "branches": []}
# gained: {"lines": [44, 45, 46, 47, 48, 49, 50], "branches": []}

import pytest
from flutils.packages import _VersionPart

def test_version_part_initialization():
    version_part = _VersionPart(pos=1, txt='alpha', num=2, pre_txt='beta', pre_num=3, name='release')
    assert version_part.pos == 1
    assert version_part.txt == 'alpha'
    assert version_part.num == 2
    assert version_part.pre_txt == 'beta'
    assert version_part.pre_num == 3
    assert version_part.name == 'release'
