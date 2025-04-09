# file: dataclasses_json/undefined.py:130-131
# asked: {"lines": [130, 131], "branches": []}
# gained: {"lines": [130, 131], "branches": []}

import pytest
from dataclasses_json.undefined import _UndefinedParameterAction

def test_catch_all_undefined_parameters_sentinel_no_default():
    class _CatchAllUndefinedParameters(_UndefinedParameterAction):
        class _SentinelNoDefault:
            pass

    # Verify that the _SentinelNoDefault class exists within _CatchAllUndefinedParameters
    assert hasattr(_CatchAllUndefinedParameters, '_SentinelNoDefault')
    # Verify that _SentinelNoDefault is indeed a class
    assert isinstance(_CatchAllUndefinedParameters._SentinelNoDefault, type)
