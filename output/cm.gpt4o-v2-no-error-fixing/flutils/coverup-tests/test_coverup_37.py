# file: flutils/packages.py:53-87
# asked: {"lines": [53, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 84, 85, 86, 87], "branches": [[59, 0], [59, 60], [61, 62], [61, 63], [71, 74], [71, 87], [76, 77], [76, 78], [78, 79], [78, 87]]}
# gained: {"lines": [53, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 84, 85, 86, 87], "branches": [[59, 0], [59, 60], [61, 62], [61, 63], [71, 74], [71, 87], [76, 77], [76, 78], [78, 79], [78, 87]]}

import pytest
from distutils.version import StrictVersion
from flutils.packages import _each_version_part, _VersionPart

_BUMP_VERSION_POSITION_NAMES = ["major", "minor", "patch"]

def test_each_version_part():
    ver_obj = StrictVersion("1.2.3")
    parts = list(_each_version_part(ver_obj))
    assert len(parts) == 3
    assert parts[0] == _VersionPart(pos=0, txt='1', num=1, pre_txt='', pre_num=-1, name='major')
    assert parts[1] == _VersionPart(pos=1, txt='2', num=2, pre_txt='', pre_num=-1, name='minor')
    assert parts[2] == _VersionPart(pos=2, txt='3', num=3, pre_txt='', pre_num=-1, name='patch')

def test_each_version_part_with_prerelease():
    ver_obj = StrictVersion("1.2.0a1")
    parts = list(_each_version_part(ver_obj))
    assert len(parts) == 3
    assert parts[0] == _VersionPart(pos=0, txt='1', num=1, pre_txt='', pre_num=-1, name='major')
    assert parts[1] == _VersionPart(pos=1, txt='2a1', num=2, pre_txt='a', pre_num=1, name='minor')
    assert parts[2] == _VersionPart(pos=2, txt='', num=0, pre_txt='', pre_num=-1, name='patch')

def test_each_version_part_with_prerelease_non_zero_patch():
    ver_obj = StrictVersion("1.2.3a1")
    parts = list(_each_version_part(ver_obj))
    assert len(parts) == 3
    assert parts[0] == _VersionPart(pos=0, txt='1', num=1, pre_txt='', pre_num=-1, name='major')
    assert parts[1] == _VersionPart(pos=1, txt='2', num=2, pre_txt='', pre_num=-1, name='minor')
    assert parts[2] == _VersionPart(pos=2, txt='3a1', num=3, pre_txt='a', pre_num=1, name='patch')
