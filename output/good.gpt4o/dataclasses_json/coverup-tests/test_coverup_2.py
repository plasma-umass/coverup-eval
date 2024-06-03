# file dataclasses_json/cfg.py:11-17
# lines [11, 12, 16, 17]
# branches []

import pytest
from dataclasses_json.cfg import Exclude

def test_exclude_always():
    assert Exclude.ALWAYS(None) is True
    assert Exclude.ALWAYS(123) is True
    assert Exclude.ALWAYS("test") is True

def test_exclude_never():
    assert Exclude.NEVER(None) is False
    assert Exclude.NEVER(123) is False
    assert Exclude.NEVER("test") is False
