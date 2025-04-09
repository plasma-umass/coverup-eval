# file dataclasses_json/mm.py:69-113
# lines [69, 70, 71, 72, 73, 74, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 89, 90, 92, 94, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 108, 109, 111, 113]
# branches ['77->78', '77->79', '79->80', '79->89', '80->81', '80->86', '81->82', '81->85', '86->79', '86->87', '98->99', '98->104', '100->101', '100->104', '101->100', '101->102', '104->105', '104->108', '105->104', '105->106']

import pytest
from dataclasses import dataclass, field
from dataclasses_json.mm import _UnionField
from marshmallow import Schema, fields
from typing import Union
import warnings

# Define a simple dataclass for testing
@dataclass
class SimpleDataClass:
    x: int

# Define a schema for the SimpleDataClass
class SimpleDataClassSchema(Schema):
    x = fields.Integer()

# Define a schema for UnionField
class UnionFieldSchema(Schema):
    union_field = _UnionField(
        desc={int: fields.Integer(), SimpleDataClass: SimpleDataClassSchema()},
        cls=SimpleDataClass,
        field=field(metadata={"marshmallow_field": _UnionField}),
    )

# Define a test function to cover the missing lines
@pytest.fixture
def mock_issubclass_safe(mocker):
    return mocker.patch('dataclasses_json.mm._issubclass_safe', return_value=False)

@pytest.fixture
def mock_get_type_origin(mocker):
    return mocker.patch('dataclasses_json.mm._get_type_origin', side_effect=lambda x: x.__args__[0] if hasattr(x, '__args__') else x)

def test_union_field_serialization_deserialization(mock_issubclass_safe, mock_get_type_origin):
    # Create an instance of the schema
    schema = UnionFieldSchema()

    # Test serialization with an unsupported type
    with pytest.warns(UserWarning):
        serialized = schema.dump({'union_field': 3.14})
    assert serialized == {'union_field': 3.14}

    # Test deserialization with an unsupported type
    with pytest.warns(UserWarning):
        deserialized = schema.load({'union_field': 3.14})
    assert deserialized == {'union_field': 3.14}
