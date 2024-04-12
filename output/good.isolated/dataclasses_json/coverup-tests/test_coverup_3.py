# file dataclasses_json/cfg.py:11-17
# lines [11, 12, 16, 17]
# branches []

import pytest
from dataclasses_json.cfg import Exclude

def test_exclude_always_never():
    assert Exclude.ALWAYS(None) is True, "Exclude.ALWAYS should always return True"
    assert Exclude.NEVER(None) is False, "Exclude.NEVER should always return False"
