# file: flutils/packages.py:90-95
# asked: {"lines": [90, 91, 92, 93, 94, 95], "branches": []}
# gained: {"lines": [90, 91, 92, 93, 94, 95], "branches": []}

import pytest
from flutils.packages import _VersionInfo

def test_version_info_namedtuple():
    version_info = _VersionInfo(version="1.2.3", major=1, minor=2, patch=3, pre_pos=-1)
    
    assert version_info.version == "1.2.3"
    assert version_info.major == 1
    assert version_info.minor == 2
    assert version_info.patch == 3
    assert version_info.pre_pos == -1
