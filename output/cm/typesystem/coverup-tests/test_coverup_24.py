# file typesystem/fields.py:81-92
# lines [81, 82, 83, 85, 87, 88, 90, 92]
# branches ['82->83', '82->85', '87->88', '87->90']

import pytest
from typesystem.fields import Field, Union

class MockField(Field):
    pass

def test_field_or_operator_combines_fields_into_union():
    field1 = MockField()
    field2 = MockField()
    field3 = MockField()

    # Test combining two non-Union fields
    union1 = field1 | field2
    assert isinstance(union1, Union)
    assert field1 in union1.any_of
    assert field2 in union1.any_of

    # Test combining a Union with a non-Union field
    union2 = union1 | field3
    assert isinstance(union2, Union)
    assert field1 in union2.any_of
    assert field2 in union2.any_of
    assert field3 in union2.any_of

    # Test combining a non-Union field with a Union
    union3 = field3 | union1
    assert isinstance(union3, Union)
    assert field1 in union3.any_of
    assert field2 in union3.any_of
    assert field3 in union3.any_of

    # Test combining two Unions
    union4 = union1 | union2
    assert isinstance(union4, Union)
    assert field1 in union4.any_of
    assert field2 in union4.any_of
    assert field3 in union4.any_of
    # Ensure that there are no duplicates
    assert len(set(union4.any_of)) == 3
