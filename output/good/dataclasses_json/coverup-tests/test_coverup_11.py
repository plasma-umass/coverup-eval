# file dataclasses_json/undefined.py:121-129
# lines [121, 122]
# branches []

import pytest
from dataclasses import dataclass
from dataclasses_json import dataclass_json, CatchAll, Undefined
from typing import Any

# Assuming the module dataclasses_json.undefined contains the _CatchAllUndefinedParameters class
from dataclasses_json.undefined import _CatchAllUndefinedParameters

# Define a dataclass with a CatchAll field
@dataclass_json(undefined=Undefined.INCLUDE)
@dataclass
class TestDataClassWithCatchAll:
    catch_all: CatchAll

# Define a test function to cover the _CatchAllUndefinedParameters class
def test_catch_all_undefined_parameters():
    # Create an instance of the dataclass with extra undefined parameters
    instance = TestDataClassWithCatchAll.from_dict({'extra_param1': 'value1', 'extra_param2': 'value2'})
    
    # Assert that the extra undefined parameters are included in the catch_all field
    assert instance.catch_all == {'extra_param1': 'value1', 'extra_param2': 'value2'}

    # Create an instance without undefined parameters
    instance_empty = TestDataClassWithCatchAll.from_dict({})
    
    # Assert that the catch_all field is an empty dictionary when no undefined parameters are given
    assert instance_empty.catch_all == {}

# Run the test function
def test_catch_all_undefined_parameters_cleanup(mocker):
    # Mock the _CatchAllUndefinedParameters to ensure it does not affect other tests
    mocker.patch('dataclasses_json.undefined._CatchAllUndefinedParameters', _CatchAllUndefinedParameters)
    
    # Run the test function
    test_catch_all_undefined_parameters()
