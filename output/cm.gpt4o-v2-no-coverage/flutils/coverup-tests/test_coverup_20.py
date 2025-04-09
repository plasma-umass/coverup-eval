# file: flutils/packages.py:98-109
# asked: {"lines": [98, 101, 102, 103, 104, 105, 106, 107, 108, 109], "branches": [[104, 105], [104, 108], [105, 106], [105, 107]]}
# gained: {"lines": [98, 101, 102, 103, 104, 105, 106, 107, 108, 109], "branches": [[104, 105], [104, 108], [105, 106], [105, 107]]}

import pytest
from distutils.version import StrictVersion
from flutils.packages import _build_version_info, _VersionInfo, _each_version_part

def test_build_version_info():
    version = "1.2.3"
    result = _build_version_info(version)
    
    assert isinstance(result, _VersionInfo)
    assert result.version == version
    assert result.major.txt == "1"
    assert result.minor.txt == "2"
    assert result.patch.txt == "3"
    assert result.pre_pos == -1

def test_build_version_info_with_prerelease():
    version = "1.2.3a1"
    result = _build_version_info(version)
    
    assert isinstance(result, _VersionInfo)
    assert result.version == version
    assert result.major.txt == "1"
    assert result.minor.txt == "2"
    assert result.patch.txt == "3a1"
    assert result.patch.pre_txt == "a"
    assert result.patch.pre_num == 1
    assert result.pre_pos == 2

def test_each_version_part():
    version = "1.2.3"
    ver_obj = StrictVersion(version)
    parts = list(_each_version_part(ver_obj))
    
    assert len(parts) == 3
    assert parts[0].txt == "1"
    assert parts[1].txt == "2"
    assert parts[2].txt == "3"

def test_each_version_part_with_prerelease():
    version = "1.2.3a1"
    ver_obj = StrictVersion(version)
    parts = list(_each_version_part(ver_obj))
    
    assert len(parts) == 3
    assert parts[0].txt == "1"
    assert parts[1].txt == "2"
    assert parts[2].txt == "3a1"
    assert parts[2].pre_txt == "a"
    assert parts[2].pre_num == 1
