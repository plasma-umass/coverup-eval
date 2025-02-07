# file: typesystem/fields.py:62-63
# asked: {"lines": [62, 63], "branches": []}
# gained: {"lines": [62, 63], "branches": []}

import pytest
from typesystem.fields import Field

def test_serialize():
    field = Field()
    obj = "test_object"
    result = field.serialize(obj)
    assert result == obj

