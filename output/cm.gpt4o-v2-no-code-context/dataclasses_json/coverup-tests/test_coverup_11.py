# file: dataclasses_json/core.py:295-312
# asked: {"lines": [295, 305, 306, 307, 308, 309, 311, 312], "branches": [[305, 306], [305, 308], [308, 309], [308, 311]]}
# gained: {"lines": [295, 305, 306, 307, 308, 309, 311, 312], "branches": [[305, 306], [305, 308], [308, 309], [308, 311]]}

import pytest
from dataclasses import dataclass, is_dataclass
from dataclasses_json.core import _decode_items, _decode_dataclass, _decode_generic

@dataclass
class ExampleDataclass:
    field: int

def test_decode_items_with_dataclass():
    data = [{'field': 1}, {'field': 2}]
    result = list(_decode_items(ExampleDataclass, data, infer_missing=False))
    assert all(isinstance(item, ExampleDataclass) for item in result)
    assert result[0].field == 1
    assert result[1].field == 2

def test_decode_items_with_supported_generic(monkeypatch):
    class MockGeneric:
        def __init__(self, value):
            self.value = value

    def mock_is_supported_generic(type_arg):
        return type_arg == MockGeneric

    def mock_decode_generic(type_arg, x, infer_missing):
        return MockGeneric(x)

    monkeypatch.setattr('dataclasses_json.core._is_supported_generic', mock_is_supported_generic)
    monkeypatch.setattr('dataclasses_json.core._decode_generic', mock_decode_generic)

    data = [1, 2, 3]
    result = list(_decode_items(MockGeneric, data, infer_missing=False))
    assert all(isinstance(item, MockGeneric) for item in result)
    assert result[0].value == 1
    assert result[1].value == 2
    assert result[2].value == 3

def test_decode_items_with_plain_list():
    data = [1, 2, 3]
    result = _decode_items(int, data, infer_missing=False)
    assert result == data
