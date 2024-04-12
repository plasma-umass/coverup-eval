# file dataclasses_json/undefined.py:130-131
# lines [130, 131]
# branches []

import pytest
from dataclasses_json.undefined import _CatchAllUndefinedParameters

def test_catchall_undefined_parameters():
    catch_all = _CatchAllUndefinedParameters()
    sentinel = catch_all._SentinelNoDefault()

    # Assert that the sentinel is an instance of the nested class
    assert isinstance(sentinel, _CatchAllUndefinedParameters._SentinelNoDefault)
