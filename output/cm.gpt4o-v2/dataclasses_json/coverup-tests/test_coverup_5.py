# file: dataclasses_json/cfg.py:11-17
# asked: {"lines": [11, 12, 16, 17], "branches": []}
# gained: {"lines": [11, 12, 16, 17], "branches": []}

import pytest
from dataclasses_json.cfg import Exclude

def test_exclude_always():
    assert Exclude.ALWAYS(None) is True
    assert Exclude.ALWAYS(1) is True
    assert Exclude.ALWAYS("test") is True

def test_exclude_never():
    assert Exclude.NEVER(None) is False
    assert Exclude.NEVER(1) is False
    assert Exclude.NEVER("test") is False
