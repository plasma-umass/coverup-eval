# file: flutils/packages.py:53-87
# asked: {"lines": [53, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 84, 85, 86, 87], "branches": [[59, 0], [59, 60], [61, 62], [61, 63], [71, 74], [71, 87], [76, 77], [76, 78], [78, 79], [78, 87]]}
# gained: {"lines": [53, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 84, 85, 86, 87], "branches": [[59, 0], [59, 60], [61, 62], [61, 63], [71, 74], [71, 87], [76, 77], [76, 78], [78, 79], [78, 87]]}

import pytest
from flutils.packages import _each_version_part
from distutils.version import StrictVersion

class _VersionPart:
    def __init__(self, pos, txt, num, pre_txt, pre_num, name):
        self.pos = pos
        self.txt = txt
        self.num = num
        self.pre_txt = pre_txt
        self.pre_num = pre_num
        self.name = name

_BUMP_VERSION_POSITION_NAMES = ['major', 'minor', 'patch']

def test_each_version_part_full_coverage():
    # Test case 1: version without prerelease
    ver_obj = StrictVersion("1.2.3")
    parts = list(_each_version_part(ver_obj))
    assert len(parts) == 3
    assert parts[0].pos == 0
    assert parts[0].txt == '1'
    assert parts[0].num == 1
    assert parts[0].pre_txt == ''
    assert parts[0].pre_num == -1
    assert parts[0].name == 'major'
    
    assert parts[1].pos == 1
    assert parts[1].txt == '2'
    assert parts[1].num == 2
    assert parts[1].pre_txt == ''
    assert parts[1].pre_num == -1
    assert parts[1].name == 'minor'
    
    assert parts[2].pos == 2
    assert parts[2].txt == '3'
    assert parts[2].num == 3
    assert parts[2].pre_txt == ''
    assert parts[2].pre_num == -1
    assert parts[2].name == 'patch'

    # Test case 2: version with prerelease
    ver_obj = StrictVersion("1.2.0a1")
    parts = list(_each_version_part(ver_obj))
    assert len(parts) == 3
    assert parts[0].pos == 0
    assert parts[0].txt == '1'
    assert parts[0].num == 1
    assert parts[0].pre_txt == ''
    assert parts[0].pre_num == -1
    assert parts[0].name == 'major'
    
    assert parts[1].pos == 1
    assert parts[1].txt == '2a1'
    assert parts[1].num == 2
    assert parts[1].pre_txt == 'a'
    assert parts[1].pre_num == 1
    assert parts[1].name == 'minor'
    
    assert parts[2].pos == 2
    assert parts[2].txt == ''
    assert parts[2].num == 0
    assert parts[2].pre_txt == ''
    assert parts[2].pre_num == -1
    assert parts[2].name == 'patch'

    # Test case 3: version with prerelease and non-zero patch
    ver_obj = StrictVersion("1.2.3a1")
    parts = list(_each_version_part(ver_obj))
    assert len(parts) == 3
    assert parts[0].pos == 0
    assert parts[0].txt == '1'
    assert parts[0].num == 1
    assert parts[0].pre_txt == ''
    assert parts[0].pre_num == -1
    assert parts[0].name == 'major'
    
    assert parts[1].pos == 1
    assert parts[1].txt == '2'
    assert parts[1].num == 2
    assert parts[1].pre_txt == ''
    assert parts[1].pre_num == -1
    assert parts[1].name == 'minor'
    
    assert parts[2].pos == 2
    assert parts[2].txt == '3a1'
    assert parts[2].num == 3
    assert parts[2].pre_txt == 'a'
    assert parts[2].pre_num == 1
    assert parts[2].name == 'patch'
