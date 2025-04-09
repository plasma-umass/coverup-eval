# file: dataclasses_json/undefined.py:259-266
# asked: {"lines": [259, 260, 264, 265, 266], "branches": []}
# gained: {"lines": [259, 260, 264, 265, 266], "branches": []}

import pytest
from dataclasses_json.undefined import Undefined, _CatchAllUndefinedParameters, _RaiseUndefinedParameters, _IgnoreUndefinedParameters

def test_undefined_enum_include():
    assert Undefined.INCLUDE.value == _CatchAllUndefinedParameters

def test_undefined_enum_raise():
    assert Undefined.RAISE.value == _RaiseUndefinedParameters

def test_undefined_enum_exclude():
    assert Undefined.EXCLUDE.value == _IgnoreUndefinedParameters
