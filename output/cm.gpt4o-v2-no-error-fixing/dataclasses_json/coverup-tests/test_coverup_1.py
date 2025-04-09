# file: dataclasses_json/undefined.py:130-131
# asked: {"lines": [130, 131], "branches": []}
# gained: {"lines": [130, 131], "branches": []}

import pytest
from dataclasses_json.undefined import _CatchAllUndefinedParameters

def test_sentinel_no_default_class():
    sentinel_instance = _CatchAllUndefinedParameters._SentinelNoDefault()
    assert isinstance(sentinel_instance, _CatchAllUndefinedParameters._SentinelNoDefault)
