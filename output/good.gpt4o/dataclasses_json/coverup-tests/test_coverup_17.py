# file dataclasses_json/undefined.py:59-73
# lines [59, 60, 65, 66, 67, 68, 69, 70, 71, 72, 73]
# branches ['70->71', '70->73']

import pytest
from dataclasses import dataclass
from dataclasses_json.undefined import _RaiseUndefinedParameters, UndefinedParameterError, _UndefinedParameterAction

@dataclass
class DummyClass:
    a: int
    b: int

def test_raise_undefined_parameters_handle_from_dict():
    kvs = {'a': 1, 'b': 2, 'c': 3}
    
    with pytest.raises(UndefinedParameterError) as excinfo:
        _RaiseUndefinedParameters.handle_from_dict(DummyClass, kvs)
    
    assert "Received undefined initialization arguments {'c': 3}" in str(excinfo.value)

def test_raise_undefined_parameters_handle_from_dict_no_error():
    kvs = {'a': 1, 'b': 2}
    
    result = _RaiseUndefinedParameters.handle_from_dict(DummyClass, kvs)
    
    assert result == {'a': 1, 'b': 2}
