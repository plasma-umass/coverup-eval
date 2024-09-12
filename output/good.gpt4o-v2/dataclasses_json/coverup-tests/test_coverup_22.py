# file: dataclasses_json/mm.py:318-369
# asked: {"lines": [318, 322, 323, 324, 326, 327, 332, 333, 334, 336, 337, 338, 340, 342, 343, 349, 350, 351, 352, 353, 355, 356, 357, 359, 360, 361, 362, 363, 364, 365, 366, 367, 369], "branches": [[337, 338], [337, 340], [349, 350], [349, 355], [350, 351], [350, 357]]}
# gained: {"lines": [318, 322, 323, 324, 326, 327, 332, 333, 334, 336, 337, 338, 340, 342, 343, 349, 350, 351, 352, 353, 355, 356, 357, 359, 360, 361, 362, 363, 364, 365, 366, 367, 369], "branches": [[337, 338], [349, 350], [349, 355], [350, 351], [350, 357]]}

import pytest
import typing
from marshmallow import Schema
from dataclasses import dataclass, field
from dataclasses_json.mm import build_schema
from dataclasses_json.utils import CatchAllVar

@dataclass
class TestClass:
    a: int
    b: typing.Optional[int] = None
    dataclass_json_config: typing.Optional[str] = None
    catch_all: typing.Optional[CatchAllVar] = field(default_factory=dict)

def test_build_schema(monkeypatch):
    # Arrange
    cls = TestClass
    mixin = object()
    infer_missing = True
    partial = False

    # Act
    schema_cls = build_schema(cls, mixin, infer_missing, partial)
    schema_instance = schema_cls()

    # Assert
    assert issubclass(schema_cls, Schema)
    assert hasattr(schema_cls, 'Meta')
    assert hasattr(schema_instance, 'make_testclass')
    assert hasattr(schema_instance, 'dumps')
    assert hasattr(schema_instance, 'dump')

    # Test the make_instance method
    obj = schema_instance.make_testclass({'a': 1, 'b': 2})
    assert isinstance(obj, TestClass)
    assert obj.a == 1
    assert obj.b == 2

    # Test the dumps method
    json_str = schema_instance.dumps(obj)
    assert '"a": 1' in json_str

    # Test the dump method
    dumped_dict = schema_instance.dump(obj)
    assert dumped_dict['a'] == 1
    assert 'catch_all' not in dumped_dict

    # Test the dump method with many=True
    obj_list = [TestClass(a=1), TestClass(a=2)]
    dumped_list = schema_instance.dump(obj_list, many=True)
    assert len(dumped_list) == 2
    assert dumped_list[0]['a'] == 1
    assert dumped_list[1]['a'] == 2

    # Clean up
    monkeypatch.undo()
