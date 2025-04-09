# file: dataclasses_json/undefined.py:193-201
# asked: {"lines": [193, 194, 195, 196, 197, 198, 199, 200, 201], "branches": [[198, 199], [198, 201]]}
# gained: {"lines": [193, 194, 195, 196, 197, 198, 199, 200, 201], "branches": [[198, 199], [198, 201]]}

import pytest
from dataclasses import dataclass, field
from typing import Any, Dict, Optional
from dataclasses_json.undefined import _CatchAllUndefinedParameters
from dataclasses_json.utils import CatchAllVar
from marshmallow import ValidationError

class UndefinedParameterError(ValidationError):
    """
    Raised when something has gone wrong handling undefined parameters.
    """
    pass

@dataclass
class TestClass:
    catch_all: Optional[CatchAllVar] = field(default_factory=dict)

def test_handle_to_dict_with_dict():
    obj = TestClass(catch_all={'extra_param': 'value'})
    kvs = {'catch_all': obj.catch_all}
    result = _CatchAllUndefinedParameters.handle_to_dict(obj, kvs)
    assert result == {'extra_param': 'value'}

def test_handle_to_dict_without_dict():
    obj = TestClass(catch_all=None)
    kvs = {'catch_all': obj.catch_all}
    result = _CatchAllUndefinedParameters.handle_to_dict(obj, kvs)
    assert result == {}

def test_get_catch_all_field():
    field = _CatchAllUndefinedParameters._get_catch_all_field(TestClass)
    assert field.name == 'catch_all'

def test_get_catch_all_field_no_field():
    @dataclass
    class NoCatchAllFieldClass:
        pass

    with pytest.raises(ValidationError, match='No field of type dataclasses_json.CatchAll defined'):
        _CatchAllUndefinedParameters._get_catch_all_field(NoCatchAllFieldClass)

def test_get_catch_all_field_multiple_fields():
    @dataclass
    class MultipleCatchAllFieldClass:
        catch_all1: Optional[CatchAllVar] = field(default_factory=dict)
        catch_all2: Optional[CatchAllVar] = field(default_factory=dict)

    with pytest.raises(ValidationError, match='Multiple catch-all fields supplied: 2.'):
        _CatchAllUndefinedParameters._get_catch_all_field(MultipleCatchAllFieldClass)
