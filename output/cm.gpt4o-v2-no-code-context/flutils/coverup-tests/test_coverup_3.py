# file: flutils/packages.py:44-50
# asked: {"lines": [44, 45, 46, 47, 48, 49, 50], "branches": []}
# gained: {"lines": [44, 45, 46, 47, 48, 49, 50], "branches": []}

import pytest
from flutils.packages import _VersionPart

def test_version_part_initialization():
    version_part = _VersionPart(pos=1, txt='1.0', num=100, pre_txt='alpha', pre_num=1, name='version')
    assert version_part.pos == 1
    assert version_part.txt == '1.0'
    assert version_part.num == 100
    assert version_part.pre_txt == 'alpha'
    assert version_part.pre_num == 1
    assert version_part.name == 'version'
