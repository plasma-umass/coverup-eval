# file: flutils/packages.py:112-127
# asked: {"lines": [125, 126], "branches": [[124, 125]]}
# gained: {"lines": [125, 126], "branches": [[124, 125]]}

import pytest
from flutils.packages import _build_version_bump_position

def test_build_version_bump_position_within_range():
    assert _build_version_bump_position(0) == 0
    assert _build_version_bump_position(1) == 1
    assert _build_version_bump_position(2) == 2

def test_build_version_bump_position_below_range():
    with pytest.raises(ValueError):
        _build_version_bump_position(-4)

def test_build_version_bump_position_above_range():
    with pytest.raises(ValueError):
        _build_version_bump_position(3)

def test_build_version_bump_position_negative():
    assert _build_version_bump_position(-1) == 2
    assert _build_version_bump_position(-2) == 1
    assert _build_version_bump_position(-3) == 0
