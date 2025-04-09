# file: typesystem/fields.py:81-92
# asked: {"lines": [81, 82, 83, 85, 87, 88, 90, 92], "branches": [[82, 83], [82, 85], [87, 88], [87, 90]]}
# gained: {"lines": [81, 82, 83, 85, 87, 88, 90, 92], "branches": [[82, 83], [82, 85], [87, 88], [87, 90]]}

import pytest
from typesystem.fields import Field, Union

def test_field_or_operator_with_union():
    field1 = Field()
    field2 = Field()
    union1 = Union(any_of=[field1])
    union2 = Union(any_of=[field2])

    result = field1 | union2
    assert isinstance(result, Union)
    assert result.any_of == [field1, field2]

def test_field_or_operator_without_union():
    field1 = Field()
    field2 = Field()

    result = field1 | field2
    assert isinstance(result, Union)
    assert result.any_of == [field1, field2]

def test_union_or_operator_with_union():
    field1 = Field()
    field2 = Field()
    union1 = Union(any_of=[field1])
    union2 = Union(any_of=[field2])

    result = union1 | union2
    assert isinstance(result, Union)
    assert result.any_of == [field1, field2]

def test_union_or_operator_without_union():
    field1 = Field()
    field2 = Field()
    union1 = Union(any_of=[field1])

    result = union1 | field2
    assert isinstance(result, Union)
    assert result.any_of == [field1, field2]
