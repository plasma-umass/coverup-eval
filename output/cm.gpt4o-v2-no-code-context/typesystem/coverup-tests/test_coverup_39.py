# file: typesystem/fields.py:62-63
# asked: {"lines": [62, 63], "branches": []}
# gained: {"lines": [62, 63], "branches": []}

import pytest
from typesystem.fields import Field

def test_field_serialize():
    field = Field()
    obj = "test_string"
    result = field.serialize(obj)
    assert result == obj

    obj = 123
    result = field.serialize(obj)
    assert result == obj

    obj = {"key": "value"}
    result = field.serialize(obj)
    assert result == obj

    obj = [1, 2, 3]
    result = field.serialize(obj)
    assert result == obj

    obj = None
    result = field.serialize(obj)
    assert result == obj
