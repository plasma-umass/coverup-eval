# file dataclasses_json/core.py:295-312
# lines [295, 305, 306, 307, 308, 309, 311, 312]
# branches ['305->306', '305->308', '308->309', '308->311']

import pytest
from dataclasses import dataclass
from dataclasses_json.core import _decode_items
from typing import List, TypeVar, Generic

T = TypeVar('T')

@dataclass
class ExampleDataClass:
    value: int

class ExampleGeneric(Generic[T]):
    pass

def is_dataclass(obj):
    return isinstance(obj, type) and dataclass(obj)

def _is_supported_generic(type_arg):
    return hasattr(type_arg, '__origin__')

def test_decode_items_dataclass(mocker):
    mocker.patch('dataclasses_json.core.is_dataclass', side_effect=is_dataclass)
    mocker.patch('dataclasses_json.core._is_supported_generic', return_value=False)
    mocker.patch('dataclasses_json.core._decode_dataclass', side_effect=lambda t, x, _: x)
    
    xs = [ExampleDataClass(1), ExampleDataClass(2)]
    items = list(_decode_items(ExampleDataClass, xs, infer_missing=False))
    assert items == xs

def test_decode_items_generic(mocker):
    mocker.patch('dataclasses_json.core.is_dataclass', return_value=False)
    mocker.patch('dataclasses_json.core._is_supported_generic', side_effect=_is_supported_generic)
    mocker.patch('dataclasses_json.core._decode_generic', side_effect=lambda t, x, _: x)
    
    xs = [ExampleGeneric(), ExampleGeneric()]
    items = list(_decode_items(ExampleGeneric[int], xs, infer_missing=False))
    assert items == xs

def test_decode_items_plain_list(mocker):
    mocker.patch('dataclasses_json.core.is_dataclass', return_value=False)
    mocker.patch('dataclasses_json.core._is_supported_generic', return_value=False)
    
    xs = [1, 2, 3]
    items = list(_decode_items(List[int], xs, infer_missing=False))
    assert items == xs
