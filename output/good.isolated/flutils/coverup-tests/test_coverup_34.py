# file flutils/packages.py:53-87
# lines [53, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 84, 85, 86, 87]
# branches ['59->exit', '59->60', '61->62', '61->63', '71->74', '71->87', '76->77', '76->78', '78->79', '78->87']

import pytest
from distutils.version import StrictVersion
from typing import NamedTuple, Tuple, Union, Generator, Dict, Any, cast
from flutils.packages import _each_version_part

_VersionPart = NamedTuple('_VersionPart', [
    ('pos', int),
    ('txt', str),
    ('num', int),
    ('pre_txt', str),
    ('pre_num', int),
    ('name', str)
])

_BUMP_VERSION_POSITION_NAMES = ('major', 'minor', 'micro')

@pytest.fixture
def strict_version_mock(mocker):
    mock = mocker.Mock(spec=StrictVersion)
    mock.version = (1, 2, 0)
    mock.prerelease = ('a', 1)
    return mock

def test_each_version_part_with_prerelease(strict_version_mock):
    parts = list(_each_version_part(strict_version_mock))
    assert parts[0].txt == '1'
    assert parts[0].pre_txt == ''
    assert parts[0].pre_num == -1
    assert parts[1].txt == '2a1'
    assert parts[1].pre_txt == 'a'
    assert parts[1].pre_num == 1
    assert parts[2].txt == ''
    assert parts[2].pre_txt == ''
    assert parts[2].pre_num == -1

def test_each_version_part_without_prerelease(strict_version_mock):
    strict_version_mock.prerelease = None
    parts = list(_each_version_part(strict_version_mock))
    assert parts[0].txt == '1'
    assert parts[0].pre_txt == ''
    assert parts[0].pre_num == -1
    assert parts[1].txt == '2'
    assert parts[1].pre_txt == ''
    assert parts[1].pre_num == -1
    assert parts[2].txt == ''
    assert parts[2].pre_txt == ''
    assert parts[2].pre_num == -1
