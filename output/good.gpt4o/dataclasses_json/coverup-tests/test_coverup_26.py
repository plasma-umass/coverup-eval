# file dataclasses_json/core.py:295-312
# lines [295, 305, 306, 307, 308, 309, 311, 312]
# branches ['305->306', '305->308', '308->309', '308->311']

import pytest
from dataclasses import dataclass, is_dataclass
from dataclasses_json.core import _decode_items

@dataclass
class ExampleDataclass:
    value: int

def _decode_dataclass(type_arg, x, infer_missing):
    return type_arg(**x)

def _is_supported_generic(type_arg):
    return type_arg in [list, dict, set]

def _decode_generic(type_arg, x, infer_missing):
    if type_arg == list:
        return x  # Assuming x is already a list
    elif type_arg == dict:
        return {k: v for k, v in x.items()}
    elif type_arg == set:
        return {item for item in x}
    return x

def test_decode_items_with_dataclass():
    xs = [{'value': 1}, {'value': 2}]
    result = list(_decode_items(ExampleDataclass, xs, infer_missing=False))
    assert result == [ExampleDataclass(value=1), ExampleDataclass(value=2)]

def test_decode_items_with_supported_generic():
    xs = [[1, 2], [3, 4]]
    result = list(_decode_items(list, xs, infer_missing=False))
    assert result == [[1, 2], [3, 4]]

def test_decode_items_with_unsupported_type():
    xs = [1, 2, 3]
    result = _decode_items(int, xs, infer_missing=False)
    assert result == xs

@pytest.fixture(autouse=True)
def mock_dependencies(mocker):
    mocker.patch('dataclasses_json.core._decode_dataclass', _decode_dataclass)
    mocker.patch('dataclasses_json.core._is_supported_generic', _is_supported_generic)
    mocker.patch('dataclasses_json.core._decode_generic', _decode_generic)
