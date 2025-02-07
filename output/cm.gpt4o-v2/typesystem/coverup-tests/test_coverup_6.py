# file: typesystem/fields.py:81-92
# asked: {"lines": [81, 82, 83, 85, 87, 88, 90, 92], "branches": [[82, 83], [82, 85], [87, 88], [87, 90]]}
# gained: {"lines": [81, 82, 83, 85, 87, 88, 90, 92], "branches": [[82, 83], [82, 85], [87, 88], [87, 90]]}

import pytest
from typesystem.fields import Field, Union

def test_field_or_with_union():
    field1 = Field(title="Field1")
    field2 = Field(title="Field2")
    union_field = Union(any_of=[field1, field2])

    result = field1 | union_field

    assert isinstance(result, Union)
    assert result.any_of == [field1, field1, field2]

def test_field_or_with_field():
    field1 = Field(title="Field1")
    field2 = Field(title="Field2")

    result = field1 | field2

    assert isinstance(result, Union)
    assert result.any_of == [field1, field2]

def test_union_or_with_union():
    field1 = Field(title="Field1")
    field2 = Field(title="Field2")
    field3 = Field(title="Field3")
    union_field1 = Union(any_of=[field1, field2])
    union_field2 = Union(any_of=[field3])

    result = union_field1 | union_field2

    assert isinstance(result, Union)
    assert result.any_of == [field1, field2, field3]

def test_union_or_with_field():
    field1 = Field(title="Field1")
    field2 = Field(title="Field2")
    union_field = Union(any_of=[field1])

    result = union_field | field2

    assert isinstance(result, Union)
    assert result.any_of == [field1, field2]
