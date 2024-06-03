# file dataclasses_json/undefined.py:209-241
# lines [211, 212, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 226, 227, 228, 229, 231, 232, 233, 234, 235, 236, 237, 238, 239, 241]
# branches ['221->223', '221->224']

import pytest
from unittest.mock import patch, MagicMock
from dataclasses_json.undefined import _CatchAllUndefinedParameters
import inspect
import functools

class DummyClass:
    def __init__(self, a, b, c=None):
        self.a = a
        self.b = b
        self.c = c

@pytest.fixture
def mock_handle_from_dict(mocker):
    return mocker.patch('dataclasses_json.undefined._CatchAllUndefinedParameters.handle_from_dict', return_value={'a': 1, 'b': 2, 'c': None})

@pytest.fixture
def mock_separate_defined_undefined_kvs(mocker):
    return mocker.patch('dataclasses_json.undefined._CatchAllUndefinedParameters._separate_defined_undefined_kvs', return_value=({}, {'d': 4, 'e': 5}))

@pytest.fixture
def mock_get_catch_all_field(mocker):
    return mocker.patch('dataclasses_json.undefined._CatchAllUndefinedParameters._get_catch_all_field', return_value=MagicMock(name='catch_all_field'))

def test_catch_all_init(mock_handle_from_dict, mock_separate_defined_undefined_kvs, mock_get_catch_all_field):
    init_func = _CatchAllUndefinedParameters.create_init(DummyClass)
    dummy_instance = DummyClass.__new__(DummyClass)
    
    init_func(dummy_instance, 1, 2, d=4, e=5)
    
    assert dummy_instance.a == 1
    assert dummy_instance.b == 2
    assert dummy_instance.c is None
    mock_handle_from_dict.assert_called_once()
    mock_separate_defined_undefined_kvs.assert_called_once()
    mock_get_catch_all_field.assert_called_once()
