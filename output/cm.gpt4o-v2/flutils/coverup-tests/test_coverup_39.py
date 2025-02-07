# file: flutils/packages.py:112-127
# asked: {"lines": [112, 115, 116, 118, 119, 120, 121, 124, 125, 126, 127], "branches": [[118, 119], [118, 124], [124, 125], [124, 127]]}
# gained: {"lines": [112, 115, 116, 118, 119, 120, 121, 124, 125, 126, 127], "branches": [[118, 119], [118, 124], [124, 125], [124, 127]]}

import pytest

from flutils.packages import _build_version_bump_position

def test_build_version_bump_position_within_range():
    assert _build_version_bump_position(0) == 0
    assert _build_version_bump_position(1) == 1
    assert _build_version_bump_position(2) == 2
    assert _build_version_bump_position(-1) == 2
    assert _build_version_bump_position(-2) == 1
    assert _build_version_bump_position(-3) == 0

def test_build_version_bump_position_out_of_range():
    with pytest.raises(ValueError, match=r"The given value for 'position', 3, must be an 'int' between \(-3\) and \(2\)."):
        _build_version_bump_position(3)
    with pytest.raises(ValueError, match=r"The given value for 'position', -4, must be an 'int' between \(-3\) and \(2\)."):
        _build_version_bump_position(-4)
