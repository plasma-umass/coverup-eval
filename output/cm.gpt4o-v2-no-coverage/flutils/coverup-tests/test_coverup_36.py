# file: flutils/packages.py:44-50
# asked: {"lines": [44, 45, 46, 47, 48, 49, 50], "branches": []}
# gained: {"lines": [44, 45, 46, 47, 48, 49, 50], "branches": []}

import pytest
from flutils.packages import _VersionPart

def test_version_part_creation():
    part = _VersionPart(pos=1, txt='alpha', num=2, pre_txt='beta', pre_num=3, name='release')
    assert part.pos == 1
    assert part.txt == 'alpha'
    assert part.num == 2
    assert part.pre_txt == 'beta'
    assert part.pre_num == 3
    assert part.name == 'release'

def test_version_part_replace():
    part = _VersionPart(pos=1, txt='alpha', num=2, pre_txt='beta', pre_num=3, name='release')
    new_part = part._replace(txt='gamma')
    assert new_part.txt == 'gamma'
    assert new_part.pos == 1  # unchanged
    assert new_part.num == 2  # unchanged
    assert new_part.pre_txt == 'beta'  # unchanged
    assert new_part.pre_num == 3  # unchanged
    assert new_part.name == 'release'  # unchanged

def test_version_part_asdict():
    part = _VersionPart(pos=1, txt='alpha', num=2, pre_txt='beta', pre_num=3, name='release')
    part_dict = part._asdict()
    assert part_dict == {
        'pos': 1,
        'txt': 'alpha',
        'num': 2,
        'pre_txt': 'beta',
        'pre_num': 3,
        'name': 'release'
    }

def test_version_part_equality():
    part1 = _VersionPart(pos=1, txt='alpha', num=2, pre_txt='beta', pre_num=3, name='release')
    part2 = _VersionPart(pos=1, txt='alpha', num=2, pre_txt='beta', pre_num=3, name='release')
    part3 = _VersionPart(pos=2, txt='beta', num=3, pre_txt='gamma', pre_num=4, name='final')
    assert part1 == part2
    assert part1 != part3

def test_version_part_ordering():
    part1 = _VersionPart(pos=1, txt='alpha', num=2, pre_txt='beta', pre_num=3, name='release')
    part2 = _VersionPart(pos=2, txt='beta', num=3, pre_txt='gamma', pre_num=4, name='final')
    assert part1 < part2
    assert part1 <= part2
    assert part2 > part1
    assert part2 >= part1

def test_version_part_hash():
    part1 = _VersionPart(pos=1, txt='alpha', num=2, pre_txt='beta', pre_num=3, name='release')
    part2 = _VersionPart(pos=1, txt='alpha', num=2, pre_txt='beta', pre_num=3, name='release')
    part_set = {part1, part2}
    assert len(part_set) == 1  # because part1 and part2 are equal, they should be considered the same in a set
