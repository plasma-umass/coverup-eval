# file: dataclasses_json/core.py:130-208
# asked: {"lines": [131, 132, 133, 134, 135, 136, 137, 138, 140, 141, 142, 143, 144, 145, 146, 149, 151, 152, 153, 156, 157, 159, 160, 161, 162, 163, 164, 165, 166, 169, 171, 172, 173, 175, 176, 177, 179, 181, 182, 184, 185, 187, 188, 189, 194, 195, 197, 198, 199, 200, 201, 202, 203, 205, 206, 208], "branches": [[131, 132], [131, 133], [140, 141], [140, 149], [141, 142], [141, 143], [143, 144], [143, 145], [145, 140], [145, 146], [153, 156], [153, 208], [156, 157], [156, 159], [161, 162], [161, 175], [164, 165], [164, 171], [175, 176], [176, 177], [176, 179], [181, 184], [181, 189], [184, 185], [184, 187], [189, 194], [189, 200], [194, 195], [194, 197], [200, 201], [200, 205]]}
# gained: {"lines": [131, 133, 134, 135, 136, 137, 138, 140, 141, 142, 143, 144, 149, 151, 152, 153, 156, 159, 160, 161, 162, 163, 164, 165, 166, 169, 171, 172, 173, 175, 176, 177, 181, 182, 189, 194, 195, 197, 198, 199, 200, 201, 202, 203, 205, 206, 208], "branches": [[131, 133], [140, 141], [140, 149], [141, 142], [141, 143], [143, 144], [153, 156], [153, 208], [156, 159], [161, 162], [161, 175], [164, 165], [164, 171], [175, 176], [176, 177], [181, 189], [189, 194], [189, 200], [194, 195], [194, 197], [200, 201], [200, 205]]}

import pytest
from dataclasses import dataclass, field, MISSING
from typing import Optional, List, Dict
from unittest.mock import patch
from dataclasses_json.core import _decode_dataclass

@dataclass
class Nested:
    x: int

@dataclass
class TestClass:
    a: int
    b: Optional[str] = None
    c: List[int] = field(default_factory=list)
    d: Dict[str, int] = field(default_factory=dict)
    e: Nested = field(default_factory=lambda: Nested(0))
    f: Optional[Nested] = None

def test_decode_dataclass():
    data = {
        'a': 1,
        'b': 'test',
        'c': [1, 2, 3],
        'd': {'key': 4},
        'e': {'x': 5},
        'f': {'x': 6}
    }

    result = _decode_dataclass(TestClass, data, infer_missing=False)
    assert result == TestClass(a=1, b='test', c=[1, 2, 3], d={'key': 4}, e=Nested(5), f=Nested(6))

def test_decode_dataclass_infer_missing():
    data = {
        'a': 1,
        'c': [1, 2, 3],
        'd': {'key': 4},
        'e': {'x': 5}
    }

    result = _decode_dataclass(TestClass, data, infer_missing=True)
    assert result == TestClass(a=1, b=None, c=[1, 2, 3], d={'key': 4}, e=Nested(5), f=None)

def test_decode_dataclass_with_defaults():
    data = {
        'a': 1,
        'b': 'test'
    }

    result = _decode_dataclass(TestClass, data, infer_missing=False)
    assert result == TestClass(a=1, b='test', c=[], d={}, e=Nested(0), f=None)

def test_decode_dataclass_with_none_value():
    data = {
        'a': 1,
        'b': None,
        'c': None,
        'd': None,
        'e': None,
        'f': None
    }

    with patch('warnings.warn') as mock_warn:
        result = _decode_dataclass(TestClass, data, infer_missing=False)
        assert result == TestClass(a=1, b=None, c=None, d=None, e=None, f=None)
        assert mock_warn.call_count == 3

def test_decode_dataclass_with_infer_missing_and_none_value():
    data = {
        'a': 1,
        'b': None,
        'c': None,
        'd': None,
        'e': None,
        'f': None
    }

    with patch('warnings.warn') as mock_warn:
        result = _decode_dataclass(TestClass, data, infer_missing=True)
        assert result == TestClass(a=1, b=None, c=None, d=None, e=None, f=None)
        assert mock_warn.call_count == 3
