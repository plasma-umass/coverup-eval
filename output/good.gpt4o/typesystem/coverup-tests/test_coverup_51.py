# file typesystem/fields.py:62-63
# lines [62, 63]
# branches []

import pytest
from typesystem.fields import Field

def test_field_serialize():
    field = Field()
    obj = "test_string"
    serialized_obj = field.serialize(obj)
    
    assert serialized_obj == obj

