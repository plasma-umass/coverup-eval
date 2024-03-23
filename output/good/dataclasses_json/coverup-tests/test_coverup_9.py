# file dataclasses_json/undefined.py:193-201
# lines [193, 194, 195, 196, 197, 198, 199, 200, 201]
# branches ['198->199', '198->201']

import pytest
from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, CatchAll, Undefined
from dataclasses_json.undefined import _CatchAllUndefinedParameters
from typing import Any, Dict

@dataclass_json(undefined=Undefined.INCLUDE)
@dataclass
class MyClass:
    x: int
    y: int
    extra: CatchAll

def test_catch_all_undefined_parameters_handle_to_dict():
    obj = MyClass(x=1, y=2, extra={'z': 3})
    kvs = {'x': 1, 'y': 2, 'extra': {'z': 3}}
    
    result = _CatchAllUndefinedParameters.handle_to_dict(obj, kvs)
    
    assert result == {'x': 1, 'y': 2, 'z': 3}, "The extra undefined parameters should be included in the result"
