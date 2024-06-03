# file flutils/packages.py:98-109
# lines [98, 101, 102, 103, 104, 105, 106, 107, 108, 109]
# branches ['104->105', '104->108', '105->106', '105->107']

import pytest
from flutils.packages import _build_version_info, _VersionInfo
from distutils.version import StrictVersion

def test_build_version_info(mocker):
    # Mocking _each_version_part to control its output
    mocker.patch('flutils.packages._each_version_part', return_value=[
        mocker.Mock(pre_txt=None, pos=0),
        mocker.Mock(pre_txt='a', pos=1),
        mocker.Mock(pre_txt=None, pos=2)
    ])

    version = "1.0a1"
    expected_args = [version, mocker.ANY, mocker.ANY, mocker.ANY, 1]

    result = _build_version_info(version)

    assert isinstance(result, _VersionInfo)
    assert result == _VersionInfo(*expected_args)
