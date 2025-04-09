# file: dataclasses_json/undefined.py:209-241
# asked: {"lines": [209, 210, 211, 212, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 226, 227, 228, 229, 231, 232, 233, 234, 235, 236, 237, 238, 239, 241], "branches": [[221, 223], [221, 224]]}
# gained: {"lines": [209, 210, 211, 212, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 226, 227, 228, 229, 231, 232, 233, 234, 235, 236, 237, 238, 239, 241], "branches": [[221, 223]]}

import pytest
from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, Undefined, CatchAll
from dataclasses_json.undefined import _CatchAllUndefinedParameters, UndefinedParameterError
import inspect
import functools

@dataclass_json(undefined=Undefined.INCLUDE)
@dataclass
class TestClass:
    a: int
    b: int = field(default=0)
    c: dict = field(default_factory=dict)
    catch_all: CatchAll = field(default_factory=dict)

def test_catch_all_init(monkeypatch):
    # Create a mock for the original __init__ method
    def mock_init(self, a, b=0, c=None, catch_all=None, **kwargs):
        self.a = a
        self.b = b
        self.c = c if c is not None else {}
        self.catch_all = catch_all if catch_all is not None else {}
        self.unknown = kwargs

    monkeypatch.setattr(TestClass, '__init__', mock_init)

    # Apply the _CatchAllUndefinedParameters.create_init to TestClass
    new_init = _CatchAllUndefinedParameters.create_init(TestClass)
    monkeypatch.setattr(TestClass, '__init__', new_init)

    # Create an instance of TestClass with extra parameters
    obj = TestClass(1, 2, d=4, e=5)

    # Assertions to verify the behavior
    assert obj.a == 1
    assert obj.b == 2
    assert obj.c == {}
    assert obj.catch_all == {'d': 4, 'e': 5}

    # Clean up
    monkeypatch.undo()
