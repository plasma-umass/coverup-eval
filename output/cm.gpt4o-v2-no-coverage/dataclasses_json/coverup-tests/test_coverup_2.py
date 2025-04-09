# file: dataclasses_json/cfg.py:11-17
# asked: {"lines": [11, 12, 16, 17], "branches": []}
# gained: {"lines": [11, 12, 16, 17], "branches": []}

import pytest
from dataclasses_json.cfg import Exclude

def test_exclude_always():
    assert Exclude.ALWAYS(None) == True
    assert Exclude.ALWAYS(1) == True
    assert Exclude.ALWAYS("test") == True

def test_exclude_never():
    assert Exclude.NEVER(None) == False
    assert Exclude.NEVER(1) == False
    assert Exclude.NEVER("test") == False
