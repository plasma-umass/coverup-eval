# file: dataclasses_json/undefined.py:169-191
# asked: {"lines": [176, 177, 179, 181, 182, 183, 184, 185, 189, 191], "branches": [[183, 184], [183, 185], [185, 189], [185, 191]]}
# gained: {"lines": [176, 177, 179, 181, 182, 183, 184, 185, 189, 191], "branches": [[183, 184], [183, 185], [185, 189], [185, 191]]}

import pytest
import dataclasses
from dataclasses import Field
from dataclasses_json.undefined import _CatchAllUndefinedParameters

class _UndefinedParameterAction:
    pass

class _SentinelNoDefault:
    pass

def test_get_default_with_default():
    field_with_default = Field(default=10, default_factory=dataclasses.MISSING, init=True, repr=True, hash=None, compare=True, metadata=None, kw_only=False)
    result = _CatchAllUndefinedParameters._get_default(field_with_default)
    assert result == 10

def test_get_default_with_default_factory():
    field_with_default_factory = Field(default=dataclasses.MISSING, default_factory=lambda: 20, init=True, repr=True, hash=None, compare=True, metadata=None, kw_only=False)
    result = _CatchAllUndefinedParameters._get_default(field_with_default_factory)
    assert result == 20

def test_get_default_with_no_default_or_factory():
    field_with_none = Field(default=dataclasses.MISSING, default_factory=dataclasses.MISSING, init=True, repr=True, hash=None, compare=True, metadata=None, kw_only=False)
    result = _CatchAllUndefinedParameters._get_default(field_with_none)
    assert result == _CatchAllUndefinedParameters._SentinelNoDefault
