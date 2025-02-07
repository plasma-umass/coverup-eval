# file: dataclasses_json/core.py:315-338
# asked: {"lines": [320, 321, 322, 323, 324, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 338], "branches": [[320, 321], [320, 330], [322, 323], [322, 326], [330, 331], [330, 334], [334, 336], [334, 338]]}
# gained: {"lines": [320, 321, 322, 323, 324, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 338], "branches": [[320, 321], [320, 330], [322, 323], [322, 326], [330, 331], [330, 334], [334, 336], [334, 338]]}

import pytest
from dataclasses import dataclass, field
from typing import List, Dict, Any
from dataclasses_json import dataclass_json
from dataclasses_json.core import _asdict

@dataclass_json
@dataclass
class TestClass:
    a: int
    b: str
    c: List[int] = field(default_factory=list)
    d: Dict[str, Any] = field(default_factory=dict)

def test_asdict_with_dataclass_instance():
    obj = TestClass(a=1, b="test", c=[1, 2, 3], d={"key": "value"})
    result = _asdict(obj)
    assert result == {
        "a": 1,
        "b": "test",
        "c": [1, 2, 3],
        "d": {"key": "value"}
    }

def test_asdict_with_mapping():
    obj = {"key1": "value1", "key2": "value2"}
    result = _asdict(obj)
    assert result == {"key1": "value1", "key2": "value2"}

def test_asdict_with_collection():
    obj = [1, 2, 3, 4]
    result = _asdict(obj)
    assert result == [1, 2, 3, 4]

def test_asdict_with_non_dataclass_instance():
    obj = "test_string"
    result = _asdict(obj)
    assert result == "test_string"
