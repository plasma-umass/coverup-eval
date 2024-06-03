# file dataclasses_json/undefined.py:259-266
# lines [259, 260, 264, 265, 266]
# branches []

import pytest
from enum import Enum
from dataclasses_json.undefined import Undefined, _CatchAllUndefinedParameters, _RaiseUndefinedParameters, _IgnoreUndefinedParameters

def test_undefined_enum():
    # Test that the Undefined enum has the correct members
    assert Undefined.INCLUDE.value == _CatchAllUndefinedParameters
    assert Undefined.RAISE.value == _RaiseUndefinedParameters
    assert Undefined.EXCLUDE.value == _IgnoreUndefinedParameters

    # Test that the enum members are instances of their respective classes
    assert isinstance(Undefined.INCLUDE.value, type)
    assert isinstance(Undefined.RAISE.value, type)
    assert isinstance(Undefined.EXCLUDE.value, type)

    # Test that the enum members are of type Enum
    assert isinstance(Undefined.INCLUDE, Enum)
    assert isinstance(Undefined.RAISE, Enum)
    assert isinstance(Undefined.EXCLUDE, Enum)
