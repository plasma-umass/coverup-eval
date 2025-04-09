# file: dataclasses_json/core.py:295-312
# asked: {"lines": [295, 305, 306, 307, 308, 309, 311, 312], "branches": [[305, 306], [305, 308], [308, 309], [308, 311]]}
# gained: {"lines": [295, 305, 306, 307, 308, 309, 311, 312], "branches": [[305, 306], [305, 308], [308, 309], [308, 311]]}

import pytest
from dataclasses import dataclass, is_dataclass
from unittest.mock import patch
from dataclasses_json.core import _decode_items

@dataclass
class DummyClass:
    field: int

def test_decode_items_with_dataclass():
    @dataclass
    class TestClass:
        a: int

    data = [{'a': 1}, {'a': 2}]
    with patch('dataclasses_json.core._decode_dataclass', return_value=TestClass(1)) as mock_decode_dataclass:
        result = list(_decode_items(TestClass, data, infer_missing=False))
        assert all(isinstance(item, TestClass) for item in result)
        assert mock_decode_dataclass.call_count == len(data)

def test_decode_items_with_supported_generic():
    data = [1, 2, 3]
    with patch('dataclasses_json.core._decode_generic', return_value=1) as mock_decode_generic, \
         patch('dataclasses_json.core._is_supported_generic', return_value=True):
        result = list(_decode_items(list, data, infer_missing=False))
        assert result == [1, 1, 1]
        assert mock_decode_generic.call_count == len(data)

def test_decode_items_with_neither_dataclass_nor_generic():
    data = [1, 2, 3]
    with patch('dataclasses_json.core._is_supported_generic', return_value=False):
        result = _decode_items(int, data, infer_missing=False)
        assert result == data

@pytest.fixture(autouse=True)
def run_around_tests():
    # Code to run before each test
    yield
    # Code to run after each test
    # Clean up any state here if necessary
