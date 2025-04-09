# file: flutils/packages.py:98-109
# asked: {"lines": [98, 101, 102, 103, 104, 105, 106, 107, 108, 109], "branches": [[104, 105], [104, 108], [105, 106], [105, 107]]}
# gained: {"lines": [98, 101, 102, 103, 104, 105, 106, 107, 108, 109], "branches": [[104, 105], [104, 108], [105, 106], [105, 107]]}

import pytest
from flutils.packages import _build_version_info, _VersionInfo
from distutils.version import StrictVersion

def test_build_version_info(monkeypatch):
    class MockVersionPart:
        def __init__(self, pre_txt=None, pos=None):
            self.pre_txt = pre_txt
            self.pos = pos

    def mock_each_version_part(ver_obj):
        return [
            MockVersionPart(pre_txt=None, pos=0),
            MockVersionPart(pre_txt='a', pos=1),
            MockVersionPart(pre_txt=None, pos=2)
        ]

    monkeypatch.setattr('flutils.packages._each_version_part', mock_each_version_part)

    version = "1.0a1"
    result = _build_version_info(version)
    
    assert isinstance(result, _VersionInfo)
    assert result.version == version
    assert result.pre_pos == 1
    assert result[1].pos == 0
    assert result[2].pre_txt == 'a'
    assert result[3].pos == 2
