# file: flutils/packages.py:90-95
# asked: {"lines": [90, 91, 92, 93, 94, 95], "branches": []}
# gained: {"lines": [90, 91, 92, 93, 94, 95], "branches": []}

import pytest
from flutils.packages import _VersionInfo, _VersionPart

def test_version_info():
    # Create a _VersionPart instance
    version_part = _VersionPart(pos=1, txt='1', num=1, pre_txt='alpha', pre_num=1, name='version')

    # Create a _VersionInfo instance
    version_info = _VersionInfo(version='1.0.0-alpha.1', major=version_part, minor=version_part, patch=version_part, pre_pos=1)

    # Assertions to verify the _VersionInfo instance
    assert version_info.version == '1.0.0-alpha.1'
    assert version_info.major == version_part
    assert version_info.minor == version_part
    assert version_info.patch == version_part
    assert version_info.pre_pos == 1
