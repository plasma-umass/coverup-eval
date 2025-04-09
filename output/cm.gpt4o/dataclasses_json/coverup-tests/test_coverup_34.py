# file dataclasses_json/undefined.py:79-118
# lines [88, 89, 90, 91, 95, 96, 98, 99, 100, 101, 102, 103, 104, 105, 107, 108, 109, 110, 112, 113, 114, 115, 116, 118]
# branches []

import pytest
from dataclasses import dataclass
from dataclasses_json.undefined import _IgnoreUndefinedParameters, _UndefinedParameterAction
from typing import Dict, Any
import functools
import inspect

# Mock class to use for testing
@dataclass
class MockClass:
    a: int
    b: int = 0

def test_handle_from_dict(mocker):
    # Mock the _separate_defined_undefined_kvs method
    mocker.patch.object(_UndefinedParameterAction, '_separate_defined_undefined_kvs', return_value=({'a': 1}, {'c': 3}))
    
    kvs = {'a': 1, 'c': 3}
    result = _IgnoreUndefinedParameters.handle_from_dict(MockClass, kvs)
    
    assert result == {'a': 1}

def test_create_init(mocker):
    # Mock the _separate_defined_undefined_kvs method
    mocker.patch.object(_UndefinedParameterAction, '_separate_defined_undefined_kvs', return_value=({'a': 1}, {'c': 3}))
    
    # Create a new init method using the create_init method
    new_init = _IgnoreUndefinedParameters.create_init(MockClass)
    
    # Create an instance of MockClass using the new init method
    instance = MockClass.__new__(MockClass)
    new_init(instance, a=1, c=3)
    
    assert instance.a == 1
    assert instance.b == 0

@pytest.fixture(autouse=True)
def cleanup():
    yield
    # Cleanup code if necessary
