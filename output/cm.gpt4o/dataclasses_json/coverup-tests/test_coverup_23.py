# file dataclasses_json/mm.py:161-163
# lines [161, 162, 163]
# branches []

import pytest
from unittest.mock import MagicMock
from dataclasses_json.mm import SchemaF

def test_schemaf_dump():
    class DummySchema(SchemaF[int]):
        def dump(self, obj: int, many: bool = None) -> str:
            if not isinstance(obj, int):
                raise TypeError("obj must be an int")
            if many is not None and not isinstance(many, bool):
                raise TypeError("many must be a bool")
            if many:
                return str([obj])
            return str(obj)

    schema = DummySchema.__new__(DummySchema)
    result = schema.dump(42)
    assert result == "42"

    result_many = schema.dump(1, many=True)
    assert result_many == "[1]"

    with pytest.raises(TypeError):
        schema.dump("not an int")

    with pytest.raises(TypeError):
        schema.dump(42, many="not a bool")
